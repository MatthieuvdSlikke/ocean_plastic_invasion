import pygame
from pygame.sprite import Sprite 

class Plastic(Sprite):
	"""A class to represent a single platic waste in the fleet"""
	def __init__(self, opi_set, screen):
		""" initialize the Plastic waste and set its starting position"""

		super(Plastic,self).__init__()
		self.screen = screen
		self.opi_set = opi_set

		#load the plastic rubbish and set its rect attribute 
		if opi_set.plastic_num == 1 :
			self.image = pygame.image.load('images/bouteille.bmp')
		elif opi_set.plastic_num == 2: 
			self.image = pygame.image.load('images/canette.bmp')
		elif opi_set.plastic_num == 3: 
			self.image = pygame.image.load('images/sac_plastique.bmp')

		self.rect = self.image.get_rect()

		#start each new plastic waste near the top left of the screen 
		self.rect.x = self.rect.width 
		self.rect.y = self.rect.height

		#store the plastic waste's exact position
		self.x = float(self.rect.x)

	def blitme(self):
		""" draw the plastic waste its current location."""
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		"""return true if plastic is at the edge of screen """
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		""" move the plastic to the right or left """
		self.x += (self.opi_set.plastic_speed_factor * self.opi_set.fleet_direction)
		self.rect.x = self.x
		



