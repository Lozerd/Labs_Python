import pygame as py

# define constants
WIDTH = 500
HEIGHT = 500
FPS = 30

# define colors
BLACK = (0 , 0 , 0)
GREEN = (0 , 255 , 0)

# initialize pygame and create screen
py.init()
screen = py.display.set_mode((WIDTH , HEIGHT))
# for setting FPS
clock = py.time.Clock()

rot = 45
rot_speed = 0


image_orig = py.Surface((100 , 50))
image_orig.set_colorkey(BLACK)
image_orig.fill(GREEN)
rect = image_orig.get_rect()
rect.center = (WIDTH // 2 , HEIGHT // 2)

running = True
while running:
    # set FPS
    clock.tick(FPS)
    # clear the screen every time before drawing new objects
    screen.fill(BLACK)
    # check for the exit
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # making a copy of the old center of the rectangle
    old_center = rect.center
    # rotating the orignal image
    print(1, rect.center, old_center)

    new_image = py.transform.rotate(image_orig , 45)
    rect = new_image.get_rect()
    # set the rotated rectangle to the old center
    print(rect.center, old_center)
    rect.center = old_center
    # drawing the rotated rectangle to the screen
    screen.blit(new_image , rect)
    # flipping the display after drawing everything
    py.display.flip()

py.quit()