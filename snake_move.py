import pygame
from random import randrange

#Зададим величину окна и размер секции змейки
window_size=700
section_size=50

#зададим начальное положение змейки и яблока
snake_x,snake_y=randrange(0,window_size,section_size),randrange(0,window_size,section_size)
posittion_apple=randrange(0,window_size,section_size),randrange(0,window_size,section_size)
lengh=1
snake=[(snake_x,snake_y)]

#Зададим направление и скорость движения
route_x,route_y=0,0
speed=5

#Создадим рабочее окно
pygame.init()
screen = pygame.display.set_mode([window_size,window_size])
clock = pygame.time.Clock()

#счётчик очков
font_score =pygame.font.SysFont('Arial',25,bold=True)
score=0

#графика
head=pygame.image.load('images/raccoon_for_game.jpg')
head_game_over=pygame.image.load('images/game_over.jpg')
cookie=pygame.image.load('images/cookie.jpeg').convert()
stripes=pygame.image.load('images/stripes.jpg').convert()
font_end =pygame.font.SysFont('Arial',65,bold=True)
while True:

    screen.fill(pygame.Color('white'))
    #изобразим змейку
    [(pygame.draw.rect(screen , pygame.Color('grey'),(i,j,section_size-2,section_size-2))) for i,j in snake]
    screen.blit(head,[*snake[-1],section_size,section_size])
    #изобразим печеньку
    screen.blit(cookie,[*posittion_apple,section_size,section_size])

    #передвижение змейки
    snake_x+=route_x*section_size
    snake_y+=route_y*section_size
    snake.append((snake_x , snake_y))

    #Поедание яблока
    snake=snake[-lengh:]
    if snake[-1]==posittion_apple:
        posittion_apple = randrange(0, window_size, section_size), randrange(0, window_size, section_size)
        lengh=lengh+1
        speed=speed+0.5
        score=score+1
    render_score=font_score.render('SCORE:'+str(score),0,pygame.Color('red'))
    screen.blit(render_score,[0,0])

    #Обновляем поверхность
    pygame.display.flip()
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #Управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        route_x,route_y = 0, -1
    if key[pygame.K_s]:
        route_x,route_y = 0, 1
    if key[pygame.K_a]:
        route_x, route_y = -1, 0
    if key[pygame.K_d]:
        route_x,route_y = 1, 0

    # Проигрыш
    if snake_x < 0 or snake_x > window_size - section_size or snake_y < 0 or snake_y > window_size - section_size or len(snake) !=len(set(snake)):
        while True:
         screen.blit(head_game_over, [*snake[-1], section_size, section_size])
         render_end = font_end.render('GAME OVER', 0, pygame.Color('red'))
         screen.blit(render_end,(window_size//2-200,window_size//3))
         pygame.display.flip()
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 exit()
