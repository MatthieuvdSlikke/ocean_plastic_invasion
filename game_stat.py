class GameStats():
	""" Track Statistics for the game"""

	def __init__(self, opi_set):
		""" initialize stats"""
		self.opi_set = opi_set
		self.reset_stats()
		self.game_active = False 

		#high score should never be reset
		self.high_score = 0 

	def reset_stats(self):
		"""Initialize statistics that can change during the game"""
		self.turtles_left = self.opi_set.turtle_limit
		self.score = 0 
		self.level = 1
		