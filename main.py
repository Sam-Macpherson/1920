import pygame
import constants

from exceptions import Terminate
from scene_manager import SceneManager


def main():
    # pygame.init()

    fullscreen = True

    screen = pygame.display.set_mode(constants.MONITOR_DIMENSIONS, pygame.FULLSCREEN)
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
