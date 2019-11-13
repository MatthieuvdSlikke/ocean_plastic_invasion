class Settings():
	""" A class to store all settings for Ocean Plastic Invasion."""

	def __init__(self):

		""" initialize the game's settings."""

		#Screen settings
		self.screen_width = 1200
		self.screen_height = 700
		
		#turtle settings
		self.turtle_limit = 3

		#bullet settings
		self.bullet_radius = 6
		self.bullet_width = self.bullet_radius*2
		self.bullet_height = self.bullet_radius*2
		self.bullet_color = 255,250,250
		self.bullets_allowed = 4

		#plastic rubbish settings
		self.fleet_drop_speed = 10
		#fleet direction of 1 represents right ; -1 represents left
		self.fleet_direction = 1

		#change the plastic object
		self.plastic_num  = 1

		#how quickly the game speeds up
		self.speedup_scale = 1.1

		#scoring
		self.plastic_points = 50

		#how quickly the plastic point values increase
		self.scoring_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings (self):
		""" Initialize settings that change throught the game"""

		self.turtle_speed_factor = 10
		self.bullet_speed_factor = 6
		self.plastic_speed_factor = 5

		#fleet direction 
		self.fleet_direction = 1

	def increase_speed(self):
		"""increase speed settings and plastic point values"""
		self.bullet_speed_factor *= self.speedup_scale
		self.plastic_speed_factor *= self.speedup_scale

		self.plastic_points = int (self.plastic_points * self.scoring_scale)
	


