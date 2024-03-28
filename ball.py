import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

white = (255, 255, 255)
red = (255, 0, 0)

ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

while True:
    screen.fill(white)

    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y = max(ball_y - ball_speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_y = min(ball_y + ball_speed, screen_height - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_x = max(ball_x - ball_speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_x = min(ball_x + ball_speed, screen_width - ball_radius)

    pygame.display.flip()