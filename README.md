# DevDash 🛠️

> Your ultimate local-first developer dashboard. All-in-one workspace for power users.

[![PyPI](https://img.shields.io/pypi/v/devdash)](https://pypi.org/project/devdash/)
[![License](https://img.shields.io/github/license/HoraceDong31415-bit/devdash)](LICENSE)
[![Stars](https://img.shields.io/github/stars/HoraceDong31415-bit/devdash)](https://github.com/HoraceDong31415-bit/devdash)

## Why DevDash?

Because developers need one unified workspace, not 10 different apps.

### Features

- 📋 **Clipboard Manager** - Auto-save, search, categorize, favorites
- 📝 **Snippets** - 50+ languages, syntax detection, quick copy
- 📓 **Notes** - Markdown-style with tags, wiki-links
- ⏱️ **Time Tracking** - Project-based, statistics
- 🔖 **Bookmarks** - Categorized, quick open
- ⚡ **Commands** - Save & run frequent commands

## Quick Start

```bash
# Install
pip install devdash

# Initialize
devdash init

# Clipboard
devdash clip save "important text"
devdash clip list
devdash clip search "query"

# Snippets  
devdash snip add "my-snippet" "echo hello" --lang bash
devdash snip list --lang python

# Notes
devdash note add "Project Ideas" "Build something cool"

# Time
devdash time start "coding"
devdash time stop
devdash time stats

# Dashboard
devdash dash
```

## Installation

```bash
# From PyPI
pip install devdash

# Or from source
git clone https://github.com/HoraceDong31415-bit/devdash.git
cd devdash
pip install -e .
```

## Commands

### Clipboard
| Command | Description |
|---------|-------------|
| `devdash clip save [text]` | Save to history |
| `devdash clip list` | Show history |
| `devdash clip search <query>` | Search |
| `devdash clip paste <idx>` | Paste from history |
| `devdash clip stats` | Show statistics |

### Snippets
| Command | Description |
|---------|-------------|
| `devdash snip add <name> <code>` | Add snippet |
| `devdash snip list` | List all |
| `devdash snip get <idx>` | Copy to clipboard |
| `devdash snip search <query>` | Search |

### Notes
| Command | Description |
|---------|-------------|
| `devdash note add <title> <content>` | Create note |
| `devdash note list` | List notes |
| `devdash note get <idx>` | View note |

### Time Tracking
| Command | Description |
|---------|-------------|
| `devdash time start <project>` | Start timer |
| `devdash time stop` | Stop timer |
| `devdash time list` | Show entries |
| `devdash time stats` | Statistics |

## Configuration

Config file: `~/.devdash/config.json`

```json
{
  "clip_limit": 500,
  "default_lang": "python",
  "theme": "dark"
}
```

## Requirements

- Python 3.8+
- macOS / Linux / Windows

## License

MIT
