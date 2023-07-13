# SPDX-FileCopyrightText: 2023 DJDevon3
# SPDX-License-Identifier: MIT
# Circuit Python displayio Driver for ST7796x based displays

import board
import displayio
import terminalio
from adafruit_display_text import label
from circuitpython_st7796 import ST7796

spi = board.SPI()
while not spi.try_lock():
    pass
spi.configure(baudrate=24000000)  # Configure SPI for 24MHz
spi.unlock()
tft_cs = board.D9
tft_dc = board.D10
tft_rst = board.D12

# 4.0" ST7796S Display
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 320

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7796(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, rotation=270)

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
hello_label.anchored_position = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)
hello_label.scale = (3)
hello_label.color = TEXT_WHITE

# Create Display Groups
text_group = displayio.Group()
text_group.append(hello_label)
display.show(text_group)

while True:
    hello_label.text = "HELLO WORLD!"
