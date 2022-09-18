from Enemy import Enemy
from player import *
from bullet import Bullet, Enemy_bullet
pygame.init()


def game(level):
    # USER_EVENT
    fire = pygame.USEREVENT + 0
    pygame.time.set_timer(fire, 500)
    create_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(create_enemy, 1500)
    # END USER_EVENT
    clock = pygame.time.Clock()
    FPS = 60
    screen = pygame.display.set_mode((1200, 800))
    back = pygame.image.load('image/background/background.png').convert_alpha()
    screen.blit(back, (0, 0))
    player = Ship('image/Spaceship/spice_1.png', 10)
    enemys = pygame.sprite.Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == fire:
                player.shoot()
            elif event.type == create_enemy:
                Enemy.create(enemys, level)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level += 1

        btn = pygame.key.get_pressed()
        if btn[pygame.K_LEFT]:
            if player.rect.x <= 0:
                player.rect.x = 0
            player.left()
        elif btn[pygame.K_RIGHT]:
            if player.rect.x >= 1100:
                player.rect.x = 1100
            player.right()

        for en in Enemy.enemy:
            for bul in Bullet.bullet:
                if en.rect.collidepoint(bul.rect.x, bul.rect.y):
                    en.hit(Bullet.bullet_damage[Bullet.n])
                    bul.kill()
                    bul.kill_()

        for bullet_en in Enemy_bullet.bullet:
            if player.rect.collidepoint(bullet_en.rect.x, bullet_en.rect.y):
                player.hit(bullet_en.atk)
                bullet_en.kill()
                bullet_en.kill_()

        screen.blit(back, (0, 0))
        screen.blit(player.image, player.rect)
        player.bullets.draw(screen)
        enemys.draw(screen)
        for x in Enemy.enemy:
            x.bullets.draw(screen)
            x.bullets.update()
        player.bullets.update()
        pygame.display.update()
        enemys.update()
        clock.tick(FPS)
