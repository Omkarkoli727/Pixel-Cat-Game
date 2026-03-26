import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Pixel Cat")
clock = pygame.time.Clock()
game_active=True
font = pygame.font.Font("GomePixel-DYJX1.otf",50)

sky_surf = pygame.image.load("sky2.png").convert_alpha()
ground_surf = pygame.image.load("ground-0002.png").convert_alpha()
title_surf = font.render("Cat Game",False,(64,64,64))
title_rect = title_surf.get_rect(center=(400,50))

current_time = int(pygame.time.get_ticks() / 1000)
score_surf = font.render(str(current_time), False, (64,64,64))

score_rect=score_surf.get_rect(center=(775,25))

colud_surf_1=pygame.image.load("cloud5t.png").convert_alpha()
colud_rect_1=colud_surf_1.get_rect(center=(700,50))

colud_surf_2=pygame.image.load("cloud2.png").convert_alpha()
colud_rect_2=colud_surf_2.get_rect(center=(100,50))

colud_surf_3=pygame.image.load("cloud3.png").convert_alpha()
colud_rect_3=colud_surf_3.get_rect(center=(370,50))

box_surf = pygame.image.load("catbox11.png").convert_alpha()
box_rect = box_surf.get_rect(midbottom=(600,300))
pygame.draw.rect(screen, "red", box_rect, 2)




player_surf = pygame.image.load("cat3.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(100,355))
pygame.draw.rect(screen, "blue",player_rect, 2)
player_gravity = 0




game_over_surf = pygame.image.load("Game_over_page3.png").convert_alpha()
game_over_rect = game_over_surf.get_rect(center=(400, 200))
gameover_text=font.render("Game Over",False,(64,64,64))
gameover_text_rect=gameover_text.get_rect(center=(400,50))



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            
            pygame.quit()
            exit()
        if game_active:
            
            if event.type==pygame.MOUSEBUTTONDOWN :
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                    
                    player_gravity=-20
            
            if event.type==pygame.KEYDOWN: 
               if event.key==pygame.K_SPACE and player_rect.bottom>=300:
                   player_gravity=-20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player_rect.x += 10

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                box_rect.left = 800
                player_rect.midbottom = (100, 355)
                player_gravity = 0
    start_time = pygame.time.get_ticks()

    if game_active:
            screen.blit(sky_surf,(0,0))
            screen.blit(ground_surf,(0,100))
            

            screen.blit(colud_surf_1,colud_rect_1)
            colud_rect_1.x-=1
            if colud_rect_1.right <=0:
                colud_rect_1.left=800
            screen.blit(colud_surf_2,colud_rect_2)
            colud_rect_2.x-=1
            if colud_rect_2.right <=0:
                colud_rect_2.left=800
            screen.blit(colud_surf_3,colud_rect_3)
            colud_rect_3.x-=1
            if colud_rect_3.right <=0:
                colud_rect_3.left=800
            
            pygame.draw.rect(screen,"#fdb307",title_rect)
            pygame.draw.rect(screen,"#ecb431",title_rect,10)

            
            screen.blit(title_surf,title_rect)

            pygame.draw.rect(screen,"#fdb307",score_rect)
            pygame.draw.rect(screen,"#ecb431",score_rect,50)
            screen.blit(score_surf,score_rect)

            
            

    
            #box
            screen.blit(box_surf,box_rect)
            box_rect.x -=8
            if box_rect.right <=0:
                box_rect.left =800
            
    
            #player
            screen.blit(player_surf,player_rect)
            player_gravity+=1
            player_rect.y+=player_gravity
            if player_rect.bottom >=355:
               player_rect.bottom=355
    
    
    #collision

            player_feet = pygame.Rect(
            player_rect.x + 30,
            player_rect.bottom -80,
            player_rect.width - 80,
            30
        )

            box_hitbox = pygame.Rect(
            box_rect.x + 20,
            box_rect.y + 40,
            box_rect.width - 60,
            box_rect.height - 60
        )

            pygame.draw.rect(screen, "green", player_feet, 2)
            pygame.draw.rect(screen, "red", box_hitbox, 2)

            if player_feet.colliderect(box_hitbox):
                game_active = False

    else:
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(gameover_text,gameover_text_rect)
                
        
        

    
    

    
            
    pygame.display.update()
    clock.tick(60)

