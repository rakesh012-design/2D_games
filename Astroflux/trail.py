import pygame
import time
import random


width,height=1000,720
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('N/A')
player_width=20
player_height=40
player_vel=5
run=True
player_jump=2.5
gravity=+4
bg=pygame.image.load('bg2.jpeg')
spaceship=pygame.image.load('spaceship.jpg')

while run:
    win.blit(bg,(0,0))
    spaceship.set_colorkey((255,255,255))
    win.blit(spaceship,(100,200))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()        