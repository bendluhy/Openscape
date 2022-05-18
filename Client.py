import pygame

from scenemanager.TitleScene import TitleScene
from util import Reference, Settings, DebugMessager

# MAIN WINDOW #
pygame.init()
DebugMessager.debugmessage("LAUNCH", f"Launching Game VERSION: {Reference.version} DEVSTAGE: {Reference.development_stage}")
screen = pygame.display.set_mode([Settings.windowX, Settings.windowY])
pygame.display.set_caption(f"Openscape {Reference.version} {Reference.development_stage}")
clock = pygame.time.Clock()
active_scene = TitleScene()
while active_scene != None:
    pressed_keys = pygame.key.get_pressed()

    # Event filtering
    filtered_events = []
    for event in pygame.event.get():
        quit_attempt = False
        if event.type == pygame.QUIT:
            quit_attempt = True
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or \
                          pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_ESCAPE:
                quit_attempt = True
            elif event.key == pygame.K_F4 and alt_pressed:
                quit_attempt = True

        if quit_attempt:
            active_scene.terminate()
        else:
            filtered_events.append(event)

    active_scene.processinput(filtered_events, pressed_keys)
    active_scene.update()
    active_scene.render(screen)

    active_scene = active_scene.next

    pygame.display.flip()
    clock.tick(Settings.fps)



    # Flip the display
    pygame.display.flip()

