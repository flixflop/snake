from random import randint

class GameOver(Exception):
    pass

class GameState:

    def __init__(self, grid_size:int, snake_start:tuple) -> None:
        # We are using a tuple to store the game coordinates
        # Maybe in the futre, we can make this a point, so we can define math operations like
        # subtraction propertly.
        # Another todo could be to use a double-ended queue as a data structure.
        self.grid_size = grid_size
        self.snake = [snake_start]
        self.snack = self.generate_snack()
        self.direction = None
        self.score = 0
        self.movements = {
            "Left" : (-1, 0),
            "Right" : (1, 0),
            "Up" : (0, -1),
            "Down" : (0, 1)
        }

    def generate_snack(self):
        while True:
            snack_x = randint(0, self.grid_size)
            snack_y = randint(0, self.grid_size)
            snack = (snack_x, snack_y)
            if snack not in self.snake:
                return snack
            
    def set_direction(self, direction):
        if direction == "Left" and self.direction != "Right":
            self.direction = direction
        elif direction == "Right" and self.direction != "Left":
            self.direction = direction
        if direction == "Up" and self.direction != "Down":
            self.direction = direction
        if direction == "Down" and self.direction != "Up":
            self.direction = direction   

    def move_snake(self):
        if self.direction:
            head_x, head_y = self.snake[0]
            dx, dy = self.movements[self.direction]
            new_head = (head_x + dx, head_y + dy)

            # snack eating & movement logic
            if new_head == self.snack:
                self.snake = [new_head] + self.snake
                self.score += 1
                self.snack = self.generate_snack()
            else:
                self.snake = [new_head] + self.snake[:-1]

            # wall collision
            if (head_x < 0 or head_x > self.grid_size or
                head_y < 0 or head_y > self.grid_size):
                raise GameOver("Game Over: Collision with wall!")
            
            # self collision
            if new_head in self.snake[1:]:
                raise GameOver("Game Over: Collison with self!")