from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Header, Footer
from textual.containers import Container, VerticalScroll, Vertical, Horizontal
from textual.reactive import reactive
from textual.widgets import RichLog

from playerctlWrapper import PlayerctlWrapper
from components import PlayerList, PlayerInfo, Controls

class MainApp(App):
    CSS_PATH = "styles.tcss"
    TITLE = "Playerctl TUI"
    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [("space", "toggle_play", "Play/Pause"), ("n", "next", "Siguiente")]
    
    # init=False evita que falle al arrancar la app
    count = reactive(0, init=False)

    def __init__(self) -> None:
        super().__init__()
        self.player = PlayerctlWrapper()
        self.active_player = ""

    def compose(self) -> ComposeResult: 
        yield Header()
        with Horizontal(id="main-layout"):
            with Vertical(id="left-panel"):
                yield Static("Players", classes="panel-header")
                yield PlayerList(player=self.player, classes="player_list")
            with Vertical(id="right-panel"):
                yield Static("Player Info", classes="panel-header")
                yield PlayerInfo(classes="player_info")
                yield Controls(classes="controls")
        #yield Footer()

    def on_mount(self) -> None:
        self.log_players()

    def log_players(self) -> None:
        players = self.player.list_players()
        self.log(f"Available players: {', '.join(players) if players else 'None'}")

if __name__ == "__main__":
    MainApp().run()
