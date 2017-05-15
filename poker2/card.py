class Card:
    IMAGE_SIZE=(2179,1216)
    CARD_WIDTH=IMAGE_SIZE[0]/13
    CARD_HEIGHT=IMAGE_SIZE[1]/5
    @classmethod
    def create_cards(cls):
        cards=[]
        card=Card(0, 0, 0)
        cards.append(card)
        id=1
        for i in range(1,5):
            for j in range(1,14):
                card=Card(id, i, j)
                cards.append(card)
                id+=1
        card=Card(53, 5, 14)
        cards.append(card)
        card=Card(54, 5, 14)
        cards.append(card)
        return cards
        
    def __init__(self, id, suit, number):
        # 1-52 FOR NORMAL CARDS, 53 FOR BLACK JOKER, 54 FOR RED JOKER, 0 FOR COVER CARD
        self.id = id 
        #1: CLUB, 2: DIAMOND, 3: HEART, 4:SPACE, 5. JOKER, 0 FOR COVER CARD
        self.suit= suit
        # 1 TO 13,  14 FOR JOKER, O FOR COVER CARD
        self.number=number
        self.rect = None
        
    def get_image_rect(self, ratio):
        if self.rect==None:
            if self.id>=1 and self.id<=52:
                x=(self.number-1)*Card.CARD_WIDTH
                y=(self.suit-1)*Card.CARD_HEIGHT
            elif self.id==0:
                x=2*Card.CARD_WIDTH
                y=4*Card.CARD_HEIGHT
            elif self.id==53:
                x=0
                y=4*Card.CARD_HEIGHT
            elif self.id==54:
                x=Card.CARD_WIDTH
                y=4*Card.CARD_HEIGHT
            else:
                print("Error when calling get_image_rect()")
            self.rect =  (x,y,Card.CARD_WIDTH,Card.CARD_HEIGHT)
        return (self.rect[0]*ratio, self.rect[1]*ratio, self.rect[2]*ratio, self.rect[3]*ratio)
    def __str__(self):
        return "[%d, %d, %d]" % (self.id, self.suit, self.number)
    def __repr__(self):
        return "[%d, %d, %d]" % (self.id, self.suit, self.number)
    
        