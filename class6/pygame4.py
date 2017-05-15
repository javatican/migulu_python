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
my_rect = pygame.Rect(x,y,10,20)
while not is_done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            is_done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            my_rect.y -= step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            my_rect.y += step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            my_rect.x -= step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            my_rect.x += step
    screen.fill(black)
    pygame.draw.rect(screen, red, my_rect)    
    pygame.display.update()
    clock.tick(30)