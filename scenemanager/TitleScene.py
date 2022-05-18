import pygame

from scenemanager.Scene import SceneBase
from scenemanager.Game import GameScene
from util import DebugMessager, Settings,fonts
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
    def render(self, screen, surface:pygame.Surface):
        surface.fill((0,255,255))

        #Init Font
        font = fonts.title_font
        text = font.render("OpenScape", True, (0, 0, 0))
        surface.blit(text,((Settings.windowX/2) - 200,50))

        pygame.transform.scale(screen, (Settings.windowX, Settings.windowY))
        screen.blit(surface,(0,0))



