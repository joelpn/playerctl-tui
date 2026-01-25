from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Container

class PlayerInfo(Static):
    """Widget que muestra la información del reproductor activo."""
    BORDER_TITLE = "Player Info"

    def compose(self) -> ComposeResult:
        # with Container():
            yield Static("Información disponible:")
