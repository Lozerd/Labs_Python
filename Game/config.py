import os

import pygame.time

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# SCREEN
WIDTH, HEIGHT = 800, 600


# CONFIGS
IMAGE_DIR = os.path.join('src', 'images')
FPS = 120
BACKGROUNDS = [
    os.path.join(IMAGE_DIR, 'bg1.jpg'),
    os.path.join(IMAGE_DIR, 'bg2.jpg'),
]