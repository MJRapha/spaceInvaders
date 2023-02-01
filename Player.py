import pygame
#import random
from Bullet import Bullet

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self, p_win, p_player_img, p_bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.win = p_win
        self.winWidth = p_win.get_width()
        self.winHeight = p_win.get_height()
        #self.s_width = p_width
        #self.s_height = p_height
        self.image = pygame.transform.scale(p_player_img, (70, 70))
        self.image.set_colorkey(BLACK)
        #self.color = self.image.fill(p_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.winWidth / 2
        self.rect.bottom = self.winHeight - 10
        self.speedX = 0
        self.bullet_image = p_bullet_img
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.speedX = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speedX = -20
        if key_state[pygame.K_RIGHT]:
            self.speedX = 20
        self.rect.x += self.speedX
        if self.rect.right > self.winWidth:
            self.rect.right = self.winWidth
        if self.rect.left < 0:
            self.rect.left = 0
        self.bullets.draw(self.win)
        self.bullets.update()

    def shoot(self):
        bullet = Bullet(self.win, self.rect.centerx, self.rect.top, self.bullet_image)
        self.bullets.add(bullet)

    #def change_color(self):
        #r_color = random.randint(0, 255)
        #g_color = random.randint(0, 255)
        #b_color = random.randint(0, 255)
        #self.color = self.image.fill((r_color, g_color, b_color))
