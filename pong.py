import pygame
import sys

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Megalopong")

posX = 150
posY = 150

blockX = 30
blockY = 30

width = 10
height = 100

block2X = 360
block2Y = 30


FPS = 180
clock = pygame.time.Clock()

moveUp = False
moveDown = False
moveLeft = False
moveRight = False

while True:
    clock.tick(FPS)
    keypressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveUp = True
                moveDown = False
                moveLeft = False
                moveRight = False
            if event.key == pygame.K_s:
                moveDown = True
                moveUp = False
                moveLeft =False
                moveRight = False
            if event.key == pygame.K_a:
                moveLeft = True
                moveUp = False
                moveDown = False
                moveRight = False
            if event.key == pygame.K_d:
                moveRight = True
                moveUp = False
                moveDown = False
                moveLeft = False
    if moveUp and posY >= 15:
        posY -= 5
    elif moveDown and posY <=400 - 15:
        posY += 5
    elif moveLeft and posX >= 15:
        posX -= 5
    elif moveRight and posX <= 400 - 15:
        posX += 5
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,0,0), (int(posX),int(posY)), 10)
    pygame.draw.rect(screen, (255,255,255), (int(blockX), int(blockY),width,height))
    pygame.draw.rect(screen, (255,255,255), (int(block2X), int(block2Y),width,height))

    pygame.display.update()


