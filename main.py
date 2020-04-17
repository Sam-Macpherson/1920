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
else:
    monitor_dimensions = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(monitor_dimensions, pygame.FULLSCREEN)
running = True
scene_manager = SceneManager()

while running:
    if not scene_manager.current_scene():
        scene_manager.change_scene(constants.MAIN_MENU)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            scene_manager.handle_mouse_motion(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            scene_manager.handle_mouse_button_up(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            scene_manager.handle_mouse_button_down(pygame.mouse.get_pos())


    scene_manager.draw_scene(screen)
    pygame.display.update()

