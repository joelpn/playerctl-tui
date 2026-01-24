from textual.app import ComposeResult
from textual.widgets import Static

class PlayerInfo(Static):
    """Widget que muestra la información del reproductor activo."""

    def compose(self) -> ComposeResult:
        yield Static("Información disponible:")
