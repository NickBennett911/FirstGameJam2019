import pygame
import math
import random
from config import *


class Enemy:
    def __init__(self, x, y, letter=None):

        self.mPos = [x, y]
        self.mSin_width = random.randint(30, 75)
        self.mid_x = x
        self.driftx = random.randint(-2, 2)/10
        self.drifty = random.randint(-2, 2)/10
        self.offsetx = 0
        self.offsety = 0
        self.Speed = 0.1
        self.mRate = 100
        self.mEnemy_rad = 18
        self.mFrame_delay = 0.1
        self.Exploding = False
        self.Exploding_frameh = 105
        self.pars_y = 323
        self.mLetter = letter
        self.mAttack_type = random.randint(0,1)
        self.mBullet_list = []
        self.mBullet_cooldown = 1.5
        self.Spwn_bullets = False

    def update(self, dt):
        self.mBullet_cooldown -= dt
        if not self.Exploding:
            self.mPos[1] += self.mRate * dt
            self.mPos[0] = math.sin(self.mPos[1] * .05) * self.mSin_width + self.mid_x
            if self.mBullet_cooldown < 0:
                self.mBullet_cooldown = 1.5
                self.Spwn_bullets = True
            else:
                self.Spwn_bullets = False
        elif self.Exploding:
            self.mFrame_delay -= dt
            self.offsetx += self.driftx
            self.offsety += self.drifty
            self.Spwn_bullets = False
            if self.mFrame_delay < 0:
                self.pars_y -= self.Exploding_frameh
                self.mFrame_delay = 0.1

        return self.Spwn_bullets

    def attack(self):
        x_rate = 75
        y_rate = 200

        if self.mAttack_type == 0:
            bullet1 = [self.mPos[0] - 7, self.mPos[1], [0, y_rate*1.5]]
            bullet2 = [self.mPos[0] + 7, self.mPos[1], [0, y_rate*1.5]]
            bullet_group = [bullet1, bullet2]
        if self.mAttack_type == 1:
            bullet1 = [self.mPos[0] - 5, self.mPos[1], [x_rate, y_rate]]
            bullet2 = [self.mPos[0] + 5, self.mPos[1], [-x_rate, y_rate]]
            bullet3 = [self.mPos[0], self.mPos[1], [0, y_rate*1.1]]
            bullet_group = [bullet1, bullet2, bullet3]
        self.mBullet_cooldown = 1.5

        return bullet_group

    def explode(self):
        # self.mSource_rect = pygame.Rect()
        self.Exploding = True

    def draw(self, win, font):
        if not self.Exploding:
            win.blit(ENEMY, (int(self.mPos[0] - (35/2)), int(self.mPos[1]) - (40/2)), (5, 10, 35, 40))
        else:
            if self.mLetter != None:
                txt = font.render(str(self.mLetter), True, (0, 255, 0))
                txt_w = txt.get_width()
                txt_h = txt.get_height()

                win.blit(txt, (int(self.mPos[0] - (txt_w/2) + self.offsetx), int(self.mPos[1]) - (txt_h/2) + self.offsety))
            win.blit(SHIP, (int(self.mPos[0] - (85/2)), int(self.mPos[1]) - (self.Exploding_frameh/2)), (310, self.pars_y, 85, self.Exploding_frameh))
        # pygame.draw.circle(win, (255, 0, 0), (int(self.mPos[0]), int(self.mPos[1]) - 5), self.mEnemy_rad, 1)
