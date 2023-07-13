# SPDX-FileCopyrightText: 2023 DJDevon3
# SPDX-License-Identifier: MIT
# Generic Circuit Python Driver for ST7796x based displays

import displayio


_INIT_SEQUENCE = (
    b"\x01\x80\x96"  # _SWRESET and Delay 150ms
    b"\x11\x80\xFF"  # _SLPOUT and Delay 500ms
    b"\x3A\x81\x55\x0A"  # _COLMOD and Delay 10ms
    b"\x36\x01\x48"  # _MADCTL
    b"\x20\x80\x0A"  # _INVON Hack and Delay 10ms
    b"\x15\x80\x0A"  # _NORON and Delay 10ms
    b"\x36\x01\x48"  # _MADCTL
    b"\x29\x80"  # _DISPON and Delay 500ms
)


# pylint: disable=too-few-public-methods
class ST7796(displayio.Display):
    """ST7796 driver"""

    def __init__(self, bus: displayio.FourWire, **kwargs) -> None:
        super().__init__(bus, _INIT_SEQUENCE, **kwargs)
