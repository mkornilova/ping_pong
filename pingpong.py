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
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_w - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_w - 80:
            self.rect.y += self.speed                

racket1 = Player('racket.png', 4,-35,150,120,200)
racket2 = Player('racket.png', 4,520,150,120,200)
ball = GameSprite('tenis.jpg',4,200,200,80,50)
clock = time.Clock()
FPS = 60
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
             run = False
    window.fill(back)  
    ball.reset()
    racket1.update_r()
    racket2.update_l()
    racket1.reset()
    racket2.reset()
    display.update()
    
    clock.tick(FPS)
    
    
