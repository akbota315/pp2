import pygame
import random
import time
import psycopg2
from datetime import datetime

# PostgreSQL connection
DB_PARAMS = {
    "database": "lab10",
    "user": "postgres",
    "password": "12345678",
    "host": "localhost",
    "port": "5432"
}

# Get user or create if not exists
def get_user_data(username):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
        last_game = cur.fetchone()
        conn.close()
        if last_game:
            print(f"Welcome back, {username}! Last Level: {last_game[1]}, Last Score: {last_game[0]}")
            return user_id, last_game
        else:
            print(f"Welcome back, {username}! Starting fresh.")
            return user_id, (0, 0)
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        conn.close()
        print(f"New player created: {username}. Starting at Level 0.")
        return user_id, (0, 0)

# Save score to database
def save_game(user_id, score, level):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, score, level, saved_at) VALUES (%s, %s, %s, %s)",
                (user_id, score, level, datetime.now()))
    conn.commit()
    conn.close()

# Get top players
def get_top_scores(limit=5):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        SELECT u.username, MAX(s.score) as max_score
        FROM users u JOIN user_score s ON u.id = s.user_id
        GROUP BY u.username
        ORDER BY max_score DESC
        LIMIT %s
    """, (limit,))
    result = cur.fetchall()
    conn.close()
    return result

# ============ Snake Game ============

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (160, 32, 240)

# Grid
GRID_WIDTH = 20
CELL = 30
WIDTH = GRID_WIDTH * CELL + 200
HEIGHT = 600

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Arial", 24)

# Classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            for _ in range(food.weight):
                self.body.append(Point(head.x, head.y))
            return True
        return False

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= GRID_WIDTH or head.y < 0 or head.y >= HEIGHT // CELL

class Food:
    def __init__(self, snake):
        self.pos = self.generate_position(snake)
        self.weight = random.choice([1, 2, 3])
        self.spawn_time = time.time()
        self.color = {1: GREEN, 2: BLUE, 3: PURPLE}[self.weight]

    def generate_position(self, snake):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if all(segment.x != x or segment.y != y for segment in snake.body):
                return Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def is_expired(self, timeout=7):
        return time.time() - self.spawn_time > timeout

# Grid drawing
def draw_grid():
    for i in range(GRID_WIDTH):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(screen, [WHITE, GRAY][(i+j)%2], (i*CELL, j*CELL, CELL, CELL))

def draw_top_panel():
    pygame.draw.rect(screen, GRAY, (WIDTH - 160, 20, 130, 50))
    pygame.draw.rect(screen, BLACK, (WIDTH - 160, 20, 130, 50), 2)
    text = font.render("Pause (P)", True, BLACK)
    screen.blit(text, (WIDTH - 145, 35))

def draw_score(score, level, fps):
    screen.blit(font.render(f"Score: {score}", True, BLACK), (WIDTH - 145, 90))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (WIDTH - 145, 120))
    screen.blit(font.render(f"Speed: {fps}", True, BLACK), (WIDTH - 145, 150))

    screen.blit(font.render("Top Players:", True, BLACK), (WIDTH - 145, 190))
    for i, (username, best) in enumerate(get_top_scores()):
        screen.blit(font.render(f"{i+1}. {username[:6]}: {best}", True, BLACK), (WIDTH - 145, 220 + i*25))

# Walls
def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, BLACK, (wall[0] * CELL, wall[1] * CELL, CELL, CELL))

# Levels
levels_data = {
    0: {"speed": 3, "walls": []},
    1: {"speed": 4, "walls": [(10, 5)]},
    2: {"speed": 5, "walls": [(5, 8), (15, 12)]},
    3: {"speed": 6, "walls": [(3, 5), (6, 8), (14, 10)]},
    4: {"speed": 7, "walls": [(3, 9), (16, 10)]},
    5: {"speed": 8, "walls": [(5, y) for y in range(5, 15)]},
    6: {"speed": 9, "walls": [(10, y) for y in range(0, 10)] + [(15, y) for y in range(10, 20)]},
}

# Game start
username = input("Enter your username: ")
user_id, (score, level) = get_user_data(username)
FPS = levels_data.get(level, levels_data[0])["speed"]
snake = Snake()
food = Food(snake)
clock = pygame.time.Clock()
death_reason = ""

# Pre-start screen
while True:
    screen.fill(WHITE)
    title = font.render("Press ENTER to Start", True, BLACK)
    screen.blit(title, (WIDTH // 2 - 140, HEIGHT // 2))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            break
    else:
        continue
    break

# Game loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_top_panel()
    draw_score(score, level, FPS)
    draw_walls(levels_data.get(level, {}).get("walls", []))
    food.draw()
    snake.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1: snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1: snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1: snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1: snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_p:
                save_game(user_id, score, level)
                paused = True
                screen.blit(font.render("Paused. Press P to resume.", True, BLACK), (WIDTH // 2 - 160, HEIGHT // 2))
                pygame.display.flip()
                while paused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT: paused = False; running = False
                        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_p: paused = False

    snake.move()
    head = snake.body[0]

    # Death
    if snake.check_wall_collision():
        death_reason = "Hit border!"
        running = False
    elif (head.x, head.y) in levels_data[level]["walls"]:
        death_reason = "Crashed into wall!"
        running = False
    elif head.x >= GRID_WIDTH:
        death_reason = "Crashed into sidebar!"
        running = False

    # Food collision
    if snake.check_collision(food):
        score += food.weight
        food = Food(snake)

    if food.is_expired():
        food = Food(snake)

    # Level up
    if score // 5 > level and level + 1 in levels_data:
        level += 1
        FPS = levels_data[level]["speed"]

    pygame.display.flip()
    clock.tick(FPS)

# Game over screen
screen.fill(WHITE)
screen.blit(font.render("GAME OVER", True, RED), (WIDTH // 2 - 100, HEIGHT // 2 - 60))
screen.blit(font.render(death_reason, True, BLACK), (WIDTH // 2 - 140, HEIGHT // 2 - 20))
screen.blit(font.render(f"Your score: {score}  Level: {level}", True, BLACK), (WIDTH // 2 - 140, HEIGHT // 2 + 20))
screen.blit(font.render("Press ESC to exit", True, BLACK), (WIDTH // 2 - 140, HEIGHT // 2 + 60))
pygame.display.flip()

save_game(user_id, score, level)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit(); exit()
