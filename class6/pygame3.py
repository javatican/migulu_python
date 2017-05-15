#
import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
x=10
y=10
step=50
red = (255,0,0)
black= (0,0,0)
clock = pygame.time.Clock()
is_done=False
while not is_done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            is_done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            y-=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            y+=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            x-=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            x+=step
    screen.fill(black)
    pygame.draw.rect(screen, red, pygame.Rect(x,y,10,20))    
    pygame.display.update()
    clock.tick(30)