import sys
import pygame


pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от клавиатуры")
#pygame.display.set_icon(pygame.image.load("app.bmp"))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()

x = W // 2
y = H // 2
speed = 5

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed
            elif event.key == pygame.K_RIGHT:
                x += speed

            elif event.key == pygame.K_q:
                y -= speed
                x -= speed

            elif event.key == pygame.K_DOWN:
                y += speed


    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 30, 30))
    pygame.display.update()

    clock.tick(FPS)
