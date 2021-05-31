import random
import pygame
import sys
from const import *
from player import Player
from mob import Mob
from bullet import Bullet
from explosion import Explosion
from os import path

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My 1st game")
clock = pygame.time.Clock()
# настраиваем шрифт
font_name = pygame.font.match_font('arial')
def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)

def create_new_mob():
    m = Mob(meteor_images)
    all_sprites.add(m)
    mobs.add(m)
def draw_hp_bar(surf, x, y, hp):
    if hp < 0:
        hp = 0
    fill = (hp / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect,2)
    
#вставка фона
background = pygame.image.load(img_dir+'background.png').convert()
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#делаем метеориты разного размера
#список с именами файлов - картинок метеоритов
meteor_list = ['meteorBrown_big1.png','meteorBrown_big2.png','meteorBrown_big3.png',
'meteorBrown_big4.png','meteorBrown_med1.png','meteorBrown_med3.png','meteorBrown_small1.png',
'meteorBrown_small2.png','meteorBrown_tiny1.png','meteorBrown_tiny2.png']
#список изображений метеоритов
meteor_images = []
#проходим по списку файлов и грузим картинку в список изображений
for img in meteor_list:
    meteor_images.append(pygame.image.load(img_dir + img).convert())
# группа для метеоритов   
mobs = pygame.sprite.Group()
for i in range(MOBS_QTY):
    create_new_mob()
#группа для пуль
bullets = pygame.sprite.Group()

#картинки для анимации взрывов
explosion_anim = {}
explosion_anim['large'] = []
explosion_anim['small'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(img_dir + filename).convert()
    img.set_colorkey(BLACK)
    img_large = pygame.transform.scale(img,(75,75))
    explosion_anim['large'].append(img_large)
    img_small = pygame.transform.scale(img,(32,32))
    explosion_anim['small'].append(img_small)
    
#настройка времени для вычисления задержек
newtime = pygame.time.get_ticks()

#иконки для отображения жизней
#???
player_icon = pygame.transform.scale(player.image,(20,16))
player_icon.set_colorkey(BLACK)

run = True
score = 0

while run:
    #задержка на частоту кадров
    clock.tick(FPS)
    # 1 - обработка ввода (клавиши клавиатуры, мышь)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                oldtime = newtime
                newtime = pygame.time.get_ticks()
                if newtime - oldtime > 300:
                    bullet = player.shoot()
                    all_sprites.add(bullet)
                    bullets.add(bullet)
            
    # 2 - изменяем игровые объекты
    all_sprites.update()
    #проверка что пуля попала в астероид
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    
    for hit in hits:
        if hit.radius > 40:
            score += 3
        elif hit.radius < 40 and hit.radius > 18:
            score += 5
        else:
            score += 10
        # на месте астероида создаем взрыв
        explosion = Explosion(explosion_anim, hit.rect.center,'large')
        all_sprites.add(explosion)
        #вместо убитого астероида создаём новый
        create_new_mob()
     
    #проверка что астероид попал в игрока
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        #player.hp -= hit.damage
        if hit.radius >= 40:
            player.hp -= 50
        elif hit.radius < 40 and hit.radius >= 25:
            player.hp -= 20
        elif hit.radius < 25 and hit.radius > 14:
            player.hp -= 10
        else:
            player.hp -= 5
        create_new_mob()
        if player.hp <=0:
            player_explosion = Explosion(explosion_anim, player.rect.center,'small')
            all_sprites.add(player_explosion)
            player.hide()
            player.lives -= 1
            player.hp = 100
            
    # проверка что игрок умер и анимация завершилась
    if not player.alive() and not player_explosion.alive():
        run = False 
    # 3 - отрисовка
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score),SCORE_FONT_SIZE, SCORE_X, SCORE_Y)
    draw_hp_bar(screen, WIDTH - BAR_LENGTH - 10, 10, player.hp)
    draw_lives(screen, WIDTH//2 - 20, 10, player.lives, player_icon)
    pygame.display.flip()

pygame.quit()
sys.exit()
