from pygame import *

win_w = 600
win_h = 500
back = (90,250,0)
window = display.set_mode((win_w,win_h))
display.set_caption('Ping-pong')
window.fill(back)

clock = time.Clock()
FPS = 60
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
             run = False  
    display.update()
    clock.tick(FPS)
    
    