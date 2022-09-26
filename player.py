import pygame
from bullet import Bullet
import json
pygame.init()


class Ship(pygame.sprite.Sprite):
    s = pygame.mixer.Sound('sound/vystril_1.wav')
    s.set_volume(0.1)
    level = 0
    hp = [500, 1000, 1500, 3000, 5000]
    price = [5000, 10000, 25000, 50000, 0]
    skins = ['image/Spaceship/spice_1.png', 'image/Spaceship/spice_2.png', 'image/Spaceship/spice_3.png',
             'image/Spaceship/spice_4.png', 'image/Spaceship/spice_5.png']
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Ship.skins[Ship.level]).convert_alpha()
        self.image.blit(pygame.image.load('image/hp_bar/100_hp.png'), (0, 95))
        self.rect = self.image.get_rect(bottomleft=(600, 800))
        self.speed = speed
        self.hp = Ship.hp[Ship.level]
        self.full_hp = Ship.hp[Ship.level]
        self.bullets = pygame.sprite.Group()
        self.score = 0

    def left(self):
        self.rect.x -= self.speed

    def right(self):
        self.rect.x += self.speed

    def up(self):
        self.rect.y -= self.speed

    def doun(self):
        self.rect.y += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.x + 50, self.rect.y, self.bullets)
        Ship.s.play()
        return bullet

    def hit(self, value):
        self.hp -= value
        if self.hp * 100 / self.full_hp >= 90:
            self.image.blit(pygame.image.load('image/hp_bar/90_hp.png'), (0, 95))
        elif 80 <= self.hp * 100 / self.full_hp < 90:
            self.image.blit(pygame.image.load('image/hp_bar/80_hp.png'), (0, 95))
        elif 70 <= self.hp * 100 / self.full_hp < 80:
            self.image.blit(pygame.image.load('image/hp_bar/70_hp.png'), (0, 95))
        elif 60 <= self.hp * 100 / self.full_hp < 70:
            self.image.blit(pygame.image.load('image/hp_bar/60_hp.png'), (0, 95))
        elif 50 <= self.hp * 100 / self.full_hp < 60:
            self.image.blit(pygame.image.load('image/hp_bar/50_hp.png'), (0, 95))
        elif 40 <= self.hp * 100 / self.full_hp < 50:
            self.image.blit(pygame.image.load('image/hp_bar/40_hp.png'), (0, 95))
        elif 30 <= self.hp * 100 / self.full_hp < 40:
            self.image.blit(pygame.image.load('image/hp_bar/30_hp.png'), (0, 95))
        elif 20 <= self.hp * 100 / self.full_hp < 30:
            self.image.blit(pygame.image.load('image/hp_bar/20_hp.png'), (0, 95))
        elif 10 <= self.hp * 100 / self.full_hp < 20:
            self.image.blit(pygame.image.load('image/hp_bar/10_hp.png'), (0, 95))
        if self.hp <= 0:
            rez = {'6':{'name': "player", 'score':self.score}}
            with open('record_table.json', 'r') as file:
                data = json.load(file)
            data.update(rez)
            b = sorted(data.items(), key=lambda x: x[1]['score'], reverse=True)
            if self.score > b[4][1]['score']:
                new_record = {"1":{'name': b[0][1]['name'], 'score':b[0][1]['score']},
                              "2": {'name': b[1][1]['name'], 'score': b[1][1]['score']},
                              "3": {'name': b[2][1]['name'], 'score': b[2][1]['score']},
                              "4": {'name': b[3][1]['name'], 'score': b[3][1]['score']},
                              "5": {'name': b[4][1]['name'], 'score': b[4][1]['score']},
                              }
                with open('record_table.json', 'w') as file:
                    json.dump(new_record, file)
            return True

    def upgrade_level_hp(self):
        if Ship.level_hp >= 4:
            Ship.level_hp = 4
        Ship.level_hp += 1
        self.hp = Ship.hp[Ship.level_hp]
        self.full_hp = Ship.hp[Ship.level_hp]


    def heal(self):
        if self.score >= (self.full_hp - self.hp) * 5:
            self.score -= (self.full_hp - self.hp) * 5
            self.hp = self.full_hp
            self.image.blit(pygame.image.load('image/hp_bar/100_hp.png'), (0, 95))

    def upgrade(self):
        if self.score >= Ship.price[Ship.level]+(self.full_hp - self.hp) * 5:
            self.score -= Ship.price[Ship.level]+(self.full_hp - self.hp) * 5
            Ship.level += 1
            if Ship.level >= 4:
                Ship.level = 4
            self.full_hp = Ship.hp[Ship.level]
            self.image = pygame.image.load(Ship.skins[Ship.level]).convert_alpha()
            self.hp = self.full_hp
            self.image.blit(pygame.image.load('image/hp_bar/100_hp.png'), (0, 95))
            print(self.hp)






