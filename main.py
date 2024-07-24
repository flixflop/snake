import tkinter as tk
from random import randint, choice
from time import sleep

# Constants for character size and movement step
CHARACTER_SIZE = 20
MOVEMENT_STEP = CHARACTER_SIZE
MOVE_DELAY = 250  # Movement delay in milliseconds for continuous movement
A = 21
WIDTH = A * CHARACTER_SIZE
HEIGHT = A * CHARACTER_SIZE

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        # Create the character as a rectangle
        self.snake = [self.canvas.create_rectangle(
            A // 2 * CHARACTER_SIZE, 
            A // 2 * CHARACTER_SIZE, 
            A // 2 * CHARACTER_SIZE + CHARACTER_SIZE, 
            A // 2 * CHARACTER_SIZE + CHARACTER_SIZE,
            fill="blue"
        )]

        # Create a game border
        self.border = self.canvas.create_rectangle(
            CHARACTER_SIZE,
            CHARACTER_SIZE,
            WIDTH - CHARACTER_SIZE, 
            HEIGHT - CHARACTER_SIZE,
            outline="black"
        )
        # Randomly generate a snack.
        self.generate_snack()

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
            #for segment in self.snake:
            x0, y0, x1, y1 = self.canvas.coords(self.snake[0])
            dx, dy = self.movements[self.current_direction]
            
            self.snake = [self.canvas.create_rectangle(
                x0 + dx,
                y0 + dy,
                x1 + dx, 
                y1 + dy,
                fill="blue"
                )] + self.snake
            self.canvas.delete(self.snake[-1])
            self.snake.pop()

        # snack eating
        if self.canvas.coords(self.snack) == self.canvas.coords(self.snake[0]):

            # get snack coordinates
            sx0, sy0, sx1, sy1 = self.canvas.coords(self.snack)
            sdx, sdy = self.movements[self.current_direction]
            # eat snack and spawn a new one.
            self.canvas.delete(self.snack)
            self.generate_snack()
            # create a new rectangel.
            self.snake = [
                self.canvas.create_rectangle(
                    sx0 + sdx,
                    sy0 + sdy,
                    sx1 + sdx, 
                    sy1 + sdy,
                    fill="blue"
                    )
                ] + self.snake

        # wrap around conditions
        # r_x0, r_y0, r_x1, r_y1 = self.canvas.coords(self.snake[0])
        # b_x0, b_y0, b_x1, b_y1 = self.canvas.coords(self.border)
        # if r_x0 < b_x0:
        #     self.canvas.move(self.snake, b_x1 - CHARACTER_SIZE, 0)
        # if r_x1 > b_x1:
        #     self.canvas.move(self.snake, (b_x1 - CHARACTER_SIZE) * (-1), 0)
        # if r_y0 < b_y0:
        #     self.canvas.move(self.snake, 0, (b_y1 - CHARACTER_SIZE))
        # if r_y1 > b_y1:
        #     self.canvas.move(self.snake, 0, (b_y1 - CHARACTER_SIZE) * (-1))

        # Schedule the next move
        self.root.after(MOVE_DELAY, self.move_character)

    def generate_snack(self):
        # Get border coordinates.
        b_x0, b_y0, b_x1, b_y1 = self.canvas.coords(self.border)
        # Random x0 and y0 inside the border.
        s_x0 = choice([i for i in range(int(b_x0), int(b_x1), CHARACTER_SIZE)])
        s_y0 = choice([i for i in range(int(b_y0), int(b_y1), CHARACTER_SIZE)])
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
    game = SnakeGame(root)
    root.mainloop()