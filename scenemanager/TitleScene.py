import pygame

from scenemanager.Scene import SceneBase
from scenemanager.Game import GameScene
from scenemanager.WorldsListScene import WorldList
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # Check for SinglePlayer Button
                    if 800 < pygame.mouse.get_pos()[0] < 1100:
                        if  300 < pygame.mouse.get_pos()[1]  < 425:
                            DebugMessager.debugmessage("GUI", "Player Clicked Singleplayer Button")
                            self.switchtoscene(WorldList())

    def update(self):
        pass

    def render(self, screen, surface:pygame.Surface):
        surface.fill((0,255,255))

        #Init Font
        text = fonts.title_font.render("OpenScape", False, (0, 0, 0))
        surface.blit(text,((Settings.windowX/2) - 200,50))

        #SinglePlayer Button
        pygame.draw.rect(surface, (255,255,255), (800,300,300,125))
        text = fonts.button_font.render("SinglePlayer", False, (0, 0, 0))
        surface.blit(text,(830,340))

        pygame.transform.scale(screen, (Settings.windowX, Settings.windowY))
        screen.blit(surface,(0,0))



