import pygame
from scenemanager.Scene import SceneBase
from util import DebugMessager
from util import fonts


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.player_x = 500
        self.player_y = 500
        self.movespeed = 5
    def processinput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    DebugMessager.errormessage("SceneManager","No more scenes!")



    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.player_y -= self.movespeed
        if key[pygame.K_s]:
            self.player_y += self.movespeed
        if key[pygame.K_a]:
            self.player_x -= self.movespeed
        if key[pygame.K_d]:
            self.player_x += self.movespeed
    def render(self, screen:pygame.surface,surface, clock):

        #Set screen blank
        screen.fill((255,255,255))

        #render terrain


        # render player
        pygame.draw.rect(screen,(0,0,255),(self.player_x,self.player_y,50,50))


        #render gui if there is any
        pygame.draw.rect(screen,(0,0,0),(500,500,100,100))

        text = fonts.fps_font.render(str(int(clock.get_fps())), False, (0, 0, 0))
        screen.blit(text,(0,0))

