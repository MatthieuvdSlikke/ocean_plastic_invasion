import sys
import pygame
from settings import Settings
from turtle import Turtle
import game_functions as gf
from pygame.sprite import Group
from game_stat import GameStats
from button import Button 
from scoreboard import Scoreboard


def run_game():

	#initialize game
	pygame.init() 

	opi_set = Settings()

	#create a screen with dimensions (width, hight)
	screen = pygame.display.set_mode((opi_set.screen_width,opi_set.screen_height))
	pygame.display.set_caption("Ocean Plastic Invasion")
	background_image = pygame.image.load('images/background.bmp').convert()

	#create an instance to store game statistics
	stats = GameStats(opi_set)

	# make a turtle , group of bullets and plastic rubbish
	turtle = Turtle(opi_set, screen)
	bullets = Group()
	plastics = Group()
	gf.create_fleet(opi_set,screen,turtle,plastics)

	#make the play button

	play_button = Button(opi_set,screen,"Play")
	game_over_button = Button(opi_set,screen,"Play Again")
	sb = Scoreboard(opi_set,screen,stats)

	# Start the main loop for the game 
	while True: 

		screen.blit(background_image, [0, 0])
		gf.check_events(opi_set,screen,stats, sb, turtle, plastics, bullets, play_button)
		if stats.game_active:
			turtle.update()
			gf.update_bullets(opi_set, screen,stats,sb, turtle, plastics, bullets)
			gf.update_plastic(opi_set, stats, sb, screen, turtle, plastics, bullets)
		gf.update_screen(opi_set,screen,stats, sb, turtle, plastics, bullets, play_button, game_over_button)



run_game()