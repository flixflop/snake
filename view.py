import tkinter as tk
from model import GameState, GameOver

CHARACTER_SIZE = 20
MOVE_DELAY = 125  # Movement delay in milliseconds
GRID_SIZE = 11

class TkinterSnakeGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(
            root, 
            width=GRID_SIZE * CHARACTER_SIZE + CHARACTER_SIZE, 
            height=GRID_SIZE * CHARACTER_SIZE + CHARACTER_SIZE, 
            bg="white"
        )
        self.canvas.pack()
        
        # Initialize game state
        self.game_state = GameState(grid_size=GRID_SIZE, snake_start=(GRID_SIZE // 2, GRID_SIZE // 2))
        
        # Bind key presses
        self.root.bind("<Left>", self.change_direction)
        self.root.bind("<Right>", self.change_direction)
        self.root.bind("<Up>", self.change_direction)
        self.root.bind("<Down>", self.change_direction)
        
        # Start the game loop
        self.update()

    def change_direction(self, event):
        direction = event.keysym
        if direction in ["Left", "Right", "Up", "Down"]:
            self.game_state.set_direction(direction)

    def update(self):
        try:
            self.game_state.move_snake()
            self.render_game()
            self.root.after(MOVE_DELAY, self.update)
        except GameOver as e:
            print(e)
            self.game_over()

    def render_game(self):
        self.canvas.delete("all")
        
        # Draw snake
        for segment in self.game_state.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x * CHARACTER_SIZE, 
                y * CHARACTER_SIZE,
                (x + 1) * CHARACTER_SIZE, 
                (y + 1) * CHARACTER_SIZE,
                fill="blue"
            )
        
        # Draw snack
        sx, sy = self.game_state.snack
        self.canvas.create_rectangle(
            sx * CHARACTER_SIZE, 
            sy * CHARACTER_SIZE,
            (sx + 1) * CHARACTER_SIZE, 
            (sy + 1) * CHARACTER_SIZE,
            fill="red"
        )

    def game_over(self):
        # Display a game over message
        self.canvas.create_text(
            (GRID_SIZE * CHARACTER_SIZE) // 2,
            (GRID_SIZE * CHARACTER_SIZE) // 2,
            text="Game Over",
            font=("Helvetica", 24),
            fill="red"
        )


