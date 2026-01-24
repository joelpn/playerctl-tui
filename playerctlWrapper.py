"""Wrapper for playerctl commands."""

import subprocess
from typing import List, Dict, Optional


class PlayerctlWrapper:
    """Wrapper class for executing playerctl commands."""

    @staticmethod
    def _run_command(args: List[str]) -> str:
        """Run a playerctl command and return the output."""
        try:
            result = subprocess.run(
                ["playerctl"] + args,
                capture_output=True,
                text=True,
                timeout=2
            )
            return result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return ""

    def list_players(self) -> List[str]:
        """List all available players."""
        output = self._run_command(["-l"])
        if output:
            return [player.strip() for player in output.split("\n") if player.strip()]
        return []

    def get_status(self, player: str) -> str:
        """Get the playback status of a player."""
        output = self._run_command(["-p", player, "status"])
        return output if output else "Stopped"

    def get_metadata(self, player: str) -> Dict[str, str]:
        """Get metadata for the current track."""
        metadata = {}
        
        # Get title
        title = self._run_command(["-p", player, "metadata", "title"])
        if title:
            metadata["title"] = title
        
        # Get artist
        artist = self._run_command(["-p", player, "metadata", "artist"])
        if artist:
            metadata["artist"] = artist
        
        # Get album
        album = self._run_command(["-p", player, "metadata", "album"])
        if album:
            metadata["album"] = album
        
        # Get length (duration in microseconds)
        length = self._run_command(["-p", player, "metadata", "mpris:length"])
        if length and length.isdigit():
            metadata["length"] = str(int(length) // 1000000)  # Convert to seconds
        
        return metadata

    def get_position(self, player: str) -> Optional[int]:
        """Get the current position in seconds."""
        output = self._run_command(["-p", player, "position"])
        try:
            return int(float(output))
        except (ValueError, TypeError):
            return None

    def get_volume(self, player: str) -> Optional[float]:
        """Get the current volume (0.0 to 1.0)."""
        output = self._run_command(["-p", player, "volume"])
        try:
            return float(output)
        except (ValueError, TypeError):
            return None

    def play_pause(self, player: str) -> None:
        """Toggle play/pause."""
        self._run_command(["-p", player, "play-pause"])

    def play(self, player: str) -> None:
        """Start playback."""
        self._run_command(["-p", player, "play"])

    def pause(self, player: str) -> None:
        """Pause playback."""
        self._run_command(["-p", player, "pause"])

    def stop(self, player: str) -> None:
        """Stop playback."""
        self._run_command(["-p", player, "stop"])

    def next_track(self, player: str) -> None:
        """Skip to next track."""
        self._run_command(["-p", player, "next"])

    def previous_track(self, player: str) -> None:
        """Skip to previous track."""
        self._run_command(["-p", player, "previous"])

    def set_volume(self, player: str, level: float) -> None:
        """Set volume (0.0 to 1.0)."""
        level = max(0.0, min(1.0, level))  # Clamp between 0 and 1
        self._run_command(["-p", player, "volume", str(level)])

    def volume_up(self, player: str, amount: float = 0.05) -> None:
        """Increase volume."""
        self._run_command(["-p", player, "volume", f"{amount}+"])

    def volume_down(self, player: str, amount: float = 0.05) -> None:
        """Decrease volume."""
        self._run_command(["-p", player, "volume", f"{amount}-"])

    def get_shuffle(self, player: str) -> Optional[str]:
        """Get shuffle status."""
        output = self._run_command(["-p", player, "shuffle"])
        return output if output else None

    def toggle_shuffle(self, player: str) -> None:
        """Toggle shuffle."""
        self._run_command(["-p", player, "shuffle", "Toggle"])

    def get_loop(self, player: str) -> Optional[str]:
        """Get loop status."""
        output = self._run_command(["-p", player, "loop"])
        return output if output else None

    def toggle_loop(self, player: str) -> None:
        """Toggle loop between None, Track, and Playlist."""
        current = self.get_loop(player)
        if current == "None":
            self._run_command(["-p", player, "loop", "Track"])
        elif current == "Track":
            self._run_command(["-p", player, "loop", "Playlist"])
        else:
            self._run_command(["-p", player, "loop", "None"])
