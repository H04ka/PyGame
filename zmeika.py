import pygame
import time
import random
pygame.init()
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
YELLOW = (255,255,102)
RED = (213,50,80)
screen_width = 1920 #ширина игрового окна
screen_height = 1080 #высота игрового окна
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height)) #размер окна
pygame.display.set_caption("Dich polnaya")
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Ваш счёт:" + str(score), True, YELLOW)
    screen.blit(value, [0,0])

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block,snake_block])

def message(msg, color):
    mesg = font_style.render(msg,True,color)
    screen.blit(mesg, [screen_width/6], screen_height/3)

def gameLoop():
    game_over = False
    game_close = False
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, screen_width - snake_block)/10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block)/ 10.0)* 10.0
    while not game_over:
        while game_close == True:
            screen.fill(BLUE)
            message("вы проиграли, завершите на Q или нажмите V чтобы повторить", RED)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_v:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.type == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.type == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.type == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block)/10) * 10
            foody = round(random.randrange(0, screen_height - snake_block)/10) * 10
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()


            
