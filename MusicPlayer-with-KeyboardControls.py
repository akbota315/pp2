import pygame
import os

pygame.init()

script_dir = os.path.dirname(__file__)
music_folder = os.path.join(script_dir, "music")
background_path = os.path.join(script_dir, "background.jpg")

if not os.path.exists(music_folder):
    print(f"Error: Folder {music_folder} not found!")
    exit()

tracks = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
if not tracks:
    print("Error: No MP3 files found in 'music' folder!")
    exit()

current_track = 0
pygame.mixer.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Music Player 🎵")
font = pygame.font.Font(None, 28)

if os.path.exists(background_path):
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
else:
    background = None

def play_track(index):
    pygame.mixer.music.load(os.path.join(music_folder, tracks[index]))
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    print(f"Now playing: {tracks[index]}")

running, is_playing = True, False

while running:
    screen.blit(background, (0, 0)) if background else screen.fill((20, 20, 20))
    
    
    track_name = tracks[current_track]
    font = pygame.font.Font(None, 24)
    while font.size(track_name)[0] > screen.get_width() - 40:
        track_name = track_name[:-4] + "..."

    shadow = font.render(track_name, True, (0, 0, 0))
    shadow_rect = shadow.get_rect(center=(screen.get_width() // 2 + 2, screen.get_height() - 25 + 2))
    screen.blit(shadow, shadow_rect)

    track_text = font.render(track_name, True, (255, 255, 255))
    text_rect = track_text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 25))
    screen.blit(track_text, text_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            pygame.mixer.music.stop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_playing = not is_playing
                pygame.mixer.music.pause() if not is_playing else play_track(current_track)
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_playing = False
            elif event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                current_track = (current_track + (1 if event.key == pygame.K_RIGHT else -1)) % len(tracks)
                play_track(current_track)
                is_playing = True
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                volume = pygame.mixer.music.get_volume()
                volume += 0.1 if event.key == pygame.K_UP else -0.1
                pygame.mixer.music.set_volume(min(max(volume, 0), 1))

pygame.quit()
