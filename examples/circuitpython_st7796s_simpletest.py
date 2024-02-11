# SPDX-FileCopyrightText: 2023 DJDevon3
# SPDX-License-Identifier: MIT
# Circuit Python example for ST7796S TFT display

import board
import displayio
import terminalio
from adafruit_display_text import label
from circuitpython_st7796s import ST7796S

# Support both 8.x.x and 9.x.x. Change when 8.x.x is discontinued as a stable release.
try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire
spi = board.SPI()

# 4.0" ST7796S Display
displayio.release_displays()
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 320
DISPLAY_ROTATION = 180

tft_cs = board.D9
tft_dc = board.D10
tft_rst = board.D17
ts_cs = board.D6

spi = board.SPI()
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7796S(
    display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, rotation=DISPLAY_ROTATION
)

# Quick Colors for Labels
TEXT_BLACK = 0x000000
TEXT_BLUE = 0x0000FF
TEXT_CYAN = 0x00FFFF
TEXT_GRAY = 0x8B8B8B
TEXT_GREEN = 0x00FF00
TEXT_LIGHTBLUE = 0x90C7FF
TEXT_MAGENTA = 0xFF00FF
TEXT_ORANGE = 0xFFA500
TEXT_PURPLE = 0x800080
TEXT_RED = 0xFF0000
TEXT_WHITE = 0xFFFFFF
TEXT_YELLOW = 0xFFFF00

# Label Customizations
hello_label = label.Label(terminalio.FONT)
hello_label.anchor_point = (0.5, 1.0)
hello_label.anchored_position = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
hello_label.scale = 3
hello_label.color = TEXT_WHITE

# Create Display Groups
text_group = displayio.Group()
text_group.append(hello_label)
display.show(text_group)

while True:
    hello_label.text = "HELLO WORLD!"
