from const import *
import random
import pygame

class Mob(pygame.sprite.Sprite):
     def __init__(self, meteor_images):
        pygame.sprite.Sprite.__init__(self)
        mob_img = random.choice(meteor_images)
        self.image_orig = mob_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *0.8 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 6)
        self.speedx = random.randrange(-1, 1)
        self.rot = 0
        self.rot_speed = random.randrange(-5,5)
        self.last_update = pygame.time.get_ticks()

     def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.rotate()
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)

     def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            # вычисляем угол поворота
            self.rot = (self.rot + self.rot_speed) % 360
            # поворчиваем оргинал и сохраняем в новое изображение
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            # сохраняем координаты центра старого изображения
            old_center = self.rect.center
            # записываем новое изображение в self.image
            self.image = new_image
            # делаем новый прямоугольник
            self.rect = self.image.get_rect()
            # восстанавливаем координаты центра
            self.rect.center = old_center
