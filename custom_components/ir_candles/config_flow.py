"""Config flow for the IR Candles integration."""

from __future__ import annotations

from typing import Any

import probatio
from homeassistant.components.infrared import (
    DOMAIN as INFRARED_DOMAIN,
)
from homeassistant.components.infrared import (
    async_get_emitters,
)
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.selector import (
    EntitySelector,
    EntitySelectorConfig,
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)

from .const import CONF_INFRARED_ENTITY_ID, CONF_REMOTE_MODEL, DOMAIN, REMOTES


class IRCandlesConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for IR Candles."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        emitter_entity_ids = async_get_emitters(self.hass)
        if not emitter_entity_ids:
            return self.async_abort(reason="no_emitters")

        if user_input is not None:
            entity_id = user_input[CONF_INFRARED_ENTITY_ID]
            remote_model = user_input[CONF_REMOTE_MODEL]

            await self.async_set_unique_id(f"ir_candles_{entity_id}_{remote_model}")
            self._abort_if_unique_id_configured()

            ent_reg = er.async_get(self.hass)
            entry = ent_reg.async_get(entity_id)
            entity_name = (
                entry.name or entry.original_name or entity_id if entry else entity_id
            )
            title = f"IR Candles via {entity_name}"

            return self.async_create_entry(title=title, data=user_input)

        remotes_list = list(REMOTES.keys())
        return self.async_show_form(
            step_id="user",
            data_schema=probatio.Schema(
                {
                    probatio.Required(CONF_REMOTE_MODEL): SelectSelector(
                        SelectSelectorConfig(
                            options=remotes_list,
                            translation_key="remote_model",
                            mode=SelectSelectorMode.DROPDOWN,
                            sort=True,
                        )
                    ),
                    probatio.Required(CONF_INFRARED_ENTITY_ID): EntitySelector(
                        EntitySelectorConfig(
                            domain=INFRARED_DOMAIN,
                            include_entities=emitter_entity_ids,
                        )
                    ),
                }
            ),
        )
