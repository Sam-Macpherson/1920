import pygame
import constants

from managers import GameStateManager


def main():
    screen = pygame.display.set_mode(constants.MONITOR_DIMENSIONS, pygame.FULLSCREEN)
    game_state_manager = GameStateManager(screen)

    while game_state_manager.game_is_running():
        for event in pygame.event.get():
            game_state_manager.handle_event(event)


if __name__ == "__main__":
    main()
print('done')
