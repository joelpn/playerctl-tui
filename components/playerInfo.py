from textual.app import ComposeResult
from textual.widgets import Static, ProgressBar, Label
from textual.containers import Container, Vertical, Horizontal, Center, Middle
from playerctlWrapper import PlayerctlWrapper
from textual.color import Gradient

class PlayerInfo(Static):
    """Widget que muestra la información del reproductor activo con un diseño mejorado."""
    BORDER_TITLE = "Player Info"

    def __init__(self, player: PlayerctlWrapper, **kwargs):
        super().__init__(**kwargs)
        self.player = player
    
    def compose(self) -> ComposeResult:
        gradient = Gradient.from_colors(
            "#881177", "#aa3355", "#cc6666", "#ee9944", "#eedd00",
            "#99dd55", "#44dd88", "#22ccbb", "#00bbcc", "#0099cc",
            "#3366bb", "#663399",
        )

        with Container(classes="info-container"):
            # Estado vacío
            with Center(id="info-empty-state"):
                yield Label("Seleccione un reproductor...", id="info-status-label")
            
            # Contenido principal
            with Vertical(id="info-content"):
                # with Center():
                #     yield Label(" NOW PLAYING", id="info-header")
                
                with Vertical(classes="metadata-container"):
                    yield Label("", id="info-title", classes="title-label")
                    yield Label("", id="info-artist", classes="artist-label")
                    yield Label("", id="info-album", classes="album-label")
                
                with Vertical(classes="progress-wrapper"):
                    with Horizontal(classes="time-labels"):
                        yield Label("0:00", id="time-current")
                        yield Static("", classes="flex-spacer")
                        yield Label("0:00", id="time-total")
                    
                    yield ProgressBar(
                        show_percentage=False, 
                        show_eta=False, 
                        id="info-progress", 
                        classes="info-progress-bar",
                        gradient=gradient
                    )

    def on_mount(self) -> None:
        self.query_one("#info-content").display = False
        self.set_interval(0.5, self.refresh_info)

    def format_time(self, seconds: int) -> str:
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds:02d}"

    def refresh_info(self) -> None:
        active = getattr(self.app, "active_player", None)
        empty_state = self.query_one("#info-empty-state")
        content = self.query_one("#info-content")
        
        if not active:
            empty_state.display = True
            content.display = False
            return

        empty_state.display = False
        content.display = True

        metadata = self.player.get_metadata(active)
        position = self.player.get_position(active)
        length = int(metadata.get("length", 0))

        # Actualizar metadatos
        self.query_one("#info-title").update(str(metadata.get("title", "")))
        
        if metadata.get('artist', '') != '':
            self.query_one("#info-artist").update(f"👤 {metadata.get('artist', '')}")
        else:
            self.query_one("#info-artist").update("")
        
        if metadata.get('album', '') != '':
            self.query_one("#info-album").update(f"💿 {metadata.get('album', '')}")
        else:
            self.query_one("#info-album").update("")

        # Actualizar tiempos
        self.query_one("#time-current").update(self.format_time(int(position)))
        self.query_one("#time-total").update(self.format_time(length))

        # Actualizar barra de progreso
        progress_bar = self.query_one("#info-progress", ProgressBar)
        if length > 0:
            progress_bar.total = length
            progress_bar.update(progress=position)
            progress_bar.display = True
        else:
            progress_bar.display = False