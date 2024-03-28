import pygame
import os

pygame.init()

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Музыкальный плеер")

music_dir = "C:\\Users\\user\\Desktop\\Lab-7" 

music_files = [file for file in os.listdir(music_dir) if file.endswith('.mp3')]
current_song_index = 0

def play_music():
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song_index]))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_files)
    play_music()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_files)
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 50 <= event.pos[0] <= 100 and 100 <= event.pos[1] <= 150:
                    play_music()
                elif 110 <= event.pos[0] <= 160 and 100 <= event.pos[1] <= 150:
                    stop_music()
                elif 170 <= event.pos[0] <= 220 and 100 <= event.pos[1] <= 150:
                    next_song()
                elif 230 <= event.pos[0] <= 280 and 100 <= event.pos[1] <= 150:
                    previous_song()

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 255, 0), (50, 100, 50, 50))  # Кнопка "Play"
    pygame.draw.rect(window, (255, 0, 0), (110, 100, 50, 50))  # Кнопка "Stop"
    pygame.draw.rect(window, (0, 0, 255), (170, 100, 50, 50))  # Кнопка "Next"
    pygame.draw.rect(window, (255, 255, 0), (230, 100, 50, 50))  # Кнопка "Previous"
    pygame.display.update()
pygame.quit()