from random import randint

class GameOver(Exception):
    pass

class GameState:

    def __init__(self, grid_size:int, snake_start:tuple) -> None:
        # We are using a tuple to store the game coordinates
        # Maybe in the futre, we can make this a point, so we can define math operations like
        # subtraction propertly.
        self.grid_size = grid_size
        self.snake = [snake_start]
        self.snack = self.generate_snack()
        self.direction = None

    def generate_snack(self):
        while True:
            snack_x = randint(0, self.grid_size)
            snack_y = randint(0, self.grid_size)
            snack = (snack_x, snack_y)
            if snack not in self.snake:
                return snack

    def move_snake(self):
        if self.direction:
            head_x, head_y = self.snake[0]
            if self.direction == "Left":
                head_x -= 1
            elif self.direction == "Right":
                head_x += 1
            elif self.direction == "Down":
                head_y += 1
            elif self.direction == "Up":
                head_y -= 1
            new_head = (head_x, head_y)

            # snack eating & movement logic
            if new_head == self.snack:
                self.snake = [new_head] + self.snake
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