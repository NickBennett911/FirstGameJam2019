import pygame
from config import *
from Player import *
import random


class Boss:
    def __init__(self, x, y, map):
        self.position = [x, y]
        self.Map = map
        self.mHealth = 1000
        self.mBoss_image = pygame.image.load("Sprites/PossibleBoss1.png")
        self.mBoss_w = self.mBoss_image.get_width()
        self.mBoss_h = self.mBoss_image.get_height()
        self.speed = 100
        self.mBullet_list = []
        self.mBoss_timer = 10
        self.mBoss_phase = True
        self.mAdd_phase = False
        self.mBullet_cooldown = 1.5
        self.mBullet2_cooldown = 2
        self.enemy_box = pygame.Rect(self.position[0] - (self.mBoss_w / 2), self.position[1] - (self.mBoss_h / 2), self.mBoss_w, self.mBoss_h)

        self.pars_y = 323
        self.explostionh = 105
        self.delay0 = random.randint(1, 4) / 10
        self.delay1 =random.randint(1, 4) / 10
        self.delay2 =random.randint(1, 4) / 10
        self.delay3 =random.randint(1, 4) / 10
        self.delay4 =random.randint(1, 4) / 10
        self.delay5 =random.randint(1, 4) / 10
        self.delay6 =random.randint(1, 4) / 10
        self.delay7 =random.randint(1, 4) / 10
        self.delay8 =random.randint(1, 4) / 10
        self.delay9 =random.randint(1, 4) / 10
        self.delay10 =random.randint(1, 4) / 10
        self.delay11 =random.randint(1, 4) / 10
        self.mExplosions = [[self.position[0] + 25, self.position[1] - 25, self.delay0 , self.pars_y, self.delay0 ],
                            [self.position[0] + 75, self.position[1] + 25, self.delay1 , self.pars_y, self.delay1 ],
                            [self.position[0] + 40, self.position[1] - 30, self.delay2 , self.pars_y, self.delay2 ],
                            [self.position[0] + 10, self.position[1] + 40, self.delay3 , self.pars_y, self.delay3 ],
                            [self.position[0] - 45, self.position[1] + 80, self.delay4 , self.pars_y, self.delay4 ],
                            [self.position[0] - 70, self.position[1] - 50, self.delay5 , self.pars_y, self.delay5 ],
                            [self.position[0] - 50, self.position[1] + 50, self.delay6 , self.pars_y, self.delay6 ],
                            [self.position[0] - 70, self.position[1] + 60, self.delay7 , self.pars_y, self.delay7 ],
                            [self.position[0] - 20, self.position[1] - 70, self.delay8 , self.pars_y, self.delay8 ],
                            [self.position[0] + 35, self.position[1] + 50, self.delay9 , self.pars_y, self.delay9 ],
                            [self.position[0] + 40, self.position[1] + 80, self.delay10, self.pars_y, self.delay10],
                            [self.position[0] - 10, self.position[1] + 90, self.delay11, self.pars_y, self.delay11]]

        # text box / timer stuff
        self.print1 = False
        self.font = pygame.font.SysFont("Bahnschrift", 16)
        self.print1_text = "Hah! I'm gonna get you fool, ya fool!"
        self.print2 = False
        self.print2_text = "Figure out the code to leave fool, ya fool!"
        self.x = 0
        self.text_timer = 1.5
        self.text_box = pygame.Surface((315, 50))

    def update(self, dt):
        self.mBoss_timer -= dt
        self.Map.Player.update(dt, self.Map.code_good)

        if self.print1:
            # print("it works")
            self.x += dt
            if self.x > self.text_timer:
                self.print1 = False
                self.x = 0
        if self.print2:
            # print("it works")
            self.x += dt
            if self.x > self.text_timer:
                self.print2 = False
                self.x = 0

        if self.mBoss_timer > 0:        # this is where the boss stops
            if self.position[1] < 75:
                self.position[1] += self.speed * dt
                self.print1 = True

        if self.mBoss_timer <= 0:
            self.position[1] -= self.speed * dt
            self.print2 = True

        self.mBullet_cooldown -= dt
        if self.position[1] >= -300:
            if self.mBullet_cooldown < 0:
                self.attack1(self.position[0] - 50, self.position[1])
                self.attack1(self.position[0] + 50, self.position[1])

        self.mBullet2_cooldown -= dt
        if self.position[1] >= -300:
            if self.mBullet2_cooldown < 0:
                self.attack2(self.position[0], self.position[1])


        if self.mHealth <= 0:
            for explosion in self.mExplosions:
                explosion[2] -= dt
                if explosion[2] < 0:
                    explosion[3] -= self.explostionh
                    explosion[2] = explosion[4]


        length = len(self.mBullet_list)-1
        if length >= 0:
            while length >= 0:
            #for group in self.mBullet_list:
                bullets = self.mBullet_list[length]
                for j in range(len(bullets)):
                #for bullet in group:
                    bullet = self.mBullet_list[length][j]
                    bullet[1] += bullet[3] * dt
                    bullet[0] += bullet[2] * dt
                    if bullet[1] > win_height + 10:
                        self.mBullet_list.remove(bullets)
                        break
                    bx = bullet[0]
                    by = bullet[1]
                    px = self.Map.Player.player_pos[0]
                    py = self.Map.Player.player_pos[1]
                    a = px - bx
                    b = py - by
                    distance = (a * a + b * b) ** 0.5
                    if distance < self.Map.Player.player_hitbox:
                        if bullet[4] == "attack1":
                            self.Map.Player.health -= 5
                        elif bullet[4] == "attack2":
                            self.Map.Player.health -= 10
                        bullets.remove(bullet)
                        break
                length -= 1

        print(len(self.mBullet_list))

        for i in self.Map.Player.bullet_list:
            bul_rect = pygame.Rect(i.pos[0] - 3, i.pos[1] + 3, 6, 6)
            collide = bul_rect.colliderect(self.enemy_box)
            if collide:
                self.mHealth -= self.Map.Player.attack
                self.Map.Player.bullet_list.remove(i)

    def explosions(self, win):
        self.mExplosions[0][1] = self.position[1]-25
        self.mExplosions[1][1] = self.position[1]+25
        self.mExplosions[2][1] = self.position[1]-30
        self.mExplosions[3][1] = self.position[1]+40
        self.mExplosions[4][1] = self.position[1]+80
        self.mExplosions[5][1] = self.position[1]-50
        self.mExplosions[6][1] = self.position[1] - 50
        self.mExplosions[7][1] = self.position[1] - 60
        self.mExplosions[8][1] = self.position[1] - 70
        self.mExplosions[9][1] = self.position[1] + 50
        self.mExplosions[10][1] = self.position[1] + 80
        self.mExplosions[11][1] = self.position[1] + 90


        for explosion in self.mExplosions:
            print(explosion[0], explosion[1], "x, y for explosion")
            win.blit(SHIP, (explosion[0], explosion[1]), (310, explosion[3], 75, self.explostionh))

    def attack1(self, spwn_x, spwn_y):
        x_rate = random.randint(40, 65)
        y_rate = random.randint(175, 200)
        bullet1 = [spwn_x, spwn_y, 0, y_rate, "attack1"]
        bullet2 = [spwn_x, spwn_y, x_rate, y_rate, "attack1"]
        bullet3 = [spwn_x, spwn_y, x_rate*2, y_rate, "attack1"]
        bullet4 = [spwn_x, spwn_y, -x_rate, y_rate, "attack1"]
        bullet5 = [spwn_x, spwn_y, -x_rate*2, y_rate, "attack1"]
        bullet_group = [bullet1, bullet2, bullet3, bullet4, bullet5]
        self.mBullet_list.append(bullet_group)
        self.mBullet_cooldown = 1.5

    def attack2(self, spwn_x, spwn_y):
        x_rate = random.randint(40, 60)
        y_rate = random.randint(140, 170)
        bullet1 = [spwn_x, spwn_y, 0, y_rate*1.3, "attack2"]
        bullet2 = [spwn_x, spwn_y, x_rate*2*1.2, y_rate*1.3, "attack2"]
        bullet3 = [spwn_x, spwn_y, -x_rate*2*1.25, y_rate*1.2, "attack2"]
        self.mBullet_list.append([bullet1, bullet2, bullet3])
        self.mBullet2_cooldown = 2

    def input(self, evt, keys):
        self.Map.Player.input(evt, keys)

        if self.mBoss_timer < 0:
            if len(self.mBullet_list) <= 0:
                return False, True

        return self.mBoss_phase, self.mAdd_phase

    def reset(self):
        self.mBullet_list = []
        self.position[1] = -299
        self.mAdd_phase = False
        self.mBoss_phase = True
        self.mBoss_timer = 10
        self.mHealth = 1000

    def draw(self, win):


        self.Map.Player.draw(win)
        for bullet_group in self.mBullet_list:
            if len(bullet_group) > 3:
                for bullet in bullet_group:
                    win.blit(BULLET, (int(bullet[0]-5), int(bullet[1]-5)))
            else:
                for bullet in bullet_group:
                    win.blit(ORB, (int(bullet[0]-10), int(bullet[1]-10)))
        win.blit(self.mBoss_image, (self.position[0] - (self.mBoss_w/2), self.position[1] - (self.mBoss_h/2)))

        pygame.draw.rect(win, (255, 255, 0), (15, 15, 200, 10), 1)
        pygame.draw.rect(win, (255, 255, 0), (15, 15, int(self.mHealth/5), 10))

        if self.print1:
            win.blit(self.text_box, (self.position[0], self.position[1] + 250))
            self.text_box.fill((255, 255, 255))
            self.text_box.blit(self.font.render(self.print1_text, True, (0, 0, 0)), (15, 15))
            # self.chest_screen.blit(self.font.render(str(text[0]), True, (0, 0, 0)),(35, 20))

        if self.print2:
            win.blit(self.text_box, (self.position[0], self.position[1] + 250))
            self.text_box.fill((255, 255, 255))
            self.text_box.blit(self.font.render(self.print2_text, True, (0, 0, 0)), (15, 15))

        #pygame.draw.rect(win, (255, 255, 255), (self.position[0] - (self.mBoss_w / 2), self.position[1] - (self.mBoss_h / 2), self.mBoss_w, self.mBoss_h), 2)

        if self.mHealth <= 0:
            self.explosions(win)
