"""Constants for the IR Candles integration."""

import logging
from enum import IntEnum

from infrared_protocols.commands.nec import NECCommand

_LOGGER = logging.getLogger(__name__)

DOMAIN = "ir_candles"

CONF_INFRARED_ENTITY_ID = "infrared_entity_id"
CONF_REMOTE_MODEL = "remote_model"

_BRIGHTNESS_NEC_ADDRESS = 0x00  # Extended NEC — no address parity 08B7


class IRCandlesCode(IntEnum):
    """IR command codes for the IRCandles FB-0001 remote."""

    ON = 0x00
    OFF = 0x02
    FLICKERING = 0x10
    FLICKERING_10 = 0x0C
    STEADY = 0x12
    STEADY_10 = 0x0E
    TIMER_2H = 0x04
    TIMER_4H = 0x08
    TIMER_6H = 0x08
    TIMER_8H = 0x0A
    BRIGHTNESS_UP = 0x12
    BRIGHTNESS_DOWN = 0x10

    def to_command(self) -> NECCommand:
        """Return a NECCommand for this button press."""
        if self in (IRCandlesCode.BRIGHTNESS_UP, IRCandlesCode.BRIGHTNESS_DOWN):
            # Brightness buttons use Extended NEC (16-bit address, no inverse check)
            return NECCommand(address=_BRIGHTNESS_NEC_ADDRESS, command=self.value)
        return NECCommand(address=0x00, command=self.value)


REMOTES = {
    "six_buttons": {
        "buttons": [
            {"timer_4h": IRCandlesCode.TIMER_4H},
            {"timer_8h": IRCandlesCode.TIMER_8H},
            {"flickering": IRCandlesCode.FLICKERING},
            {"steady": IRCandlesCode.STEADY},
        ],
        "dimmable": False,
        "light": [
            {"on": IRCandlesCode.ON},
            {"off": IRCandlesCode.OFF},
        ],
    },
    "ten_buttons_rusta": {
        "buttons": [
            {"timer_2h": IRCandlesCode.TIMER_2H},
            {"timer_4h": IRCandlesCode.TIMER_4H},
            {"timer_6h": IRCandlesCode.TIMER_6H},
            {"timer_8h": IRCandlesCode.TIMER_8H},
            {"flickering": IRCandlesCode.FLICKERING_10},
            {"steady": IRCandlesCode.STEADY_10},
            {"brightness_up": IRCandlesCode.BRIGHTNESS_UP},
            {"brightness_down": IRCandlesCode.BRIGHTNESS_DOWN},
        ],
        "dimmable": True,
        "light": [
            {"on": IRCandlesCode.ON},
            {"off": IRCandlesCode.OFF},
            {"brightness_up": IRCandlesCode.BRIGHTNESS_UP},
            {"brightness_down": IRCandlesCode.BRIGHTNESS_DOWN},
        ],
    },
}
