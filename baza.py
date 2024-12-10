import pygame
import random
import os

screen_width = 1920 #ширина игрового окна
screen_height = 1080 #высота игрового окна
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height)) #размер окна
pygame.display.set_caption("Dich polnaya")
my_icon = pygame.image.load('game_icon.png') #настругать иконку надо
pygame.display.set_icon(my_icon)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

#Цвета
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite): #чебуратора сюда надо
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50)) #загрузка спрайта
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = screen_height - 300
        self.velocity_y = 0 #гравитация персонажа
        self.on_ground = False
        self.speed = 5 #скорость персонажа
    
    def update(self):
        self.rect.y += self.velocity_y
        #ходьба
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: #левый поворот
            self.rect.x -= self.speed
        if keys[pygame.K_d]: #правый поворот
            self.rect.x += self.speed
        #проверка выхода за экран
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
        
        if not self.on_ground:
            self.velocity_y += 1
    
    def jump(self):
        if self.on_ground: #проверка где ты
            self.velocity_y = -15
    
    def reset(self):
        self.rect.x = 100
        self.rect.y = screen_height


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('platform_background.jfif') #нужна платформа
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #фон
try:
    background = pygame.image.load('background.jpg').convert()
except pygame.error as e:
    print(f"Не удалось загрузить фон: {e}")
    pygame.quit()
    exit()
background = pygame.transform.scale(background, (screen_width, screen_height))

#группа спрайтов
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
     
#игрок
player = Player()
all_sprites.add(player)

#создание платформ
groud = Platform(0, screen_height - 50, screen_width, 50)
platforms.add(groud)
all_sprites.add(groud)

#доп платформы
for _ in range(5):
    p_width = random.randint(50, 150)
    p_height = 20
    p_x = random.randint(0, screen_width - p_width)
    p_y = random.randint(50, screen_height - 100)
    platform = Platform(p_x, p_y, p_width, p_height)
    platforms.add(platform)
    all_sprites.add(platform)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    
    #Обновление объектов
    all_sprites.update()

    #проверка на столкновение
    player.on_ground = False
    for platform in platforms:
        if player.rect.colliderect(platform.rect) and player.velocity_y >= 0:
            player.rect.bottom = platform.rect.top
            player.velocity = 0
            player.on_ground = True
    
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.display.update()









