import pygame

class Bullet(pygame.sprite.Sprite):
    bullet = []
    level = 0
    bullet_image = ['image/fire/fire_0.png', 'image/fire/fire_2.png', 'image/fire/fire_3.png', 'image/fire/fire_4.png',
                    'image/fire/fire_5.png']
    bullet_damage = [50, 100, 200, 350, 500]
    price = [5000, 10000, 15000, 25000, 0]

    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Bullet.bullet_image[Bullet.level]).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.damage = Bullet.bullet_damage[Bullet.level]
        self.add(group)
        Bullet.bullet.append(self)


    def update(self):
        self.rect.y -= 10
        if self.rect.y <= 0:
            Bullet.bullet.pop(Bullet.bullet.index(self))
            self.kill()

    def kill_(self):
        Bullet.bullet.pop(Bullet.bullet.index(self))

    @classmethod
    def upgrade(cls, obj):
        if obj.score >= cls.price[cls.level]:
            obj.score -= cls.price[cls.level]
            cls.level += 1
            if cls.level >= 4:
                cls.level = 4



class Enemy_bullet(Bullet):
    bullet = []
    bullet_image = 'image/fire/fire_1.png'
    bullet_damage = [50, 100, 200, 500, 1000]

    def __init__(self, x, y, group, atk):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Enemy_bullet.bullet_image).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        Enemy_bullet.bullet.append(self)
        self.atk = atk

    def update(self):
        self.rect.y += 3
        if self.rect.y > 1000:
            Enemy_bullet.bullet.pop(Enemy_bullet.bullet.index(self))
            self.kill()

    def kill_(self):
        Enemy_bullet.bullet.pop(Enemy_bullet.bullet.index(self))




