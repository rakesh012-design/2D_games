import pygame as pg
import time
import random
pg.font.init()
width,height=1000,720
flappy_bird=pg.image.load('flappy_bird_one.png')
flappy_bird=pg.transform.scale(flappy_bird,(40,40))
flappy_bird_rect=flappy_bird.get_rect(topleft=(width//2,height//2))
p1=pg.image.load('pipe.png')
win=pg.display.set_mode((width,height))
p1=pg.transform.scale(p1,(random.randint(100,200),random.randint(100,200)))
p1_rect_top=p1.get_rect(topleft=(width-flappy_bird_rect.width,(height//2)-100))
p1_rect_bottom=p1.get_rect(topleft=(width-flappy_bird_rect.width,(height//2)+200))
pg.display.set_caption('Flappy Bird')
back_ground=pg.image.load('sky.jpg')
run=True
clock=pg.time.Clock()
start_time=time.time()
pipe_li_1=[]
pipe_li_2=[]
font=pg.font.SysFont('Arial',30)
while run:
    elapsed_time=int(abs(time.time()-start_time))
    time_text=font.render(f'Score: {elapsed_time}',1,'black')
    if flappy_bird_rect.y+flappy_bird_rect.height<height:
        flappy_bird_rect.y+=2
    win.blit(back_ground,(0,0))
    win.blit(time_text,(0,10))
    win.blit(flappy_bird,flappy_bird_rect)
    clock.tick(60)
    if len(pipe_li_1)<2:
        new_pipe_top=p1.get_rect(topleft=(width-flappy_bird_rect.width,(height//2)-(random.randint(100,150))))
        new_pipe_bottom=p1.get_rect(topleft=(width-flappy_bird_rect.width,(height//2)+(random.randint(200,250)))) 
        pipe_li_1.append(new_pipe_bottom)
        pipe_li_1.append(new_pipe_top)
    for pipe in pipe_li_1[:]:
        win.blit(p1,pipe)
        pipe.x-=5
        if pipe.right<0:
            pipe_li_1.remove(pipe)
        if flappy_bird_rect.colliderect(pipe) or flappy_bird_rect.colliderect(pipe):
            pg.time.delay(2000)
            run=False
    if (elapsed_time)>1 and elapsed_time%1==0 and len(pipe_li_2)<2:
        new_pipe_top_1=p1.get_rect(topleft=(width-flappy_bird_rect.width,(height//2)-100))
        new_pipe_bottom_1=p1.get_rect(topleft=(width-flappy_bird_rect.width,(height//2)+200)) 
        pipe_li_2.append(new_pipe_bottom_1)
        pipe_li_2.append(new_pipe_top_1)
    
    for pipe in pipe_li_2[:]:
        win.blit(p1,pipe)
        pipe.x-=5
        if pipe.right<0:
            pipe_li_2.remove(pipe)
        if flappy_bird_rect.colliderect(pipe) or flappy_bird_rect.colliderect(pipe):
            pg.time.delay(2000)
            run=False
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
            break
    keys=pg.key.get_pressed()
    if keys[pg.K_UP] and flappy_bird_rect.y-flappy_bird_rect.height>=0:
        flappy_bird_rect.y-=9    
    pg.display.update() 