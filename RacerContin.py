import pygame, sys, os, random, time
from pygame.locals import *


pygame.init()
pygame.mixer.init()

FPS = 60
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0


font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font_big.render("Game Over", True, BLACK)


current_dir = os.path.dirname(__file__)
background_path = os.path.join(current_dir, "AnimatedStreet.png")
player_path = os.path.join(current_dir, "Player.png")
enemy_path = os.path.join(current_dir, "Enemy.png")
coin_path = os.path.join(current_dir, "coin.png")
sound_path = os.path.join(current_dir, "coin_sound.wav")


background = pygame.image.load(background_path)
player_image = pygame.image.load(player_path)
enemy_image = pygame.image.load(enemy_path)
coin_image = pygame.image.load(coin_path)
coin_image = pygame.transform.scale(coin_image, (30, 30))


if os.path.exists(sound_path):
    coin_sound = pygame.mixer.Sound(sound_path)
    coin_sound.set_volume(1.0)
else:
    print("coin_sound.wav not found")
    coin_sound = None


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, enemies_group):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.value = random.choice([1, 3, 5])  
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            too_close = False
            for enemy in enemies_group:
                if self.rect.colliderect(enemy.rect.inflate(60, 100)):
                    too_close = True
                    break
            if not too_close:
                break

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)

C1 = Coin(enemies)
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    screen.blit(background, (0, 0))

    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in coins:
            COINS += coin.value  
            if coin_sound:
                coin_sound.play()
            coin.kill()
            new_coin = Coin(enemies)
            coins.add(new_coin)
            all_sprites.add(new_coin)

    
        if COINS % 10 == 0:
            SPEED += 1

    
    pygame.display.update()
    clock.tick(FPS)
