"""Button platform for the IR Candle integration."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_INFRARED_ENTITY_ID, IRCandlesCode
from .entity import IRCandlesEntity

PARALLEL_UPDATES = 1


@dataclass(frozen=True, kw_only=True)
class IRCandlesButtonDescription(ButtonEntityDescription):
    """Describes an IR Candles button."""

    command_code: IRCandlesCode


BUTTON_DESCRIPTIONS: tuple[IRCandlesButtonDescription, ...] = (
    IRCandlesButtonDescription(
        key="brightness_up",
        translation_key="brightness_up",
        icon="mdi:brightness-7",
        command_code=IRCandlesCode.BRIGHTNESS_UP,
    ),
    IRCandlesButtonDescription(
        key="brightness_down",
        translation_key="brightness_down",
        icon="mdi:brightness-5",
        command_code=IRCandlesCode.BRIGHTNESS_DOWN,
    ),
    IRCandlesButtonDescription(
        key="timer_2h",
        translation_key="timer_2h",
        icon="mdi:timer-outline",
        command_code=IRCandlesCode.TIMER_2H,
    ),
    IRCandlesButtonDescription(
        key="timer_4h",
        translation_key="timer_4h",
        icon="mdi:timer-outline",
        command_code=IRCandlesCode.TIMER_4H,
    ),
    IRCandlesButtonDescription(
        key="timer_6h",
        translation_key="timer_6h",
        icon="mdi:timer-outline",
        command_code=IRCandlesCode.TIMER_6H,
    ),
    IRCandlesButtonDescription(
        key="timer_8h",
        translation_key="timer_8h",
        icon="mdi:timer-outline",
        command_code=IRCandlesCode.TIMER_8H,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up IR Candles buttons from a config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    async_add_entities(
        IRCandlesButton(entry, infrared_entity_id, description)
        for description in BUTTON_DESCRIPTIONS
    )


class IRCandlesButton(IRCandlesEntity, ButtonEntity):
    """IR Candles timer button entity."""

    entity_description: IRCandlesButtonDescription

    def __init__(
        self,
        entry: ConfigEntry,
        infrared_entity_id: str,
        description: IRCandlesButtonDescription,
    ) -> None:
        """Initialize the button entity."""
        super().__init__(entry, infrared_entity_id, unique_id_suffix=description.key)
        self.entity_description = description

    async def async_press(self) -> None:
        """Send the timer IR command."""
        await self._send_command(self.entity_description.command_code)
