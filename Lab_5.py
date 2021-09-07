import math

import pygame as pg

WIDTH = 800
HEIGHT = 800
DISPLAY = (WIDTH, HEIGHT)

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (174, 174, 174)
DARK_GRAY = (140, 141, 147)
DARKER_GRAY = (124, 129, 135)
PINK = (254, 182, 255)
LIGHT_BLUE = (21, 71, 130)
BLUE = (0, 73, 181)
RED = (195, 7, 25)
YELLOW = (223, 180, 45)
GREEN = (0, 135, 84)
TEAL = (254, 216, 151)

pg.init()

screen = pg.display.set_mode(DISPLAY)
pg.display.set_caption("PYGAME")
clock = pg.time.Clock()

rect = pg.Rect(100, 100, 100, 100)
rect_selected = False

font = pg.font.Font(None, 14)

# Body
screen1 = pg.Surface((200, 200))
body = pg.Rect(150, 125, 300, 220)
place_buttons = pg.Rect(450, 345, 100, 50)
place_buttons1 = pg.Rect(10, 10, 10, 10)

screen.fill(WHITE)
pg.draw.rect(screen, GRAY, rect=body)
pg.draw.circle(screen, GRAY, center=(150, 250), radius=125)
pg.draw.circle(screen, DARKER_GRAY, center=(150, 250), radius=75, width=1)
pg.draw.circle(screen, GRAY, center=(450, 250), radius=125)
pg.draw.circle(screen, DARK_GRAY, center=(450, 250), radius=100)

screen1.fill(BLUE)
screen1.set_colorkey(GREEN)
r = pg.draw.rect(screen1, BLACK, place_buttons, border_radius=50)
screen.blit(screen1, place_buttons1)


active = True
while active:
    c_height, c_width = 100, 100
    for event in pg.event.get():
        if event.type == pg.QUIT:
            active = False




    # pg.display.update()
    pg.display.flip()
    clock.tick(60)
pg.quit()
