import pygame

from scenemanager.Scene import SceneBase
from scenemanager.Game import GameScene
from util import DebugMessager
import sys

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    def processinput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.switchtoscene(GameScene())
    def update(self):
        pass
    def render(self, screen):
        screen.fill((255,255,0))



