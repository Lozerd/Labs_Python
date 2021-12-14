import random
import sys
import pygame

from Game.player import Player
from config import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
player.rect.x, player.rect.y = 0, WIDTH / 3
entity_list = pygame.sprite.Group()
entity_list.add(player)
active = True

background = pygame.image.load(random.choice(BACKGROUNDS))
background_rect = screen.get_rect()

while active:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            sys.exit()

        screen.blit(background, background_rect)
        player.move(event)
        player.update()
        entity_list.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
