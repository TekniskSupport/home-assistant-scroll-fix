import logging

import homeassistant.components.frontend
from homeassistant.components.frontend import _frontend_root

_LOGGER = logging.getLogger(__name__)
DOMAIN = "scrollfix"

async def async_setup(hass, config):
    return await apply_hooks(hass)

async def async_setup_entry(hass, config_entry):
    return await apply_hooks(hass)

async def apply_hooks(hass):
    def _get_template(self):
        tpl = data["get_template"](self)
        render = tpl.render

        def new_render(*args, **kwargs):
                text = text.replace("<body>", "<body>
                    <script type="module">
                        document.querySelector('body').style.overflowX='hidden';
                        document.querySelector('body').style.overflowY='scroll';
                    </script>
                ")

            return text

        tpl.render = new_render
        return tpl
    homeassistant.components.frontend.IndexView.get_template = _get_template
    return True

def remove_hooks(hass):
    return True
