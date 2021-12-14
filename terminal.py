import pygame
from config import *


class Terminal:
    def __init__(self):
        self.image = TERM
        self.font = pygame.font.SysFont("Vixar ASCI", 48)
        self.term_string = "Code: "
        self.keys = Keys_info
        self.timer = 1
        self.x = 0
        self.not_available = False      # checking for wrong key press thing
        self.solutions = ["Code: theend","Code: the end"]
        self.code_good = False
        self.locked_input = ''
        self.test_code = False

    def update(self, dt):

        if self.not_available:
            self.x += dt
            print(self.x)
            if self.x > self.timer:
                print("reset")
                self.x = 0
                self.term_string = "Code: "
                self.not_available = False

        if self.test_code == True:
            for s in self.solutions:
                if s == self.locked_input:
                    self.code_good = True
                    self.term_string = "Code: Accepted"
                    self.not_available = False
                    #print(self.code_good)
                else:
                    self.term_string = "Code: Not Accepted"
                    self.not_available = True
                    self.test_code = False
        return self.code_good


    def input(self, evt, keys):
        if evt.type == pygame.KEYDOWN:
            x = evt.key
            print(x)
            if str(x) in self.keys:
                self.term_string += self.keys[str(x)]
            else:
                x = "Code: Not Available"
                self.term_string = x
                self.not_available = True
            if evt.key == pygame.K_RETURN:
                #self.not_available = False
                self.test_code = True
                self.locked_input = self.term_string


    def draw(self, win):
        win.blit(self.image, (0, 0, win_width, win_height))
        win.blit(self.font.render(self.term_string, True, (255, 255, 255)), (220, 170))
        win.blit(self.font.render("Tab to Exit Terminal", True, (255, 255, 255)), (220, 252))
        win.blit(self.font.render("Enter to Test Code", True, (255, 255, 255)), (220, 300))
        win.blit(self.font.render("Backspace to Clear Code", True, (255, 255, 255)), (220, 348))
