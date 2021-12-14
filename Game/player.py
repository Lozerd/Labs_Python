import os
import pygame.sprite
from Game.config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args)
        self.direction = []
        self.speed = 20

        if kwargs.get('image', None):
            self.image = pygame.image.load(os.path.join(IMAGE_DIR, kwargs.get('image')))
        else:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_DIR, 'player.jpg')),
                                                (int(WIDTH / 7), int(HEIGHT / 7)))
        self.rect = self.image.get_rect()

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.direction.append("left")
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.direction.append("right")
            if event.key == pygame.K_UP or event.key == ord('s'):
                self.direction.append("up")
            if event.key == pygame.K_DOWN or event.key == ord('w'):
                self.direction.append("down")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.direction.pop(self.direction.index('left'))
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.direction.pop(self.direction.index("right"))
            if event.key == pygame.K_UP or event.key == ord('s'):
                self.direction.pop(self.direction.index("up"))
            if event.key == pygame.K_DOWN or event.key == ord('w'):
                self.direction.pop(self.direction.index("down"))

    def update(self):
        if "left" in self.direction:
            self.rect.x -= self.speed
        if "right" in self.direction:
            self.rect.x += self.speed
        if "up" in self.direction:
            self.rect.y += self.speed
        if "down" in self.direction:
            self.rect.y -= self.speed
        self.collide()

    def collide(self):
        border = ((WIDTH - (self.rect.width / 2)), (HEIGHT - (self.rect.height / 2)))
        if self.rect.x > border[0]:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = border[0]
        if self.rect.y > border[1]:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = border[1]
