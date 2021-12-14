import pygame
from config import *
from bullet import *


class Player:
    def __init__(self, screen_dems, code, img=None):

        # fancy code stuff
        self.code_good = False

        # screen dimensions
        self.screenwidth = screen_dems[0]
        self.screenheight = screen_dems[1]

        # player stuff
        self.player_pos = [self.screenwidth//2, 500]
        self.speed = 200
        self.player_hitbox = ship_directions["framewidth"]//2
        self.bullet_list = []   # bullet class objects
        self.frame_row = 6
        self.frame_column = 0
        self.timer = .25
        self.x = 0
        self.max_health = 100
        self.health = 100
        self.attack = 1
        self.pars_y = 630
        self.explosion_frameh = 105
        self.exploding = False
        self.frame_delay = 0.1
        self.distance = 400

        # stuff for the image
        self.img = img
        self.img_w = ship_directions["frameheight"]
        self.img_h = ship_directions["frameheight"]

    def update(self, dt, code):
        self.dt = dt
        self.code_good = code
        #print(str(self.code_good) + " player class")
        if self.exploding:
            self.frame_delay -= dt
            if self.frame_delay < 0:
                self.frame_delay = 0.1
                self.pars_y -= self.explosion_frameh

        # Bullet Update
        for b in self.bullet_list:
            b.update(dt)
            bx = b.pos[0]
            by = b.pos[1]
            bullet_vec = [self.player_pos[0] - bx, self.player_pos[1] - by]
            distance = (bullet_vec[0] **2 + bullet_vec[1] **2) ** (1/2)

            if b.pos[1] < 0:
                self.bullet_list.remove(b)
            elif distance >= self.distance:
                self.bullet_list.remove(b)
        print(self.player_pos)
        if self.player_pos[1] < 440:
            self.player_pos[1] = 440


        # keep on screen code
        if self.player_pos[0] < 0 + self.player_hitbox:
            self.player_pos[0] = 0 + self.player_hitbox
        if self.player_pos[0] > self.screenwidth - self.player_hitbox:
            self.player_pos[0] = self.screenwidth - self.player_hitbox
        if self.player_pos[1] < 0 + (self.player_hitbox * 2):
            self.player_pos[1] = 0 + (self.player_hitbox * 2)
        if self.player_pos[1] > self.screenheight - (self.player_hitbox *  2):
            self.player_pos[1] = self.screenheight - (self.player_hitbox * 2)


    def input(self, evt, keys):
        # Moving player_ship
        if not self.exploding:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.player_pos[0] -= self.speed * self.dt
                self.frame_row = 4
                self.frame_column = 1

            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.player_pos[0] += self.speed * self.dt
                self.frame_row = 6
                self.frame_column = 1
            else:
                self.frame_row = 6
                self.frame_column = 0

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.player_pos[1] -= self.speed * self.dt
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.player_pos[1] += self.speed * self.dt

            # make bullet list

            if keys[pygame.K_SPACE]:
                self.x += self.dt
                #print(self.code_good)
                if self.x >= self.timer:
                    self.bullet_list.append(Bullet(self.player_pos, self.code_good,1))
                    self.bullet_list.append(Bullet(self.player_pos, self.code_good,2))
                    self.bullet_list.append(Bullet(self.player_pos, self.code_good,3))
                    self.x = 0

    def draw(self, surf):
        # temporary player
        #pygame.draw.circle(surf, (0, 255, 0), (int(self.player_pos[0]), int(self.player_pos[1])), self.player_hitbox, 1)

        rect = (self.img_w * self.frame_column, self.img_h * self.frame_row, self.img_w, self.img_h)

        for i in self.bullet_list:
            i.draw(win)

        if not self.exploding:
            surf.blit(self.img, (int(self.player_pos[0] - (self.img_w/2 + 15)), int(self.player_pos[1] - (self.img_h/2 + 15))), rect)
        if self.exploding:
            print("explosion animation for player")
            surf.blit(self.img, (int(self.player_pos[0] - (self.img_w/2)), int(self.player_pos[1] - (self.img_h/2))),
                      (310, self.pars_y, 85, self.explosion_frameh))
