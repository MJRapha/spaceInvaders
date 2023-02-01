import pygame
#import random
from Player import Player
from Meteor import Meteor
from Explosion import Explosion
from os import path
from TekkiePygameLib import Label

WIN_WIDTH = 500
WIN_HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

img_dir = path.join(path.dirname(__file__), 'img')
explosions_img_dir = path.join(path.dirname(__file__), 'img/Explosions')
meteors_img_dir = path.join(path.dirname(__file__), 'img/meteor images')
sound_dir = path.join(path.dirname(__file__), 'sounds')
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load(path.join(sound_dir, 'through_space.ogg'))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)
user_score = Label(x=240, y=20, text="0", color=WHITE, size=40)
background = pygame.image.load(path.join(img_dir, 'spaceBG.png')).convert()
background = pygame.transform.scale(background, (500, 600))
my_player_img = pygame.image.load(path.join(img_dir, 'spaceship.png')).convert()
my_meteor_img = pygame.image.load(path.join(img_dir, 'meteor.png')).convert()
my_bullet_img = pygame.image.load(path.join(img_dir, 'bullet.png')).convert()

my_player = Player(win, my_player_img, my_bullet_img)

meteor_images = []
meteor_list = ["meteor1.png", "meteor2.png", "meteor3.png", "meteor4.png", "meteor5.png",
               "meteor6.png", "meteor7.png", "meteor8.png", "meteor9.png"]
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(meteors_img_dir, img)))

#player_2 = Player(win, RED, 30, 20)
all_sprites = pygame.sprite.Group()
all_sprites.add(my_player)
#print(list(all_sprites))
meteors = pygame.sprite.Group()
explosion_animation_dict = {'large': [], 'small': []}


def create_meteor():
    #r_color = random.randint(0, 255)
    #g_color = random.randint(0, 255)
    #b_color = random.randint(0, 255)
    meteor = Meteor(win, meteor_images)
    all_sprites.add(meteor)
    meteors.add(meteor)


for i in range(9):
    img_name = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(explosions_img_dir, img_name)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_animation_dict['large'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_animation_dict['small'].append(img_sm)
    create_meteor()

explosion_sounds = []
for sound in ['expl1.wav', 'expl2.wav']:
    explosion_sounds.append(pygame.mixer.Sound(path.join(sound_dir, sound)))


def create_explosion(p_explosion_loc, p_explosion_size):
    my_explosion = Explosion(p_explosion_loc, p_explosion_size, explosion_animation_dict[p_explosion_size],
                             explosion_sounds)
    all_sprites.add(my_explosion)


def show_opening_screen():
    win.blit(background, (0, 0))
    title = Label(x=250, y=200, text="Space Invaders", color=WHITE, size=65)
    credit = Label(x=250, y=500, text="TekkieUni", color=WHITE, size=25)
    game_instructions = Label(x=250, y=400, text="To move use the arrow keys, To fire use space", color=WHITE, size=30)
    start_instructions = Label(x=250, y=350, text="To start click on ENTER", color=WHITE, size=30)
    title.draw(win)
    credit.draw(win)
    game_instructions.draw(win)
    start_instructions.draw(win)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
