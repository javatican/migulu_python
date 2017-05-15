#
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
red = (255,0,0)
black= (0,0,0)
clock = pygame.time.Clock()
is_done=False
my_rect = pygame.Rect(50,50,400,400)
unit=3.14159/30
start=15*unit
while not is_done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            is_done=True
        
    screen.fill(black)
    # draw a arc
    pygame.draw.arc(screen,red,my_rect,start-unit,start,200)
    pygame.display.update()
    clock.tick(1) 
    start-=unit