from scenemanager.Scene import SceneBase
import pygame

class WorldList(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def processinput(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def render(self, screen:pygame.surface, surface):
        screen.fill((255,255,255))


