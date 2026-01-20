from textual.app import App, ComposeResult
from textual.widgets import Label, Header, Footer, Button, Static
from textual.containers import Container
#from app import PlayerctlApp

class MainApp(App):
    CSS_PATH = "styles.tcss"

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult: 
        # yield Header()
        yield Container(
            Static("Contador", id="contador"),
            Button("Incrementar", id="btn-inc"),
            Button("Decrementar", id="btn-dec"),
        )
        # yield Label("--------><--------")
        # yield Footer()

if __name__ == "__main__":
    app = MainApp()
    app.run()
