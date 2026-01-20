# playerctl-tui

A modern, responsive TUI for controlling media playback via MPRIS using playerctl. Built with Python and Textual.

## Why?

I needed a simple TUI to control my media players - not a full music player, just controls for whatever's already playing. I found plenty of TUI MP3 players, which are great but not what I wanted. I also tried `ncpamixer`, which works but is way more complex than I need for just controlling playback.

`playerctl` does exactly what I want from the command line, but switching between terminal windows to type commands breaks my flow. So I built this - a simple TUI wrapper around playerctl that gives you playback controls without the complexity.

## Requirements

- Python 3.8+
- `playerctl` installed on your system
- A media player that supports MPRIS2

## Installation

### Installing playerctl

**Arch Linux:**

```bash
sudo pacman -S playerctl
```

**Ubuntu/Debian:**

```bash
sudo apt install playerctl
```

**Fedora:**

```bash
sudo dnf install playerctl
```

**macOS:**

```bash
brew install playerctl
```

### Setting up the project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/playerctl-tui.git
cd playerctl-tui
```

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # or venv/bin/activate.fish for fish shell
pip install -e .
```

## Usage

### Run in development mode

```bash
textual run --dev main.py
```

### Run with auto-reload (watch mode)

```bash
watchfiles "textual run --dev main.py"
```

### Run normally (after development)

```bash
python main.py
```

## Development Status

🚧 **Early development** - This project is actively being developed. Features and API may change.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Tech Stack

- **[Textual](https://github.com/Textualize/textual)** - Modern TUI framework
- **[playerctl](https://github.com/altdesktop/playerctl)** - MPRIS command-line controller
- **Python 3.8+**
