import os, random, pygame
from director import Scene
from director import Director
from card import Card

class SceneHome(Scene):
    """ Welcome screen of the game, the first one to be loaded."""
    RATIO = (Director.WIDTH/13)/Card.CARD_WIDTH
    CARD_WIDTH = Director.WIDTH//13
    CARD_HEIGHT = int((Director.WIDTH/13)*(Card.CARD_HEIGHT/Card.CARD_WIDTH))
    CARDS_IMAGE= None
    #
    @classmethod
    def get_cards_img(cls):
        if SceneHome.CARDS_IMAGE==None:
            dir_name = os.path.dirname(os.path.realpath(__file__))
            image_path = os.path.join(dir_name,"cards.png")
            img = pygame.image.load(image_path).convert() 
            #scale(Surface, (width, height), DestSurface = None) -> Surface
            SceneHome.CARDS_IMAGE = pygame.transform.scale(img, 
                (int(Card.IMAGE_SIZE[0]*SceneHome.RATIO), 
                int(Card.IMAGE_SIZE[1]*SceneHome.RATIO)))
        return SceneHome.CARDS_IMAGE

    def __init__(self, director):
        super().__init__(director)
        self.img = SceneHome.get_cards_img()
        #
        self.cards = Card.create_cards()
        #
        self.cover_card = self.cards[0]
        self.cover_card_rect = self.cover_card.get_image_rect(SceneHome.RATIO)
        # 
        self.sli = self.cards[1:53]
        random.shuffle(self.sli)
        #
        white = (255,255,255)
        director.screen.fill(white)
        #
        self.dsp_origin_x=1
        self.dsp_origin_y=1
        for i in range(0,52):
            m=i//13
            n=i%13
            pos_x=self.dsp_origin_x+n*SceneHome.CARD_WIDTH
            pos_y=self.dsp_origin_y+m*SceneHome.CARD_HEIGHT
            card = self.sli[i]
            rect = card.get_image_rect(SceneHome.RATIO)
            director.screen.blit(self.img, (pos_x, pos_y), rect)
        self.counter=0
    def on_update(self):
        pass
 
    def on_event(self, event):
        pass
 
    def on_draw(self, screen):
        s = self.counter//52
        p = self.counter%52
        q = p//13
        r = p%13
        if s%2==0:
            rect = self.cover_card_rect
        else:
            card = self.sli[p]
            rect = card.get_image_rect(SceneHome.RATIO)
            
        pos_x=self.dsp_origin_x+r*SceneHome.CARD_WIDTH
        pos_y=self.dsp_origin_y+q*SceneHome.CARD_HEIGHT
        screen.blit(self.img, (pos_x, pos_y), rect)
        
        self.counter+=1
