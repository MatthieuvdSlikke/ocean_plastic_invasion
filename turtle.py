import pygame
from pygame.sprite import Sprite

class Turtle(Sprite):

	def __init__(self,opi_set,screen):
		""" initialize the turtle and set its starting position"""

		super(Turtle,self).__init__()
		self.screen = screen
		self.opi_set =opi_set

		#load the turtle image and get its rect, it turns the image
		#into a rectangle turning the images or screen into a rectangle 
		#makes it easier to manipulate as we can now give the image x 
		#and y coordinates.The (0,0) coordinate is represented by the 
		#top left of the image

		self.image = pygame.image.load('images/tortue.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#start each new turtle at the bottom center of the screen

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#store a decimal value for the ship center
		self.center = float(self.rect.centerx)

		#we set a movement flag to smoot the game and set it to false
		self.moving_right = False
		self.moving_left = False


	def blitme(self):

		""" Draw the turtle at its current location."""
		self.screen.blit(self.image,self.rect)


	def update(self):

		""" update the turtle's position based on the mouvement flag"""

		if self.moving_right and self.moving_left:
			self.rect.centerx += 0
		
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.opi_set.turtle_speed_factor
		
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.opi_set.turtle_speed_factor

		#update rect oject from self.center, only the integer part will be stored 
		self.rect.centerx = self.center

	def center_turtle(self):
		"""center the turtle on the screen"""
		self.center = self.screen_rect.centerx



