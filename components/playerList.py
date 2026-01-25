from textual.app import ComposeResult
from textual.widgets import Static, Label, ListView, ListItem
import re
from playerctlWrapper import PlayerctlWrapper

class PlayerList(Static):
    BORDER_TITLE = "Players"
    CSS_PATH = "playerList.tcss"

    def __init__(self, player: PlayerctlWrapper, **kwargs):
        super().__init__(**kwargs)
        self.player = player

    def compose(self) -> ComposeResult:
        yield ListView(id="list-view-players")

    def on_mount(self) -> None:
        self.refresh_players()
        self.set_interval(2.0, self.refresh_players)

    def refresh_players(self) -> None:
        raw_players = self.player.list_players()
        clean_players = [re.sub(r"\..*", "", p) for p in raw_players]
        unique_players = list(set(clean_players))

        self.update_players(unique_players)

    def update_players(self, players: list[str]) -> None:
        list_view = self.query_one("#list-view-players", ListView)
        
        current_players = []
        for item in list_view.children:
            name = getattr(item, "player_name", None)
            if name:
                current_players.append(name)
        
        if set(current_players) != set(players):
            highlighted_idx = list_view.index
            list_view.clear()
            
            if not players:
                item = ListItem(Label("No hay reproductores"))
                item.player_name = None
                list_view.append(item)
            else:
                for i, p in enumerate(players):
                    label_text = f"󰎆 {p}"
                    if i == highlighted_idx:
                        label_text = f"> {p} <"
                    
                    item = ListItem(Label(label_text))
                    item.player_name = p
                    list_view.append(item)
            
            if highlighted_idx is not None and highlighted_idx < len(players):
                list_view.index = highlighted_idx

    def on_list_view_highlighted_changed(self, event: ListView.HighlightedChanged) -> None:
        """Adds markers to the currently highlighted item."""
        list_view = self.query_one("#list-view-players", ListView)
        for i, item in enumerate(list_view.children):
            label = item.query_one(Label)
            name = getattr(item, "player_name", None)
            if not name:
                continue
                
            if i == event.index:
                label.update(f"> {name} <")
            else:
                label.update(f"󰎆 {name}")
    
    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Evento que se dispara al seleccionar un reproductor."""
        player_name = getattr(event.item, "player_name", None)
        if player_name:
            self.app.notify(f"Seleccionado: {player_name}")
        else:
            self.app.notify("Ningún reproductor seleccionado")