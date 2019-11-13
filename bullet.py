import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" a class to manage bullets fired from the ship"""

	def __init__(self, opi_set,screen,turtle):
		"""create a bullet object at the ship's current position"""

		#the sprite class helps you group related elements in your game.
		super(Bullet,self).__init__()
		self.screen = screen

		# create a bullet rect at (0,0) and then set correct position
		self.rect = pygame.Rect((0,0), (opi_set.bullet_width, opi_set.bullet_height)) #creates a bullet from scratch
		self.rect.centerx = turtle.rect.centerx
		self.rect.top = turtle.rect.top #set the bullet at the top of the turtle

		#self.circle.centerx = turtle.rect.centerx
	
		#store the bullet's position as a decimal value
		self.y = float(self.rect.y)
		self.radius = opi_set.bullet_radius
		self.color = opi_set.bullet_color
		self.speed_factor = opi_set.bullet_speed_factor

	def update(self):
		"""move the bullet up to the screen"""

		#update the decimal position of the bullet and the rect position
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		""" draw the bullet"""
		#pygame.draw.circle(self.screen,self.color,self.rect)
		pygame.draw.circle(self.screen,self.color,(self.rect.x,self.rect.y), self.radius)

		



