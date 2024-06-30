# Snake
This is a try at a snake - or should it be python? - game.

# Todo

# Setup
### Install Python 3.10 with pyenv
Installation is tested for a WSL system using ubunt 22.4 and python 3.10.13
Using pyenv we install python 3.10.13 in our system by
```
pyenv install 3.10.13
```
Next, we setup a virtual environment in the project folder `~/.../snake`, specifying the python version and the virtual environment name. 
```
pyenv virtualenv 3.10.13 snake
```
Before installing any dependencies, we upgrade pip
```
pyenv activate snake
python -m pip install --upgrade pip
```


# Todo
### Version one in tkinter
- Draw a game board with tkinter
- Draw a pixel in that board
- Let the pixel move around by clicking the arrow buttons

### Game description
- The snake game has only two end conditions: perfect game, i.e. the snake fills the entire screen or the snake collides with its own body
- Variation: If the snake collides with the wall, it could also be considered as a game ending collision or we wrap around
- If the snake eats a snack, a segment is added to its body