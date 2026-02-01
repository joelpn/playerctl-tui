from textual.app import ComposeResult
from textual.widgets import Static, Label, ListView, ListItem
import re
from playerctlWrapper import PlayerctlWrapper

class PlayerList(Static):
    # BORDER_TITLE = "Players"

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

        player_data = []
        for p in raw_players:
            player_data.append({
                "real_id": p,
                "clean_name": re.sub(r"\..*", "", p).capitalize()
            })
        
        self.update_players(player_data)

    def update_players(self, player_data: list[dict]) -> None:
        list_view = self.query_one("#list-view-players", ListView)
        
        new_ids = [p["real_id"] for p in player_data]
        current_ids = [getattr(item, "player_id", "") for item in list_view.children]
        
        if set(current_ids) != set(new_ids):
            highlighted_idx = list_view.index
            list_view.clear()
            
            if not player_data:
                item = ListItem(Label("󰝛 No hay reproductores"))
                item.player_id = None
                list_view.append(item)
            else:
                for p in player_data:
                    item = ListItem(Label(f"󰎆 {p['clean_name']}"))
                    item.player_id = p["real_id"]   # ID sucio (instancia)
                    item.player_name = p["clean_name"] # Nombre bonito
                    list_view.append(item)
            
            if highlighted_idx is not None and highlighted_idx < len(player_data):
                list_view.index = highlighted_idx

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        player_name = getattr(event.item, "player_id", None)
        self.app.active_player = player_name