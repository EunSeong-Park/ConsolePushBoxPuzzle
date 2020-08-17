# Console Push Box Puzzle (incomplete) 
The purpose of [Push box Puzzle](https://en.wikipedia.org/wiki/Sokoban) (a.k.a. Sokoban, warehouse keeper) is storing all of box to hole.

# How to Use
It requires Python 3 and keyboard library:

```
$ pip3 install keyboard 
```

And then run `main.py` with gameboard file. If argument is omitted, use map.txt as default gameboard
```
$ main.py [gameboard].txt
```

- `W`: Up
- `A`: Left
- `S`: Down
- `D`: Right
- `Q`: Quit
- `R`: Restart

# How to Make Gameboard
Gameboard consists of floor(`.`), wall(`#`), box(`B`), hole(`O`), and unique player(`@`). You should follow these:

- Gameboard must be rectangular
- Set board size to 40 columns (not mandatory, but recommended)
- Too long map makes it hard to see
- The number of boxes must be same with that of holes
- There must be only one player

