import pygame
from setup import *

class Player(pygame.sprite.Sprite):

    def __init__(self, current_scene, image, location, controls):
        super().__init__()

        self.current_scene = current_scene
        self.previous_scene = None

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = location
        self.controls = controls

        self.vx = 0
        self.vy = 0

    def process_input(self, events, pressed_keys):
        self.vx, self.vy = 0, 0

        if pressed_keys[self.controls['up']]:
            self.vy = -5
        elif pressed_keys[self.controls['down']]:
            self.vy = 5

        if pressed_keys[self.controls['left']]:
            self.vx = -5
        elif pressed_keys[self.controls['right']]:
            self.vx = 5

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
