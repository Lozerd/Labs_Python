import sys

import pygame

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 71, 179)

GRAY = (174, 174, 174)
D_PAD_GRAY = (81, 82, 86)
D_PAD_RECT_GRAY = (90, 91, 96)
LIGHT_GRAY = (187, 188, 192)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test app")

body = pygame.Rect(250, HEIGHT / 2 - 100, 250, 170)
d_pad = pygame.Rect(190, HEIGHT / 2 - 55, 110, 110)

d_pad_circle = pygame.Rect(150, HEIGHT / 2 - 100, 200, 200)
d_pad_inner_circle = pygame.Rect(200, 285, 90, 30)
d_pad_inner_circle_invert = pygame.Rect(d_pad_inner_circle.centerx - 15, d_pad_inner_circle.centery - 45, 30, 90)

buttons_circle = pygame.Rect(WIDTH - 400, HEIGHT / 2 - 100, 200, 200)

rotation = 45
surface = pygame.Surface((50, 30))

surface.set_colorkey(WHITE)
surface.fill(LIGHT_GRAY)

btn1_field = surface.get_rect()
btn1_field.center = (500, 290)

btn2_field = surface.get_rect()
btn2_field.center = (540, 310)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    mouse_p = pygame.mouse.get_pos()
    screen.blit(
        pygame.font.SysFont("Times New Roman", 30).render(f"X: {mouse_p[0]}; Y: {mouse_p[1]}", False, (0, 0, 0)),
        (10, 10))
    # == JoyStick ==
    pygame.draw.ellipse(screen, GRAY, d_pad_circle)
    pygame.draw.circle(screen, BLACK, radius=100, center=(d_pad_circle.centerx, d_pad_circle.centery),
                       draw_top_left=True, draw_bottom_left=True, draw_bottom_right=True, width=1)
    pygame.draw.ellipse(screen, GRAY, buttons_circle)
    pygame.draw.circle(screen, BLACK, radius=100, center=(buttons_circle.centerx, buttons_circle.centery),
                       draw_bottom_right=True, draw_top_right=True, draw_bottom_left=True, width=1)
    pygame.draw.rect(screen, GRAY, body)
    pygame.draw.line(screen, BLACK, body.topleft, body.topright, width=1)
    pygame.draw.ellipse(screen, D_PAD_GRAY, d_pad, width=2)
    pygame.draw.circle(screen, BLACK, center=buttons_circle.center, radius=80, width=2)

    # d_pad
    d_w_1 = d_pad_inner_circle_invert
    d_w_2 = d_pad_inner_circle
    pygame.draw.rect(screen, D_PAD_RECT_GRAY, d_pad_inner_circle_invert, border_radius=5)
    pygame.draw.rect(screen, BLACK, pygame.Rect(d_w_1.x, d_w_1.y, d_w_1.w, d_w_1.h / 2), border_radius=5, width=3)
    pygame.draw.rect(screen, BLACK, pygame.Rect(d_w_1.x, d_w_1.y + 45, d_w_1.w, d_w_1.h / 2), border_radius=5, width=3)

    pygame.draw.polygon(screen, D_PAD_GRAY, points=[(d_pad.centerx - 10, d_pad.centery - 20),  # TOP
                                                    (d_pad.centerx, d_pad.centery - 40),
                                                    (d_pad.centerx + 10, d_pad.centery - 20)])
    pygame.draw.polygon(screen, D_PAD_GRAY, points=[(d_pad.centerx + 10, d_pad.centery + 20),  # Bottom
                                                    (d_pad.centerx, d_pad.centery + 40),
                                                    (d_pad.centerx - 10, d_pad.centery + 20)])

    pygame.draw.rect(screen, D_PAD_RECT_GRAY, d_pad_inner_circle, border_radius=5)

    pygame.draw.rect(screen, BLACK, pygame.Rect(d_w_2.x, d_w_2.y, d_w_2.w / 2 - 5, d_w_2.h),
                     border_radius=5, width=3)
    pygame.draw.rect(screen, BLACK, pygame.Rect(d_w_2.x + 50, d_w_2.y, d_w_2.w / 2 - 5, d_w_2.h),
                     border_radius=5, width=3)

    pygame.draw.rect(screen, D_PAD_RECT_GRAY,
                     pygame.Rect(d_w_2.centerx - 13.5, d_w_2.centery - 15, d_w_2.w / 2 - 15, d_w_2.h),
                     border_radius=5)
    pygame.draw.polygon(screen, D_PAD_GRAY, points=[(d_pad.centerx + 20, d_pad.centery - 10),  # Right
                                                    (d_pad.centerx + 40, d_pad.centery),
                                                    (d_pad.centerx + 20, d_pad.centery + 10)])
    pygame.draw.polygon(screen, D_PAD_GRAY, points=[(d_pad.centerx - 20, d_pad.centery + 10),  # Left
                                                    (d_pad.centerx - 40, d_pad.centery),
                                                    (d_pad.centerx - 20, d_pad.centery - 10)])
    pygame.draw.circle(screen, (127, 128, 133), center=(d_w_2.centerx, d_w_2.centery), radius=10)

    # Buttons
    center1 = btn1_field.center
    center2 = btn2_field.center

    surface1 = pygame.transform.rotate(surface, 45)
    surface2 = pygame.transform.rotate(surface, 45)

    btn1_field = surface1.get_rect()
    btn1_field.center = center1

    btn2_field = surface2.get_rect()
    btn2_field.center = center2

    screen.blit(surface1, btn1_field)
    screen.blit(surface2, btn2_field)
    # 525, 260

    pygame.draw.circle(screen, LIGHT_GRAY, center=(
        btn1_field.topright[0] - 12,
        btn1_field.topright[1] + 12
    ), radius=15)

    pygame.draw.circle(screen, LIGHT_GRAY, center=(
        btn1_field.bottomleft[0] + 12,
        btn1_field.bottomleft[1] - 12
    ), radius=15)

    pygame.draw.circle(screen, LIGHT_GRAY, center=(
        btn2_field.topright[0] - 12,
        btn2_field.topright[1] + 12
    ), radius=15)

    pygame.draw.circle(screen, LIGHT_GRAY, center=(
        btn2_field.bottomleft[0] + 12,
        btn2_field.bottomleft[1] - 12
    ), radius=15)

    # The buttons
    pygame.draw.circle(screen, BLUE, center=(
        btn1_field.topright[0] - 12,
        btn1_field.topright[1] + 12
    ), radius=10)

    pygame.draw.rect(screen, BLACK, btn1_field, width=1)
    pygame.draw.line(screen, RED, btn1_field.center, btn1_field.center, width=3)
    pygame.draw.rect(screen, BLACK, btn2_field, width=1)
    pygame.draw.line(screen, RED, btn2_field.center, btn2_field.center, width=3)

    pygame.display.flip()
    clock.tick(60)
