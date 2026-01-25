from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.containers import Horizontal, Vertical

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
        "volume_down": "󰕿", # \U000f057d
        "mute": "󰝟"         # \U000f075f
    }
    BORDER_TITLE = "Controls"

    def compose(self) -> ComposeResult:
        with Horizontal(classes="controls-wrapper"):
            # Grupo 1: Opciones (Izquierda)
            with Horizontal(id="playback-options", classes="control-group"):
                yield Button(self.ICONS["shuffle"], id="shuffle-btn", classes="btn-small")
                yield Button(self.ICONS["repeat"], id="repeat-btn", classes="btn-small")

            # Grupo 2: Transporte (Centro)
            with Horizontal(id="transport-main", classes="control-group"):
                yield Button(self.ICONS["prev"], id="prev-btn", classes="btn-small")
                # yield Button(self.ICONS["play"], id="play-pause-btn", classes="btn-main")
                yield Button(self.ICONS["play"], id="play-pause-btn", classes="btn-small")
                yield Button(self.ICONS["stop"], id="stop-btn", classes="btn-small")
                yield Button(self.ICONS["next"], id="next-btn", classes="btn-small")

            # Grupo 3: Volumen (Derecha)
            with Horizontal(id="volume-controls", classes="control-group"):
                yield Button(self.ICONS["volume_down"], id="vol-down-btn", classes="btn-small")
                yield Button(self.ICONS["mute"], id="mute-btn", classes="btn-small")
                yield Button(self.ICONS["volume_up"], id="vol-up-btn", classes="btn-small")

    def update_play_icon(self, is_playing: bool):
        # Buscamos el widget de play/pause
        icon_widget = self.query_one("#play-pause-btn", Static)
        
        # Cambiamos el icono según el estado real del reproductor
        if is_playing:
            icon_widget.update(self.ICONS["pause"])
        else:
            icon_widget.update(self.ICONS["play"])
