# rpg_pybot

Description. 
The package rpg_pybot is used to:

	dice:
		roll	
	players:
		Player

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rpg_pybot

```bash
pip install rpg_pybot
```

## Usage

```python
from rpg_pybot.dice import roll, players
roll.roll()
player1 = player.Player("name")
player2 = player.Player("name")
player1.player_data()
player1.set_char_class([0-3])
player1.attack(player2)

```

## Author
Lucas Mateus da Silva

## License
[MIT](https://choosealicense.com/licenses/mit/)