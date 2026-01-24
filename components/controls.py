from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal

class Controls(Static):
    """Widget que muestra los controles del reproductor activo."""
    ICONS = {
        "play": "󰐊",        # \U000f040a
        "pause": "󰏤",       # \U000f03e4
        "stop": "󰓛",        # \U000f04db
        "next": "󰒭",        # \U000f04ad
        "prev": "󰒮",        # \U000f04ae
        "shuffle": "󰒝",     # \U000f049f
        "repeat": "󰑖",      # \U000f0456
        "volume_up": "󰕾",   # \U000f057e
    }

    def compose(self) -> ComposeResult:
        with Horizontal(classes="transport-controls"):
            yield Static(self.ICONS["prev"], classes="btn-small")
            yield Static(self.ICONS["play"], classes="btn-main") # Este será el más grande
            yield Static(self.ICONS["next"], classes="btn-small")

    def update_play_icon(self, is_playing: bool):
        # Buscamos el widget de play/pause
        icon_widget = self.query_one("#play-pause-btn", Static)
        
        # Cambiamos el icono según el estado real del reproductor
        if is_playing:
            icon_widget.update(self.ICONS["pause"])
        else:
            icon_widget.update(self.ICONS["play"])
