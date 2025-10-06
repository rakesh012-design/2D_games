import pygame
import time
import random


width,height=1000,720
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('Astroflux')
player_width=20
player_height=40
player_vel=5

bg=pygame.image.load('bg2.jpeg')
bg2=pygame.image.load('bg.jpg')
spaceship=pygame.image.load('spaceship.jpg')
meteor=pygame.image.load('meteor.jpg')
meteor=pygame.transform.scale(meteor,(player_width,player_height))
meteor_rock=pygame.image.load('meteor_rock.jpg')
meteor_rock=pygame.transform.scale(meteor_rock,(100,100))
spaceship=pygame.transform.scale(spaceship,(60,60))
run=True
clock=pygame.time.Clock()
star_count=0
stars=[]
star_height=40
star_width=20
start_time=time.time()
star_increment=2000
stars_td=[]
stars_lr=[]
stars_rl=[]
hit=False
score=0
pygame.font.init()
font=pygame.font.SysFont('comicsans',30)
spaceship_rect=spaceship.get_rect(topleft=(width//2,height-player_height))
player=spaceship_rect
broken_spaceship=pygame.image.load('broken.jpeg')
broken_spaceship=pygame.transform.scale(broken_spaceship,(100,100))
change_time=5000
fireball=pygame.image.load('fireball.jpg')
fireball=pygame.transform.scale(fireball,(60,60))
start_timer=pygame.time.get_ticks()
current_bg=bg
met_fire=[]
bg_y=0
bg_x=0
meteor_rock_li=[]
while run:
    bg_y+=3
    if bg_y>=bg.get_height()-30:
        bg_y=0
    win.blit(current_bg,(bg_x,bg_y))
    win.blit(current_bg,(bg_x,bg_y-bg.get_height()))
    elapsed_time=time.time()-start_time
    spaceship.set_colorkey((255,255,255))
    meteor.set_colorkey((0,20,92))
    win.blit(spaceship,spaceship_rect)
    clock.tick(60)
    timer=pygame.time.get_ticks()-start_timer
    score=int(elapsed_time//2)
    score_text=font.render(f'score:{score}',1,'white') 
    if (len(stars_td)+len(stars_lr)+len(stars_rl))<4:
        for _ in range(4):
            star_x=random.randint(0,width-star_width)
            star_y=random.randint(0,height-star_height)
            star_x_=random.randint(0,width-star_width)
            star_y_=random.randint(0,height-star_height)
            star_td_=pygame.Rect(star_x_,-star_height,star_width,star_height)
            star_lr=pygame.Rect(-star_width,star_y,star_width,star_height)
            star_rl=pygame.Rect(star_width+width,star_y_,star_width,star_height)
            if int(elapsed_time)%5==0:
                for i in range(2):
                    met_x=random.randint(100,width-meteor_rock.get_width())
                    met_y=random.randint(0,height-meteor_rock.get_height())
                    meteor_rock_rect=pygame.Rect(met_x,-meteor_rock.get_height(),meteor_rock.get_width(),meteor_rock.get_height())
            score_rect=pygame.Rect(star_x_+2,-star_height+2,star_width+2,star_height+2)
            stars_lr.append(star_lr)
            stars_td.append(star_td_)
            stars_rl.append(star_rl)   
            meteor_rock_li.append(meteor_rock_rect)
    win.blit(score_text,(10,50))
 
    if len(meteor_rock_li)!=0:
        for i in meteor_rock_li[:]:
            win.blit(meteor_rock,i)  
            meteor_rock.set_colorkey((255,255,255)) 
            i.y+=5
            if i.y>height:
                meteor_rock_li.remove(i)
            if i.colliderect(player):
                hit=True
    for star in stars_td[:]:
        star.y+=5
        win.blit(meteor,star)
        pos_text=font.render(f'{star.y}',1,(255,255,255))
        if star.y>height:
            stars_td.remove(star)
        elif star.colliderect(player):
            hit=True
        elif len(met_fire)!=0:
            if star.colliderect(met_rect):
                stars_td.remove(star)
    for star in stars_lr[:]:
        star.x+=5
        win.blit(meteor,star)
        if star.x>width:
            stars_lr.remove(star)  
        elif star.colliderect(player):
            hit=True
        elif len(met_fire)!=0:
            if star.colliderect(met_rect):
                stars_lr.remove(star)         
    for star in stars_rl[:]:
        star.x-=5
        win.blit(meteor,star)
        if star.x<0:
            stars_rl.remove(star)  
        elif star.colliderect(player):
            hit=True 
        elif len(met_fire)!=0:
            if star.colliderect(met_rect):
                stars_rl.remove(star)                               
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            break 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                for i in range(1):
                    met_rect=pygame.Rect(player.x,player.y,player_width//2,player_height//2)
                    met_fire.append(met_rect)

    if hit:
        broken_spaceship.set_colorkey((224,203,150))
        win.blit(broken_spaceship,spaceship_rect)
        lost_text=font.render(f'you score is :{score}',1,'white')
        win.blit(lost_text,(width//2-lost_text.get_width()/2,height//2-lost_text.get_height()))
        pygame.display.update()
        pygame.time.delay(2000)
        break

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x-player_vel>=0:
        spaceship_rect.x-=player_vel
        player.x-=player_vel
    if keys[pygame.K_RIGHT] and player.x+player_vel+player_width<=width:
        player.x+=player_vel
        spaceship_rect.x+=player_vel
    if keys[pygame.K_UP] and player.y-player_vel>=0:
        player.y-=player_vel
        spaceship_rect.y-=player_vel
    if keys[pygame.K_DOWN] and player.y+player_vel+player_height<=height:
        player.y+=player_vel 
        spaceship_rect.y+=player_vel          
    if met_fire:
        for i in met_fire[:]:
            win.blit(fireball,i)
            i.y-=20
            if i.y<=0:
                met_fire.remove(i)
    
    fireball.set_colorkey((255,255,255))
    pygame.display.update()




    