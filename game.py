import pygame.mixer_music
from Enemy import Enemy
from player import *
from bullet import Bullet, Enemy_bullet
from game_over import game_over
from pause import pause
from upgarade import upgrade

pygame.mixer.music.load('sound/back.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)
p = pygame.mixer.Sound('sound/pause.wav')
p.set_volume(0.6)
hit = pygame.mixer.Sound('sound/hit.wav')
hit.set_volume(0.6)


pygame.init()
def game():
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
    player = Ship(10)
    enemys = pygame.sprite.Group()


    font = pygame.font.SysFont('Impact', 24)

    g = True


    while g:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == fire:
                player.shoot()
                print(Enemy.enemy)
            elif event.type == create_enemy:
                Enemy.create(enemys)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    p.play()
                    pause()
                    p.play()
                elif event.key == pygame.K_SPACE:
                    p.play()
                    upgrade(player)
                    p.play()



        btn = pygame.key.get_pressed()
        if btn[pygame.K_LEFT]:
            if player.rect.x <= 0:
                player.rect.x = 0
            player.left()
        elif btn[pygame.K_RIGHT]:
            if player.rect.x >= 1100:
                player.rect.x = 1100
            player.right()
        elif btn[pygame.K_UP]:
            if player.rect.y <= 0:
                player.rect.y = 0
            player.up()
        elif btn[pygame.K_DOWN]:
            if player.rect.y >= 677:
                player.rect.y = 677
            player.doun()
        elif btn[pygame.K_LSHIFT]:
            player.score = 1000000

        for en in Enemy.enemy:
            for bul in Bullet.bullet:
                if en.rect.collidepoint(bul.rect.x, bul.rect.y):
                    hit.play()
                    en.hit(bul.damage)
                    player.score += en.score
                    bul.kill()
                    bul.kill_()

        for bullet_en in Enemy_bullet.bullet:
            if player.rect.collidepoint(bullet_en.rect.x, bullet_en.rect.y):
                hit.play()
                x = player.hit(bullet_en.atk)
                bullet_en.kill()
                bullet_en.kill_()
                if x:
                    Enemy.enemy = []
                    Bullet.bullet = []
                    Enemy_bullet.bullet = []
                    for x in enemys:
                        x.kill()
                    for x in Enemy.bullets:
                        x.kill()
                    pygame.display.update()
                    game_over(player.score)
                    g = False


        screen.blit(back, (0, 0))
        enemys.draw(screen)
        for x in Enemy.enemy:
            x.bullets.draw(screen)
            x.bullets.update()
        screen.blit(player.image, player.rect)
        player.bullets.draw(screen)
        player.bullets.update()

        score = font.render(f"Score: {player.score}", True, (255, 0, 0))
        screen.blit(score, (0, 0))
        tip = font.render('?????????? ???????????? ?????? ???????????????? ???????? ????????????????', True, (255, 0, 0))
        if player.hp * 100 / player.full_hp < 30:
            screen.blit(tip, (400, 0))

        enemys.update()
        pygame.display.update()
        clock.tick(FPS)
