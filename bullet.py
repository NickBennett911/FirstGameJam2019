import pygame


class Bullet:
    def __init__(self, position, code, dir=1):
        self.pos = position.copy()
        self.dir = dir
        self.speed_y = 300 * 2
        self.speed_x = 100 * 2
        self.rad = 6
        self.bullet_timer = 1


        #for when you fight boss
        self.code_good = code

    def update(self, dt):

        if self.code_good == True:
            #print("es bueno amigo")
            #self.speed_y = 300 * 2
            self.speed_x = 10 * 2

        if self.dir == 2:
            self.pos[1] -= self.speed_y * dt
        elif self.dir == 1:
            self.pos[0] += -self.speed_x * dt
            self.pos[1] -= self.speed_y * dt
        elif self.dir == 3:
            self.pos[0] += self.speed_x * dt
            self.pos[1] -= self.speed_y * dt
        elif self.dir == -2:
            self.pos[1] += self.speed_y * dt
        elif self.dir == -1:
            self.pos[0] -= -self.speed_x * dt
            self.pos[1] += self.speed_y * dt
        elif self.dir == -3:
            self.pos[0] -= self.speed_x * dt
            self.pos[1] += self.speed_y * dt

    def draw(self, win):
        pygame.draw.circle(win, (0, 255, 0), (int(self.pos[0]), int(self.pos[1])), self.rad)
