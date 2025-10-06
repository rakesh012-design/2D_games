    for i in meteor_rock_li[:]:
            win.blit(meteor_rock,i)  
            meteor_rock.set_colorkey((255,255,255)) 
            i.y+=5
            if i.y>height:
                meteor_rock_li.remove(i)
            if i.colliderect(player):
                hit=True