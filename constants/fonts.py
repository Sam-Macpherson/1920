# Font constants.

import pygame.freetype

import utilities

pygame.freetype.init()

BASKERVILLE_OLD_FACE_12 = pygame.freetype.Font(utilities.relative_path('baskerville_old_face.ttf', __file__), 12)
BASKERVILLE_OLD_FACE_24 = pygame.freetype.Font(utilities.relative_path('baskerville_old_face.ttf', __file__), 24)
BASKERVILLE_OLD_FACE_36 = pygame.freetype.Font(utilities.relative_path('baskerville_old_face.ttf', __file__), 36)
BASKERVILLE_OLD_FACE_48 = pygame.freetype.Font(utilities.relative_path('baskerville_old_face.ttf', __file__), 48)
BASKERVILLE_OLD_FACE_60 = pygame.freetype.Font(utilities.relative_path('baskerville_old_face.ttf', __file__), 60)
BASKERVILLE_OLD_FACE_72 = pygame.freetype.Font(utilities.relative_path('baskerville_old_face.ttf', __file__), 72)
BASKERVILLE_OLD_FACE_84 = pygame.freetype.Font(utilities.relative_path('baskerville_old_face.ttf', __file__), 84)
