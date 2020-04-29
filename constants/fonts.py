# Font constants.

import pygame.freetype

import constants.measurements as measurements
import utilities

pygame.freetype.init()

BASKERVILLE_OLD_FACE = [
    pygame.freetype.Font(utilities.relative_path('baskerville_old_face.ttf', __file__), i)
    for i in range(0, measurements.MONITOR_DIMENSIONS[0])
]