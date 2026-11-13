"""
Custom integration to integrate ir_candles with Home Assistant.

For more details about this integration, please refer to
https://github.com/astrandb/ir_candles
"""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

PLATFORMS = [Platform.LIGHT, Platform.BUTTON]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up IR Candles from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload an IR Candles config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
