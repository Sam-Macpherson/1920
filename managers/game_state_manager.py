"""
The game loop:
1. Listen to the radio for the local news
2. Go to work
3. Be at work and twirl the pizzas
4. Manage the books at work
5. Go home from work

As the game progresses, up and coming events will disrupt this loop.
i.e. one night when the player is in stage 5, instead of the usual
"go home" scene, the player is accosted by mafia representatives.

It's all about systematically adding phases and complexity to the
main loop over time.

The GameStateManager is in charge of knowing the current scene situation,
as well as the player's notable stats. The Game State manager is the
workhorse which will handle all the data input/output to/from each scene,
and will prompt scene transitions, and maintain timers.
"""
import pygame

import constants
import constants.game_loop_states as game_loop_states
from exceptions import Terminate, StartGameLoop, TransitionScene
from managers import SceneManager


class GameStateManager:

    def __init__(self, screen):
        self._game_running = True
        self._game_loop_is_running = False
        self._game_loop_states = game_loop_states.INITIAL_GAME_LOOP_STATES
        self._current_game_loop_index = -1
        self._screen = screen
        self._scene_manager = SceneManager()
        self._scene_manager.change_scene(constants.MAIN_MENU_SCENE)
        super().__init__()

    def game_is_running(self):
        return self._game_running

    def handle_event(self, event):
        try:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                raise Terminate
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                self._scene_manager.pop_scene()
            elif event.type == pygame.MOUSEMOTION:
                self._scene_manager.handle_mouse_motion(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                self._scene_manager.handle_mouse_button_up(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._scene_manager.handle_mouse_button_down(pygame.mouse.get_pos())
        except StartGameLoop:
            self._game_loop_is_running = True
            self._current_game_loop_index = 0
            self._scene_manager.change_scene(self._game_loop_states[self._current_game_loop_index])
        except TransitionScene:
            self._current_game_loop_index = (self._current_game_loop_index + 1) % len(self._game_loop_states)
            self._scene_manager.change_scene(self._game_loop_states[self._current_game_loop_index])
            self._scene_manager.handle_mouse_motion(pygame.mouse.get_pos())
        except Terminate:
            self._game_running = False

    def draw(self, screen):
        self._scene_manager.draw_scene(screen)
