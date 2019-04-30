import pygame
import sys

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Megalopong")


posX = 150
posY = 150

blockX = 30
blockY = 100

block2X = 360
block2Y = 0

width = 10
height = 100

FPS = 60
clock = pygame.time.Clock()

moveUp1 = True
moveDown1 = False
moveLeft1 = False
moveRight1 = False

moveUp2 = True
moveDown2 = False
moveLeft2 = False
moveRight2 = False

moveUp = True
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
    if any(blockY<= Y <= blockY+100 for Y in range(posX-10, posX+10)) and blockX == (posX+10):
        pygame.quit()
        sys.exit()

    if any(block2Y<= Y <= block2Y+100 for Y in range(posX-10, posX+10)) and block2X + 10 == (posX+10):
        pygame.quit()
        sys.exit()

    if blockY >= 0 and moveUp1:
        blockY -= 10
        if blockY < 0:
            moveUp1 = False
            moveDown1 = True
    elif (blockY + 100) <= 400 and moveDown1:
        blockY += 10
    else:
        moveUp1 = True
        moveDown1 = False


    if block2Y >= 0 and moveUp2:
        block2Y -= 10
        if block2Y < 0:
            moveUp2 = False
            moveDown2 = True
    elif (block2Y + 100) <= 400 and moveDown2:
        block2Y += 10
    else:
        moveUp2 = True
        moveDown2 = False
        
    
    if moveUp and posY >= 15:
        posY -= 5
    elif moveDown and posY <=400 - 15:
        posY += 5
    elif moveLeft and posX >= 15:
        posX -= 5
    elif moveRight and posX <= 400 - 15:
        posX += 5
    
#grapes
        
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,0,0), (int(posX),int(posY)), 10)
    pygame.draw.rect(screen, (255,255,255), (int(blockX), int(blockY),width,height))
    pygame.draw.rect(screen, (255,255,255), (int(block2X), int(block2Y),width,height))

    pygame.display.update()
