import random
import pygame 
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = (370, 480)
    def update(self, speed):
        self.rect.move_ip(speed, 0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, picture_path, center):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.gunshot = pygame.mixer.Sound('laser-2.mp3')
    def update(self):
        self.rect.move_ip(0, -10)
        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.kill()
    def shoot(self):
        self.gunshot.play()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.enemy_speedx = random.randrange(1, 3)
        self.enemy_speedy = random.randrange(1, 2)
    def update(self):
        self.rect.move_ip((self.enemy_speedx * 2), 1)
        if self.rect.centerx >= 768:
            self.rect.centerx = 768
            self.enemy_speedx *= -1
        elif self.rect.centerx <= 32:
            self.rect.centerx = 32
            self.enemy_speedx *= -1
        if pygame.sprite.spritecollide(self, player_group, True):
            pass


            # Enemies should move at varying speeds
# design enemy movement


# initialize pygame
pygame.init()
clock = pygame.time.Clock()
# create window & customize
screen_height = 800
screen_width = 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)
background = pygame.image.load('stars.png')
# initialize player
player = Player('spaceship.png')
player_group = pygame.sprite.Group()
player_group.add(player)
# initialize bullet group
bullet_group = pygame.sprite.Group()
# initialize enemy
enemy_group = pygame.sprite.Group()
for enemy in range(10):
    new_enemy = Enemy('ufo.png', random.randrange(0, screen_width), random.randrange(0, 150))
    enemy_group.add(new_enemy)
speed = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -5
            elif event.key == pygame.K_RIGHT:
                speed = 5
            elif event.key == pygame.K_SPACE and len(player_group) > 0:
                bullet = Bullet('bullet.png', player.rect.center)
                bullet_group.add(bullet)
                bullet.shoot()
        elif event.type == pygame.KEYUP:
            speed = 0
    
    # create player boundaries
    if player.rect.centerx >= 768:
        player.rect.centerx = 768
    elif player.rect.centerx <= 32:
        player.rect.centerx = 32

    pygame.display.update()
    screen.fill((0,0,0))
    player_group.draw(screen)
    player_group.update(speed)
    enemy_group.draw(screen)
    enemy_group.update()
    bullet_group.draw(screen)
    bullet_group.update()
    # if len(player_group) < 1:
    #     gameover 
    clock.tick(30)

""" Another option for keeping window open
running = True
while running:
    for key in pygame.event.get():
        if key.type == pygame.QUIT:
            running = False
"""


# Thanks to 
# Icon Creator:
# <a href="https://www.flaticon.com/free-icons/space-invaders" title="space invaders icons">Space invaders icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/spaceship" title="spaceship icons">Spaceship icons created by dDara - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/alien" title="alien icons">Alien icons created by Pixel Buddha - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/bullet" title="bullet icons">Bullet icons created by Smashicons - Flaticon</a>