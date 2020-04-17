import platform
import pygame
import constants
from scene_manager import SceneManager

pygame.init()

fullscreen = True
if platform.system() == 'Windows':
    import ctypes
    ctypes.windll.user32.SetProcessDPIAware()
    monitor_dimensions = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
    print(monitor_dimensions)
else:
    monitor_dimensions = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    print(monitor_dimensions)

screen = pygame.display.set_mode(monitor_dimensions, pygame.FULLSCREEN)
running = True
scene_manager = SceneManager()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
        else:
            scene_manager.handle_event(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            scene_manager.
        elif event.type == pygame.MOUSEMOTION:
            print('mouse moved to', pygame.mouse.get_pos())

    if not scene_manager.current_scene():
        scene_manager.change_scene(constants.MAIN_MENU)

    scene_manager.draw_scene(screen)
    pygame.display.update()

