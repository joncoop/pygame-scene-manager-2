# Imports
from sprites import *


# Scenes
class Scene:
    def __init__(self):
        self.next_scene = self

    def process_input(self, events, pressed_keys):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def render(self):
        raise NotImplementedError

    def terminate(self):
        self.next_scene = None


class TitleScene(Scene):
    def __init__(self):
        super().__init__()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = PlayScene()
    
    def update(self):
        pass
    
    def render(self):
        screen.fill(BLACK)
        draw_text(screen, TITLE, font_xl, WHITE, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], 'center')


class PlayScene(Scene):
    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):
        self.all_sprites = pygame.sprite.Group()

        self.player1 = Player(self, GFX['platformChar_idle'], [200, 200], p1_controls)

        self.all_sprites.add(self.player1)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = EndScene()

        self.player1.process_input(events, pressed_keys)

    def update(self):
        self.all_sprites.update()
    
    def render(self):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)


class EndScene(Scene):
    def __init__(self):
        super().__init__()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = TitleScene()
    
    def update(self):
        pass
    
    def render(self):
        screen.fill(BLACK)
        draw_text(screen, "Game Over", font_lg, WHITE, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], 'center')

