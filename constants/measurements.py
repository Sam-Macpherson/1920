# Measurement constants.

import ctypes
import platform

import pygame

if platform.system() == 'Windows':
    ctypes.windll.user32.SetProcessDPIAware()
    MONITOR_DIMENSIONS = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
else:
    pygame.init()
    MONITOR_DIMENSIONS = (pygame.display.Info().current_w, pygame.display.Info().current_h)


# Button positioning and measurements.
BUTTON_BORDER_WEIGHT = 10

# Main Menu buttons.
MAIN_MENU_EXIT_BUTTON_DIMENSIONS = (MONITOR_DIMENSIONS[0] // 5, MONITOR_DIMENSIONS[1] // 10)
MAIN_MENU_EXIT_BUTTON_COORDS = (
    MONITOR_DIMENSIONS[0] - MAIN_MENU_EXIT_BUTTON_DIMENSIONS[0],
    MONITOR_DIMENSIONS[1] - MAIN_MENU_EXIT_BUTTON_DIMENSIONS[1]
)
MAIN_MENU_SETTINGS_BUTTON_DIMENSIONS = (MONITOR_DIMENSIONS[0] // 5, MONITOR_DIMENSIONS[1] // 10)
MAIN_MENU_SETTINGS_BUTTON_COORDS = (
    MONITOR_DIMENSIONS[0] - MAIN_MENU_SETTINGS_BUTTON_DIMENSIONS[0],
    MAIN_MENU_EXIT_BUTTON_COORDS[1] - MAIN_MENU_SETTINGS_BUTTON_DIMENSIONS[1]
)
