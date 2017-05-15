import pygame
import os
import random
from card import Card

pygame.display.init()
#
WIDTH=800
HEIGHT=600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
RATIO = (WIDTH/13)/Card.CARD_WIDTH
CARD_WIDTH = WIDTH//13
CARD_HEIGHT = int((WIDTH/13)*(Card.CARD_HEIGHT/Card.CARD_WIDTH))
#
white = (255,255,255)
screen.fill(white)
#
done = False 
dir_name = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_name,"cards.png")
img = pygame.image.load(image_path).convert() 
#scale(Surface, (width, height), DestSurface = None) -> Surface
img = pygame.transform.scale(img, (int(Card.IMAGE_SIZE[0]*RATIO), int(Card.IMAGE_SIZE[1]*RATIO)))
#
cards = Card.create_cards()
#
cover_card = cards[0]
cover_card_rect = cover_card.get_image_rect(RATIO)
# 
sli = cards[1:53]
random.shuffle(sli)
#
dsp_origin_x=1
dsp_origin_y=1
for i in range(0,52):
    m=i//13
    n=i%13
    pos_x=dsp_origin_x+n*CARD_WIDTH
    pos_y=dsp_origin_y+m*CARD_HEIGHT
    card = sli[i]
    rect = card.get_image_rect(RATIO)
    screen.blit(img, (pos_x, pos_y), rect)
#
clock = pygame.time.Clock()
counter=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    s = counter//52
    p = counter%52
    q = p//13
    r = p%13
    if s%2==0:
        rect = cover_card_rect
    else:
        card = sli[p]
        rect = card.get_image_rect(RATIO)
        
    pos_x=dsp_origin_x+r*CARD_WIDTH
    pos_y=dsp_origin_y+q*CARD_HEIGHT
    screen.blit(img, (pos_x, pos_y), rect)
    
    counter+=1
    pygame.display.flip()
    clock.tick(20)
    
