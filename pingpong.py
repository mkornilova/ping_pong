from pygame import *

win_w = 600
win_h = 500
back = (90,250,0)
window = display.set_mode((win_w,win_h))
display.set_caption('Ping-pong')
window.fill(back)

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self,imagey,speed,x,y,size_x, size_y ):
        super().__init__()
        self.image = transform.scale(image.load(imagey),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


ball = GameSprite('tenis.jpg',4,200,200,80,50)
clock = time.Clock()
FPS = 60
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
             run = False  
    ball.reset()
    display.update()
    clock.tick(FPS)
    
    
