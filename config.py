import pygame
import math

win_width = 800
win_height = 600
pygame.init()
win = pygame.display.set_mode((win_width, win_height))

TheEnd_dict = {"0": "t", "1": "h", "2": "e", "3": "e", "4": "n", "5": "d"}
#TheEnd_dict = dict(l1 = "t", l2 = "h", l3 = "e", l4 = "e", l5 = "n", l6 = "d")

# Player Sprite
SHIP = pygame.image.load("Sprites/spritesheetSpaceship.png")
img_w = SHIP.get_width()
img_h = SHIP.get_height()
SHIP = pygame.transform.scale(SHIP, (img_w, img_h)).convert()
SHIP = pygame.transform.rotate(SHIP, math.pi / 2)
SHIP.set_colorkey((0, 0, 0))
ship_directions = {"frameheight": 100, "framewidth": 65}

# Enemy Sprite
ENEMY = pygame.image.load("Sprites/shipsheetparts.png")
img_w = ENEMY.get_width()
img_h = ENEMY.get_height()
ENEMY = pygame.transform.scale(ENEMY, (img_w, img_h)).convert()
ENEMY.set_colorkey((255, 255, 255))
enemy_directions = {"left": 1, "right": 3, "up": 0, "down": 2, "frameheight": 64, "framewidth": 64, "frames_wide": 8,
                    "x_offset": 15, "y_offset": 5}

# Boss Sprite
BOSS = pygame.image.load("Sprites/PossibleBoss1.png")
img_w = BOSS.get_width()
img_h = BOSS.get_height()
BOSS = pygame.transform.scale(BOSS, (img_w, img_h)).convert()
BOSS.set_colorkey((255, 0, 255))
BOSS.set_alpha(255)
boss_directions = {"left": 1, "right": 3, "up": 0, "down": 2, "frameheight": 64, "framewidth": 64, "frames_wide": 8,
                   "x_offset": 15, "y_offset": 5}

# Terminal Image
TERM = pygame.image.load("Sprites/futuristicScreen.jpg")
img_w = TERM.get_width()
img_h = TERM.get_height()
width_scalar = .94
height_scalar = 1.25
img_w = int(img_w * width_scalar)
img_h = int(img_h * height_scalar)
TERM = pygame.transform.scale(TERM, (img_w, img_h))

BULLET = pygame.image.load("Sprites/orange.png")

ORB = pygame.image.load("Sprites/electric_orb.png")

# dictionary of the keys
Keys_info = {"97": 'a', "98": 'b', "99": 'c', "100": 'd', "101": 'e', "102": 'f', "103": 'g', "104": 'h', "105": 'i',
             "106": 'j', "107": 'k', "108": 'l', "109": 'm', "110": 'n', "111": 'o', "112": 'p', "113": 'q', "114": 'r',
             "115": 's', "116": 't', "117": 'u', "118": 'v', "119": 'w', "120": 'x', "121": 'y', "122": 'z', "32": " ","13":''}
