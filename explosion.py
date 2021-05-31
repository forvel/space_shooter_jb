import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, explosion_anim, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.explosion_anim = explosion_anim # делаю словарь с картинками доступным в классе
        self.size = size
        self.image = self.explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0 # номер кадра
        self.frame_rate = 100 #  задержка между кадрами
        self.last_update = pygame.time.get_ticks() # для вычисления времени
        

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame != len(self.explosion_anim[self.size]):
                center = self.rect.center
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
            else:
                self.kill()
