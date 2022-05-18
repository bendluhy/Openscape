import pygame
from scenemanager.Scene import SceneBase
from util import DebugMessager


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    def processinput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    DebugMessager.errormessage("SceneManager","No more scenes!")
    def update(self):
        pass
    def render(self, screen,surface):
        screen.fill((255,0,0))