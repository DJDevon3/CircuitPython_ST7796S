Introduction
============



.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/DJDevon3/CircuitPython_ST7796/workflows/Build%20CI/badge.svg
    :target: https://github.com/DJDevon3/CircuitPython_ST7796/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

displayio driver for ST7796S TFT LCD displays


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Usage Example
=============

.. code-block:: python

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
	display.root_group = text_group
	
	while True:
	    hello_label.text = "HELLO WORLD!"


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/DJDevon3/CircuitPython_ST7796/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
