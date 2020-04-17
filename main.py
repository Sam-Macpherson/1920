import ctypes
import pygame
import platform
import constants

from exceptions import Terminate
from scene_manager import SceneManager


def main():
    pygame.init()

    fullscreen = True
    if platform.system() == 'Windows':
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
        try:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    raise Terminate
                elif event.type == pygame.MOUSEMOTION:
                    scene_manager.handle_mouse_motion(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    scene_manager.handle_mouse_button_up(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    scene_manager.handle_mouse_button_down(pygame.mouse.get_pos())

            scene_manager.draw_scene(screen)
            pygame.display.update()

        except Terminate:
            running = False


main()
