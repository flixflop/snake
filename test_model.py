from game_logic import GameState

class TestGameState:

	game_state = GameState(
		grid_size=20, 
		snake_start=(10, 10)
		)
	
	def test_generate_snack(self):
		assert self.game_state.snack != self.game_state.snake

	def test_move_snake(self):
		self.game_state.direction = "Left"
		self.game_state.move_snake()
		assert self.game_state.snake[0] == (9, 10)