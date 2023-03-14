import pygame
import random
import sys

path_image = '/data/data/com.myapp.myapp/files/app/'
#path_image = 'E:\\копия инфы\\Фильмы\\Мультфильмы\\НУ ПОГОДИ\\Moe\\Программирование\\PY\\Game\\'
clock = pygame.time.Clock()



gs_list = [] # cписок монстров
bullet_list = [] # cписок пуль

pygame.init()

gs_time = pygame.USEREVENT +1
print(gs_time)

pygame.time.set_timer(gs_time, 1500)

screen=pygame.display.set_mode((1600,900))
pygame.display.set_caption('Hello')
icon = pygame.image.load(path_image+'image/icon/icon.webp').convert_alpha()# иконка
gost = pygame.image.load(path_image+'image/gost/gost.png').convert_alpha() # монстр
bullet = pygame.image.load(path_image+'image/bullet/bullet.png').convert_alpha() # пуля
boom = pygame.image.load(path_image+'image/bullet/boom.png').convert_alpha() # взрыв
bg = pygame.image.load(path_image+'image/background/bg.png').convert_alpha() # задний фон

myfont = pygame.font.Font(path_image+'font/cd.ttf', 100)

pygame.display.set_icon(icon)

sound= pygame.mixer.Sound(path_image+'image/sound/muz.mp3')
sound.play()

player_r = [pygame.image.load(path_image+'image/player/right/Pl_r_1.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_r_2.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_r_3.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_r_4.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_r_5.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_r_6.png').convert_alpha()]

player_l = [pygame.image.load(path_image+'image/player/right/Pl_l_1.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_l_2.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_l_3.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_l_4.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_l_5.png').convert_alpha(),
            pygame.image.load(path_image+'image/player/right/Pl_l_6.png').convert_alpha()]



square = pygame.Surface((50,170))
square.fill('Blue')





running = True
pl_count = 0
bg_x = 0
pl_x = 100
pl_y = 700
speed = 25
jump2 = 10
jump = jump2
jp_is = False #прыжок
bullet_count = 5
game_end = False

bullet_speed = 30 # скорость пули
gost_speed = 15 # скорость монстра

text_sur = myfont.render('Вы проиграли', True, 'Blue')
text_sur2 = myfont.render('Начать заново', True, 'Red')
text_sur3 = myfont.render('Выйти из игры', True, 'Blue')

#gs_x=0


#screen.fill((120,23,45))

while running:

    keys = pygame.key.get_pressed()

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x+1601, 0))
    #screen.blit(gost, (1500-gs_x, 650))

    if not game_end: 

        
        pl_rect = player_r[0].get_rect(topleft=(pl_x, pl_y))

        #gs_rect = gost.get_rect(topleft=(1500-gs_x, 650))

        #отслеживание столкновения с монстром
        if gs_list:
            for (i, el) in enumerate(gs_list):
                screen.blit(gost,el)
                el.x -=gost_speed

                if el.x < -20:
                    gs_list.pop(i)


                if pl_rect.colliderect(el):
                    game_end = True

        #отслеживание столкновения монстр с пулей
        if bullet_list:
            for (b_i, b_el) in enumerate(bullet_list):
                screen.blit(bullet,b_el)
                b_el.x +=bullet_speed

                if b_el.x > 1600:
                    bullet_list.pop(b_i)

                else:
                    for (i, el) in enumerate(gs_list):
                        if bullet_list[b_i].colliderect(el):
                            screen.blit(boom,(el.x-10,el.y-10))
                            screen.blit(boom,(el.x+10,el.y+10))
                            screen.blit(boom,el)

                            bullet_list.pop(b_i)
                            gs_list.pop(i)                        

                            

        #gs_x +=20
        # выполнение прыжка
        if not jp_is:
            if keys[pygame.K_UP]:
                jp_is = True
        else:
            if jump >= -jump2:
                if jump > 0:
                    pl_y -= (jump ** 2) / 2
                else:
                    pl_y += (jump ** 2) / 2
                jump -=1
            else:
                jp_is = False
                jump = jump2

        #тслеживание выпуска пули
        #if keys[pygame.K_SPACE]:
        #    bullet_list.append(bullet.get_rect(topleft=(pl_x,pl_y)))


        #отрисовка игрока
        if keys[pygame.K_LEFT]:
            screen.blit(player_l[pl_count], (pl_x, pl_y))

        else:
            screen.blit(player_r[pl_count], (pl_x, pl_y))

        #ограничения передвижения игрока    
        if keys[pygame.K_LEFT] and pl_x>0 and not jp_is:
            pl_x -=speed
        if keys[pygame.K_RIGHT] and pl_x<1500 and not jp_is:
            pl_x +=speed

        #движение фона
        bg_x -=5
        if bg_x==-1600:
            bg_x=0

        #перебор движение игрока    
        if pl_count<5:
            pl_count +=1
        else:
            pl_count=0
    else:
        screen.fill((120,23,45))
        screen.blit(text_sur,(430,100))
        screen.blit(text_sur2,(430,300))
        screen.blit(text_sur3,(430,500))

        sur2_rect=text_sur2.get_rect(topleft=(430,300))
        sur3_rect=text_sur3.get_rect(topleft=(430,500))

        mouse = pygame.mouse.get_pos()

        if sur2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game_end = False
            gs_list.clear()
            bullet_list.clear()
            pl_x = 100
            pl_y = 700
            jp_is = False
            jump = jump2
        
        if sur3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            running = False   
            sys.exit()

    pygame.display.update()

    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running = False
        # elif event.type==pygame.KEYDOWN:
        #     if event.key==pygame.K_a:
        #         print('sdssdcsdc')
        #         screen.fill((70, 44, 13))

        if event.type == gs_time and not game_end:

            gs_list.append(gost.get_rect(topleft=(1600,random.randint(10,800))))
            random.seed()
            #print(gs_list)

        #тслеживание выпуска пули
        if event.type==pygame.KEYUP and keys[pygame.K_SPACE]:
            bullet_list.append(bullet.get_rect(topleft=(pl_x+150,pl_y+50)))

    clock.tick(50)        

    

    
    

    
            