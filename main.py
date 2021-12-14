from map import *
from boss import *
from terminal import *
import pygame
import random

# Pygame startup
clock = pygame.time.Clock()
done = False

start_screen = True
boss_phase = False
add_phase = False
terminal_phase = False
code_good = False
game_over = False

my_map = Map(code_good)
boss = Boss(win_width/2, -200, my_map)
term = Terminal()
end_screen = pygame.image.load("Sprites/game_jam_end.png")
start_img = pygame.image.load("Sprites/game_jam_cover.png")
start_end_font = pygame.font.Font("Sprites/Fonts/venus rising rg.ttf", 24)
add_font = pygame.font.Font("Sprites/Fonts/venus rising rg.ttf", 12)


max_stars = 200
stars = []
for i in range(max_stars):
    x, y, rgb, twinkle = randint(0, 800), randint(0, 600), randint(75, 200), randint(1, 100)
    rad, spd = randint(2, 5), randint(100, 150)
    if twinkle >= 90:
        star_twinkle = True
    else:
        star_twinkle = False
    star = [x, y, rad, spd, rgb, star_twinkle]
    stars.append(star)

while not done:
    # Update
    dt = clock.tick() / 1000.0
    if add_phase:
        my_map.update(dt, code_good)
        my_map.Player.distance = 400
    elif boss_phase:
        boss.update(dt)
        my_map.Player.distance = 1000
    elif terminal_phase:
        code_good = term.update(dt)
        print(str(code_good) + " main")
    for star in stars:
        star[1] += star[3] * dt
        if star[1] > star[2] + 600:
            star[1] = -star[2]
    if code_good:
        my_map.Player.attack = 10
    if boss.mHealth <= 0:
        boss.mHealth = 0
        for explostion in boss.mExplosions:
            if explostion[3] < -200:
                game_over = True
    elif my_map.Player.health <= 0:
        my_map.Player.exploding = True
        if my_map.Player.pars_y <= 8:
            my_map.Player.pars_y = 630
            boss.reset()
            my_map.reset()
            my_map.Player.health = 100
            my_map.Player.exploding = False
            boss_phase = False
            add_phase = True



    # Input
    evt = pygame.event.poll()
    keys = pygame.key.get_pressed()
    if add_phase:
        list2 = my_map.input(evt, keys)
        boss_phase = list2[0]
        add_phase = list2[1]
        if not add_phase:
            my_map.reset()
    elif boss_phase:
        list = boss.input(evt, keys)
        boss_phase = list[0]
        add_phase = list[1]
        if not boss_phase:
            boss.reset()

    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True
        if terminal_phase:
            term.input(evt, keys)
        if evt.key == pygame.K_p and boss_phase is not True:
            terminal_phase = True
            add_phase = False
        if terminal_phase:
            if evt.key == pygame.K_TAB:
                print("it quit")
                terminal_phase = False
                add_phase = True
        if game_over and (evt.key == pygame.K_RETURN or evt.key == pygame.K_KP_ENTER):
            done = True
        if start_screen and (evt.key == pygame.K_RETURN or evt.key == pygame.K_KP_ENTER):
            start_screen = False
            add_phase = True


    # Drawing
    win.fill((0, 0, 0))
    if game_over:
        win.blit(end_screen, (-75, -100, win_width, win_height))
        win.blit(start_end_font.render("Press Enter to Close.", True, (39, 135, 104)), (175, 500))

    elif start_screen:
        win.blit(start_img, (-100, -150, win_width, win_height))
        win.blit(start_end_font.render("Press Enter to Begin!", True, (39, 135, 104)), (175, 450))
        win.blit(add_font.render("Arrow Keys or WSAD to move", True, (39, 135, 104)), (20, 575))
        win.blit(add_font.render("Space to fire weapon", True, (39, 135, 104)), (350, 575))
        win.blit(add_font.render("P to open terminal", True, (39, 135, 104)), (600, 575))

    elif not game_over:
        for star in stars:
            x = star[0]
            y = star[1]
            rgb = star[4]
            st_twinkle = star[5]
            if st_twinkle:
                rgb = randint(50, 255)
            pygame.draw.circle(win, (rgb, rgb, rgb), (int(x), int(y)), star[2])

        pcent = my_map.Player.health / my_map.Player.max_health
        if my_map.Player.health > 0:
            color = my_map.hp_bar.get_at((int((my_map.hp_bar.get_width() - 1) * pcent), 0))
        width = 150 * pcent
        outer_width = 153
        pygame.draw.rect(win, (255, 255, 255), (618, 18, outer_width, 15), 2)
        pygame.draw.rect(win, color, (620, 20, width, 12))

        if add_phase:
            my_map.draw(win)
        elif boss_phase:
            boss.draw(win)
        elif terminal_phase:
            term.draw(win)
    pygame.display.flip()

pygame.quit()
