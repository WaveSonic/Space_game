import pygame
from random import random, randint
from bullet import Enemy_bullet
pygame.init()
kill = pygame.mixer.Sound('sound/kill.wav')
kill.set_volume(1)
class Enemy(pygame.sprite.Sprite):
    enemy = []
    level = 0
    enemy_image = ['image/Spaceship/ship_2.png', 'image/Spaceship/ship_3.png', 'image/Spaceship/ship_4.png',
                   'image/Spaceship/ship_5.png', 'image/Spaceship/ship_6.png']
    enemy_hp = [100, 200, 400, 1000, 2000]
    enemy_atk = [50, 100, 200, 400, 1000]
    price = [2500, 5000, 10000, 15000, 25000, 50000, 0]
    bullets = pygame.sprite.Group()

    def __init__(self, n, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Enemy.enemy_image[n]).convert_alpha()
        self.image = pygame.transform.flip(self.image, False, True)
        self.image.blit(pygame.image.load('image/hp_bar/100_hp.png'), (0, 0))
        self.rect = self.image.get_rect(center=(x+50, y))
        self.hp = Enemy.enemy_hp[n]
        self.full_hp = Enemy.enemy_hp[n]
        self.atk = Enemy.enemy_atk[n]
        self.score = Enemy.enemy_atk[n]
        self.add(group)
        Enemy.enemy.append(self)


    def update(self):
        n = random()
        if n < 0.008:
            self.shoot()
        self.rect.y += 3
        if self.rect.y >= 800:
            Enemy.enemy.pop(Enemy.enemy.index(self))
            self.kill()
    def hit(self, value):
        self.hp -= value
        if self.hp * 100 / self.full_hp >= 90:
            self.image.blit(pygame.image.load('image/hp_bar/90_hp.png'), (0, 0))
        elif 80 <= self.hp * 100 / self.full_hp < 90:
            self.image.blit(pygame.image.load('image/hp_bar/80_hp.png'), (0, 0))
        elif 70 <= self.hp * 100 / self.full_hp < 80:
            self.image.blit(pygame.image.load('image/hp_bar/70_hp.png'), (0, 0))
        elif 60 <= self.hp * 100 / self.full_hp < 70:
            self.image.blit(pygame.image.load('image/hp_bar/60_hp.png'), (0, 0))
        elif 50 <= self.hp * 100 / self.full_hp < 60:
            self.image.blit(pygame.image.load('image/hp_bar/50_hp.png'), (0, 0))
        elif 40 <= self.hp * 100 / self.full_hp < 50:
            self.image.blit(pygame.image.load('image/hp_bar/40_hp.png'), (0, 0))
        elif 30 <= self.hp * 100 / self.full_hp < 40:
            self.image.blit(pygame.image.load('image/hp_bar/30_hp.png'), (0, 0))
        elif 20 <= self.hp * 100 / self.full_hp < 30:
            self.image.blit(pygame.image.load('image/hp_bar/20_hp.png'), (0, 0))
        elif 10 <= self.hp * 100 / self.full_hp < 20:
            self.image.blit(pygame.image.load('image/hp_bar/10_hp.png'), (0, 0))
        if self.hp <= 0:
            kill.play()
            self.kill()
            Enemy.enemy.pop(Enemy.enemy.index(self))


    def shoot(self):
        bullet = Enemy_bullet(self.rect.x + 50, self.rect.y+100, Enemy.bullets, self.atk)
        return bullet

    @staticmethod
    def create(group):
        n = random()
        if Enemy.level == 0:
            if n >= 0.2:
                e = Enemy(0, randint(0, 1100), 0, group)
                return e
            elif n < 0.4:
                e = Enemy(1, randint(0, 1100), 0, group)
                return e
        elif Enemy.level == 1:
            if n >= 0.6:
                e = Enemy(0, randint(0, 1100), 0, group)
                return e
            elif 0.6 > n >= 0.1:
                e = Enemy(1, randint(0, 1100), 0, group)
                return e
            else:
                e = Enemy(2, randint(0, 1100), 0, group)
                return e
        elif Enemy.level == 2:
            if n >= 0.7:
                e = Enemy(0, randint(0, 1100), 0, group)
                return e
            elif 0.7 > n >= 0.3:
                e = Enemy(1, randint(0, 1100), 0, group)
                return e
            elif 0.3 > n >= 0.1:
                e = Enemy(2, randint(0, 1100), 0, group)
                return e
            else:
                e = Enemy(3, randint(0, 1100), 0, group)
                return e
        elif Enemy.level == 3:
            if n >= 0.8:
                e = Enemy(0, randint(0, 1100), 0, group)
                return e
            elif 0.8 > n >= 0.5:
                e = Enemy(1, randint(0, 1100), 0, group)
                return e
            elif 0.5 > n >= 0.3:
                e = Enemy(2, randint(0, 1100), 0, group)
                return e
            elif 0.3 > n >= 0.1:
                e = Enemy(3, randint(0, 1100), 0, group)
                return e
            else:
                e = Enemy(4, randint(0, 1100), 0, group)
                return e
        elif Enemy.level == 4:
            if n >= 0.8:
                e = Enemy(1, randint(0, 1100), 0, group)
                return e
            elif 0.8 > n >= 0.5:
                e = Enemy(2, randint(0, 1100), 0, group)
                return e
            elif 0.5 > n >= 0.2:
                e = Enemy(3, randint(0, 1100), 0, group)
                return e
            else:
                e = Enemy(4, randint(0, 1100), 0, group)
                return e
        elif Enemy.level == 5:
            if n >= 0.8:
                e = Enemy(2, randint(0, 1100), 0, group)
                return e
            elif 0.8 > n >= 0.4:
                e = Enemy(3, randint(0, 1100), 0, group)
                return e
            else:
                e = Enemy(4, randint(0, 1100), 0, group)
                return e
        elif Enemy.level == 6:
            if n >= 0.5:
                e = Enemy(3, randint(0, 1100), 0, group)
                return e
            else:
                e = Enemy(4, randint(0, 1100), 0, group)
                return e
        else:
            e = Enemy(4, randint(0, 1100), 0, group)
            return e

    @classmethod
    def level_up(cls, obj):
        if obj.score >= cls.price[cls.level]:
            obj.score -= cls.price[cls.level]
            cls.level += 1
            if cls.level >= 6:
                cls.level = 6






