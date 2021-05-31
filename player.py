import pygame
from const import *
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(img_dir+'playerShip.png').convert()
        self.image = player_img
        self.image = pygame.transform.scale(player_img,(50,40))
        self.image.set_colorkey(BLACK) #убирает ненужный цвет, обычно фоновый
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.hp = PLAYER_HP
        self.lives = PLAYER_LIVES
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0 #обнуляем скорость
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]: #если клавиша стрелка влево нажата
            self.speedx = -1 * PLAYER_SPEED #чтобы х уменьшался задаем отрицательную скорость
        if key_state[pygame.K_RIGHT]: #если клавиша стрелка вправо нажата
            self.speedx = PLAYER_SPEED #чтобы х увеличивался задаем положительную скорость
        self.rect.x += self.speedx #прибавляем скорость к координате, меняем положение
        #отслеживаем границы экрана, чтобы игрок за них не выходил
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        now = pygame.time.get_ticks()
        if self.hidden and now - self.hide_timer > 800:
            self.hidden = False
            self.rect.bottom = HEIGHT - 10 
        if self.lives <= 0:
            self.kill()
        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        return bullet

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT + 50)
