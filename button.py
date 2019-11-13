import pygame.font

class Button():

	def __init__(self, opi_set,screen,msg):
		"""Initialize button attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#set the dimensions and properties of the button
		self.width, self.height = 200, 200
		self.text_color = (255,255,255)
		self.font = pygame.font.Font("font/VerminVibesV-Zlg3.ttf", 80)

		#build the button's rect object and center it 
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center

		#the button message needs to be prepped only once
		self.prep_msg(msg)

	def prep_msg(self, msg):
		""" Turn message into a rendered image and center text on the button"""
		self.msg_image = self.font.render(msg,True,self.text_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center =self.rect.center

	def draw_button(self):
		""" draw blank button and then draw message"""
		self.screen.blit(self.msg_image, self.msg_image_rect)
