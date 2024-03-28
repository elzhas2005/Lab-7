import pygame
import datetime
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Mickey Clock')

mickey_face = pygame.image.load(r"C:\Users\user\Desktop\Lab-7\mainclock.png")
mickey_hands1 = pygame.image.load(r"C:\Users\user\Desktop\Lab-7\seconds.png")
mickey_hands2 = pygame.image.load(r"C:\Users\user\Desktop\Lab-7\seconds.png")
face_rect = mickey_face.get_rect(center=(400, 400))
hands_rect = mickey_hands1.get_rect(center=(400, 400))
hands_rect = mickey_hands2.get_rect(center=(400, 400))

def rotate_image(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rotated_rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    now = datetime.datetime.now()
    minutes_angle = now.minute * 6
    seconds_angle = now.second * 6

    minute_hand, minute_rect = rotate_image(mickey_hands1, -minutes_angle, hands_rect.center)
    second_hand, second_rect = rotate_image(mickey_hands2, -seconds_angle, hands_rect.center)

    screen.blit(mickey_face, face_rect.topleft)
    screen.blit(minute_hand, minute_rect.topleft)
    screen.blit(second_hand, second_rect.topleft)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()