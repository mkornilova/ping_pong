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


racket1 = Player('racket.png', 4,3,150,2,200)
racket2 = Player('racket.png', 4,595,150,2,200)
ball = GameSprite('tenis.jpg',4,200,200,80,50)
clock = time.Clock()
FPS = 60
run = True
finish = False
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))

speed_x = 3
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
             run = False  
    if  not finish:
        window.fill(back)  
        #ball.reset()
        racket1.update_r()
        racket2.update_l()
        #racket1.reset()
        #racket2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
        if ball.rect.y > win_h-50 or ball.rect.y <0:
            speed_y *= -1
        if ball.rect.x <0:
            finish = True
            window.blit(lose1,(200,200))
            game_over = True
        if ball.rect.x > win_w:
            finish = True
            window.blit(lose2,(200,200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()

    clock.tick(FPS)
