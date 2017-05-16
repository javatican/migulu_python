import os, random, pygame
from director import Scene
from director import Director
from card import Card 

class SceneHome(Scene):
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
        # no shuffle card
        #random.shuffle(self.sli)
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
        # create a button 
        font = pygame.font.SysFont("dejavuserif", 36)  
        black = (0,0,0)
        text_sur = font.render("START", True, black)  
        #
        yellow = (255,255,0)
        button_sur = pygame.Surface(text_sur.get_size()) 
        button_sur.fill(yellow) 
        #
        button_sur.blit(text_sur,(0,0))
        self.button_rect = director.screen.blit(button_sur,(350,450))
        #
        self.counter=0
        
    def on_update(self):
        pass
 
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(pos):
                scene = SceneGame(self.director)
                self.director.change_scene(scene)
 
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


class SceneGame(Scene):
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
            #card = self.sli[i]
            #rect = card.get_image_rect(SceneHome.RATIO)
            director.screen.blit(self.img, (pos_x, pos_y), self.cover_card_rect)
        
        self.card1=None
        self.card2=None
        self.card1_indices=None
        self.card2_indices=None
        self.empty_rect_sur = pygame.Surface((SceneHome.CARD_WIDTH,SceneHome.CARD_HEIGHT)) 
        self.empty_rect_sur.fill(white) 
    def on_update(self):
        pass
 
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #pos = pygame.mouse.get_pos()
            pos = event.pos
            i = pos[1]//SceneHome.CARD_HEIGHT
            j = pos[0]//SceneHome.CARD_WIDTH
            if i>=0 and i<4 and j>=0 and j<13:
                card = self.sli[i*13+j]
                #
                if card.valid:
                    to_show = False
                    if self.card1==None:
                        self.card1 = card
                        self.card1_indices=(i,j)
                        to_show=True
                    elif self.card2==None:
                        # check if a card been clicked twice
                        if card.id!=self.card1.id:
                            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                            self.card2 = card
                            self.card2_indices=(i,j)
                            to_show=True
                    if to_show:
                        pos_x=self.dsp_origin_x+j*SceneHome.CARD_WIDTH
                        pos_y=self.dsp_origin_y+i*SceneHome.CARD_HEIGHT
                        rect = card.get_image_rect(SceneHome.RATIO)
                        self.director.screen.blit(self.img, (pos_x, pos_y), rect)

    def on_draw(self, screen):
        if self.card1 and self.card2 :
            pygame.display.flip()
            pygame.time.wait(2000)
            if self.card1.number == self.card2.number:
                self.card1.invalid()
                self.card2.invalid()
                #blit 2 white rects
                pos_x=self.dsp_origin_x+self.card1_indices[1]*SceneHome.CARD_WIDTH
                pos_y=self.dsp_origin_y+self.card1_indices[0]*SceneHome.CARD_HEIGHT
                self.director.screen.blit(self.empty_rect_sur,(pos_x,pos_y))
                #
                pos_x=self.dsp_origin_x+self.card2_indices[1]*SceneHome.CARD_WIDTH
                pos_y=self.dsp_origin_y+self.card2_indices[0]*SceneHome.CARD_HEIGHT
                self.director.screen.blit(self.empty_rect_sur,(pos_x,pos_y))

            else:
                #blit 2 cover card
                pos_x=self.dsp_origin_x+self.card1_indices[1]*SceneHome.CARD_WIDTH
                pos_y=self.dsp_origin_y+self.card1_indices[0]*SceneHome.CARD_HEIGHT
                self.director.screen.blit(self.img, (pos_x, pos_y), self.cover_card_rect )
                #
                pos_x=self.dsp_origin_x+self.card2_indices[1]*SceneHome.CARD_WIDTH
                pos_y=self.dsp_origin_y+self.card2_indices[0]*SceneHome.CARD_HEIGHT
                self.director.screen.blit(self.img, (pos_x, pos_y), self.cover_card_rect )
                #
            self.card1 = None 
            self.card2 = None 
            self.card1_indices=None
            self.card2_indices=None
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)