# Game of Life
This is a simple [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) implementation in honour of John Conway.

## Install
> `$pip install -r requirements.txt` <br/>
> `$python board.py -b 5`

## Usage
The program has a CLI to choose from different pre-set boards with the most
common patterns.

- `board.py -h          Prints a help message`
- `board.py -b size     Creates a blinker board`
- `board.py -t size     Creates a toad board`
- `board.py -e size     Creates a beacon board`
- `board.py -g size     Creates a glider board`
- `board.py -f path     Reads a board from a given file`

## Yet to come
A GUI that let you set your own board.
