# PYTHON_ Library

A personal Python library collection of useful functions for file management, 2D game algorithms, and data processing.

## Features

### 🗂️ File Management (`utils/files/`)
- JSON file operations
- File system utilities
- Cross-platform path handling
- File monitoring and validation

### 🎮 2D Game Systems (`syst_exp/`)
- **Raycast 2D**: Line-of-sight and visibility calculations
- **Pathfinding**: A* algorithm implementation
- **Map Generation**: Procedural map creation with enemies
- **Distance Calculations**: 2D geometry utilities

### 📊 Data Processing (`create_data/`)
- JSON dataset normalization
- Text preprocessing and tokenization
- Transformers integration (GPT-2)

### 🛠️ Utilities (`utils/`)
- Colored terminal output
- Error handling
- Development debugging tools

## Quick Start

```python
from utils.files.pyos import *
from syst_exp.raycast2D import get_visible_tiles2D
from create_data.create_data_set import normalize_json

# File operations
data = readfile_to_json("config.json")
create_json_file(data, "output.json")

# 2D game mechanics
visible_tiles = get_visible_tiles2D(bot_ia, grid, player_pos)

# Data processing
normalized_data = normalize_json("dataset.json")
```

## Dependencies

- Python 3.8+
- transformers
- termcolor

## Installation

```bash
pip install transformers termcolor
```
├── create_data 
│   └── create_data_set.py
├── main.py
├── main_test.py
├── syst_exp
│   ├── calculate_distance2D.py
│   ├── calculate_player_to_enemy_moves.py
│   ├── create_maps_with_diff_ennemies.py
│   ├── door_distance.py
│   ├── fill_all_map2D_diff_ennemies.py
│   ├── fill_map2D_origin.py
│   ├── get_visible_tiles.py
│   ├── handler_data
│   │   ├── init_data.py
│   │   └── player_pos.py
│   ├── list_to_2d_array.py
│   └── raycast2D.py
└── utils
    ├── files
    │   └── pyos.py
    ├── print
    │   ├── print_color.py
    │   └── print_error.py
    └── syst_os


