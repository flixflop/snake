import tkinter as tk
from random import randint
from time import sleep


def snake():
    pass

def register_move():
    """
    Register a change in direction with a specific position
    on the game board.
    """
    pass

def eat_snack():
    pass 

def generate_snack(game_board):
    """
    Must create a snack at a valid position inside the game board.
    parameters
    ----------
    :game_board: 2D list
    """
    height, width = len(game_board), len(game_board[0])
    print(width, height)
    game_board[randint(2, height - 1)][randint(2, width - 1)] = 999
    return 


def generate_board(width, height):
    """
    Generate a game board (2D grid) with a specified width and height
    *- - - - - - *
    |	         |
    | 			 |
    |			 |
    *- - - - - - *

    [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    """
    board = []
    for h in range(height):
        if h == 0 or h == height - 1:
            board.append([1 for w in range(width)])
        else:
            row = [1] + [0 for w in range(width -2)] + [1]
            board.append(row)
    
    return board

# Constants for character size and movement step
CHARACTER_SIZE = 20
MOVEMENT_STEP = 10
MOVE_DELAY = 250  # Movement delay in milliseconds for continuous movement
WIDTH = 400
HEIGHT = 400

class CharacterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Character Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        # Create the character as a rectangle
        self.character = self.canvas.create_rectangle(
            WIDTH // 2, 
            HEIGHT // 2, 
            (WIDTH // 2) + CHARACTER_SIZE, 
            (HEIGHT // 2) + CHARACTER_SIZE,
            fill="blue"
        )
        # Create a game border
        self.border = self.canvas.create_rectangle(
            5,
            5,
            WIDTH - 5, 
            HEIGHT - 5,
            outline="black"
        )
        # Generate snack
        self.snack = self.generate_snack()

        # Current direction of movement
        self.current_direction = None

        # Bind key press events
        self.root.bind("<Left>", self.start_moving)
        self.root.bind("<Right>", self.start_moving)
        self.root.bind("<Up>", self.start_moving)
        self.root.bind("<Down>", self.start_moving)

        self.movements = {
            "Left" : (-MOVEMENT_STEP, 0),
            "Right" : (MOVEMENT_STEP, 0),
            "Up" : (0, -MOVEMENT_STEP),
            "Down" : (0, MOVEMENT_STEP)
        }

        # Start the movement loop
        self.move_character()

    def start_moving(self, event):
        # Set the current direction based on the key pressed
        self.current_direction = event.keysym

    def move_character(self):
        if self.current_direction:
            self.canvas.move(self.character, *self.movements[self.current_direction])

        r_x0, r_y0, r_x1, r_y1 = self.canvas.coords(self.character)
        b_x0, b_y0, b_x1, b_y1 = self.canvas.coords(self.border)
        if r_x0 <= b_x0:
            self.canvas.move(self.character, b_x1 - CHARACTER_SIZE, 0)
        if r_x1 >= b_x1:
            self.canvas.move(self.character, (b_x1 - CHARACTER_SIZE) * (-1), 0)
        if r_y0 <= b_y0:
            self.canvas.move(self.character, 0, (b_y1 - CHARACTER_SIZE))
        if r_y1 >= b_y1:
            self.canvas.move(self.character, 0, (b_y1 - CHARACTER_SIZE) * (-1))

        # Schedule the next move
        self.root.after(MOVE_DELAY, self.move_character)

    def generate_snack(self):
        # Get border coordinates
        b_x0, b_y0, b_x1, b_y1 = self.canvas.coords(self.border)
        s_x0 = randint(b_x0, b_x1 - CHARACTER_SIZE)
        s_y0 = randint(b_y0, b_y1 - CHARACTER_SIZE)
        # Create the character as a rectangle
        self.snack = self.canvas.create_rectangle(
            s_x0,
            s_y0,
            s_x0 + CHARACTER_SIZE,
            s_y0 + CHARACTER_SIZE,
            fill="red"
        )
        

if __name__ == "__main__":
    root = tk.Tk()
    game = CharacterGame(root)
    root.mainloop()