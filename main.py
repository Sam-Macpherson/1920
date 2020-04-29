import pygame
from pygame.time import Clock

import constants
import sprites

from managers import GameStateManager


def main():
    pygame.init()
    # This is here because cx_Freeze won't include image asset folders for some reason.
    hack = sprites.SPRITES_CONSTANT
    # Don't look at that line, look at these lines down here instead! :D
    screen = pygame.display.set_mode(constants.MONITOR_DIMENSIONS, pygame.FULLSCREEN)
    game_state_manager = GameStateManager(screen)

    while game_state_manager.game_is_running():
        # Handle all events.
        for event in pygame.event.get():
            game_state_manager.handle_event(event)
        # Draw the screen.
        game_state_manager.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
