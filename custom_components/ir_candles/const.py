"""Constants for the IR Candles integration."""

import logging
from enum import IntEnum

from infrared_protocols.commands.nec import NECCommand

_LOGGER = logging.getLogger(__name__)

DOMAIN = "ir_candles"

CONF_INFRARED_ENTITY_ID = "infrared_entity_id"

_BRIGHTNESS_NEC_ADDRESS = 0x08B7  # Extended NEC — no address parity


class IRCandlesCode(IntEnum):
    """IR command codes for the IRCandles FB-0001 remote."""

    ON = 0x00
    OFF = 0x02
    FLICKERING = 0x10
    STEADY = 0x12
    TIMER_4H = 0x08
    TIMER_8H = 0x0A
    BRIGHTNESS_UP = 0x82
    BRIGHTNESS_DOWN = 0x80

    # ON = 0x5E
    # OFF = 0x0C
    # BRIGHTNESS_UP = 0x12
    # BRIGHTNESS_DOWN = 0x10
    # TIMER_2H = 0x46
    # TIMER_4H = 0x40
    # TIMER_6H = 0x15
    # TIMER_8H = 0x19

    def to_command(self) -> NECCommand:
        """Return a NECCommand for this button press."""
        if self in (IRCandlesCode.BRIGHTNESS_UP, IRCandlesCode.BRIGHTNESS_DOWN):
            # Brightness buttons use Extended NEC (16-bit address, no inverse check)
            return NECCommand(address=_BRIGHTNESS_NEC_ADDRESS, command=self.value)
        return NECCommand(address=0x00, command=self.value)
