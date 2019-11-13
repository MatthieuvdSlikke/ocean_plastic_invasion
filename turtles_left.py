import pygame
from pygame.sprite import Sprite

class Turtles_left(Sprite):

	def __init__(self,opi_set,screen):

		super(Turtles_left,self).__init__()
		self.screen = screen
		self.opi_set =opi_set

		self.image = pygame.image.load('images/tortues.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

	def blitme(self):

		""" Draw the turtle at its current location."""
		self.screen.blit(self.image,self.rect)