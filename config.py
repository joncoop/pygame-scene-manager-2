import pygame

# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Name of Game"
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
TITLE_FONT = None
DEFAULT_FONT = None

# Controls
p1_controls = {'up': pygame.K_w,
               'left': pygame.K_a,
               'down': pygame.K_s,
               'right': pygame.K_d}