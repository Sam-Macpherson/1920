# The different phases in the game loop
import constants.scenes as scenes


LISTENING_TO_RADIO = scenes.ALARM_CLOCK_SCENE
GOING_TO_WORK = scenes.GOING_TO_WORK_SCENE
AT_WORK = scenes.RESTAURANT_SCENE
MANAGE_BOOKS = scenes.MANAGE_BOOKS_SCENE
LEAVING_WORK = scenes.LEAVING_WORK_SCENE

# The initial game loop is ordered here, this wil be built upon by the game
# state manager as the game progresses, and the order of this list will always
# be the order of the states in the game loop.
INITIAL_GAME_LOOP_STATES = [
    LISTENING_TO_RADIO,
    GOING_TO_WORK,
    AT_WORK,
    MANAGE_BOOKS,
    LEAVING_WORK
]
