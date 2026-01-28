from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Header, Footer
from textual.containers import Container, VerticalScroll, Vertical, Horizontal
from textual.reactive import reactive
from textual.widgets import RichLog

from playerctlWrapper import PlayerctlWrapper
from components import PlayerList, PlayerInfo, PlayerControls

class MainApp(App):
    CSS_PATH = "styles.tcss"
    TITLE = "Playerctl TUI"
    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [("space", "toggle_play", "Play/Pause"), ("n", "next", "Siguiente")]
    
    def __init__(self) -> None:
        super().__init__()
        self.player = PlayerctlWrapper()
        self.active_player = ""

    def compose(self) -> ComposeResult: 
        yield Header()
        with Horizontal(id="main-layout"):
            with Vertical(id="left-panel"):
                yield PlayerList(player=self.player, classes="player_list")
            with Vertical(id="right-panel"):
                yield PlayerInfo(player=self.player, classes="player_info")
                yield PlayerControls(player=self.player, classes="controls")
        #yield Footer()

if __name__ == "__main__":
    MainApp().run()
