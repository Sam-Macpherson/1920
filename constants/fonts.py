# Font constants.

import pygame.freetype

import constants.measurements as measurements
import utilities

# pygame.freetype.init()
pygame.font.init()
#
# BASKERVILLE_OLD_FACE = [
#     pygame.freetype.Font(utilities.relative_path('font_files/baskerville_old_face.ttf', __file__), i)
#     for i in range(0, measurements.MONITOR_DIMENSIONS[0])
# ]

MONOFONTO = [
    pygame.font.Font(utilities.relative_path('font_files/monofonto.ttf', __file__), i)
    for i in range(0, measurements.MONITOR_DIMENSIONS[0])
]

# TODO
"""
----------IMPORTANT NOTE----------

This version of LEMON MILK is absolutely free for personal, educational, non-profit, or charitable use. 
For commercial use, kindly donate me (pay as you want) as an appreciation. If you want to donate, my PayPal address is marsnev@marsnev.com
Every donation is greatly appreciated. 

If you need further information,
kindly check my F.A.Q page at: http://blog.marsnev.com/p/faq.html

if you cannot get the answers there,
kindly contact me at:
email address: marsnev@marsnev.com

"""
# LEMON_MILK_REGULAR = [
#     pygame.font.Font(utilities.relative_path('font_files/LEMONMILK-Regular.otf', __file__), i)
#     for i in range(0, measurements.MONITOR_DIMENSIONS[0])
# ]
