import pygame
pygame.init()
screen  = pygame.display.set_mode((400,300))
exit = False
clock = pygame.time.Clock()
is_red = True
red =(255,0,0)
green =(0,255,0)
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit =True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_red = not is_red
        if is_red:
            color = red
        else:
            color=green
    #draw.rect(底層的視窗, 顏色, 矩形的位置及大小, 模式)
    pygame.draw.rect(screen,color, pygame.Rect(10,20,30,50), 1);
    pygame.draw.circle(screen, color, (50,50), 50)
    pygame.display.update()
    clock.tick(30)
    #print(clock.get_time())
pygame.quit()      
