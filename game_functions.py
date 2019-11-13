import sys 
import pygame
from bullet import Bullet
from plastic import Plastic 
from time import sleep
from random import randint

def check_events(opi_set,screen,stats, sb, turtle, plastics, bullets, play_button):
	""" respond to keypresses and mouse events"""

	# the game is controlled by events in the while loop
	# an event is an action such pressing the keyboard or moving the mouse 
	for event in pygame.event.get(): #event loop
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_key_down_events(event,opi_set,screen,stats, turtle, plastics, bullets, play_button)
		elif event.type == pygame.KEYUP:
			check_key_up_events(event,turtle)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x , mouse_y = pygame.mouse.get_pos()
			check_play_button(opi_set,screen,stats, sb, turtle, plastics, bullets, play_button,mouse_x,mouse_y)

def check_play_button(opi_set,screen,stats, sb, turtle, plastics, bullets, play_button,mouse_x,mouse_y):
	"""start a new game when the player clicks play"""
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		#reset the game settings
		opi_set.initialize_dynamic_settings()
		# hide the mouse cursor
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True

		#reset the scoreboard images
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_turtles()

		#empty the list of platics and bullets
		plastics.empty()
		bullets.empty()

		#create a new fleet and center the ship.
		create_fleet(opi_set,screen, turtle, plastics)
		turtle.center_turtle()


def check_key_down_events(event,opi_set,screen,stats, turtle, plastics, bullets, play_button):

	""" respond to key presses"""
	if event.key == pygame.K_RIGHT:
		#move the ship to the right
		turtle.moving_right = True
	elif event.key == pygame.K_LEFT:
		turtle.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(opi_set,screen, turtle, bullets)
	elif event.key == pygame.K_q:
		sys.exit()


def check_key_up_events(event,turtle):

	""" respond to key releases"""
	if event.key == pygame.K_RIGHT:
		turtle.moving_right = False
	elif event.key == pygame.K_LEFT:
		turtle.moving_left = False


def update_screen (opi_set,screen,stats, sb, turtle, plastics, bullets, play_button, game_over_button):
	#redraw the screen during each pass through the loop
	#screen.fill(opi_set.bg_color)
	#redraw all bullets behind turtle and platic bags
	for bullet in bullets:
		bullet.draw_bullet()
	turtle.blitme()
	plastics.draw(screen)

	#draw the scoreboard
	sb.show_score()

	#draw the play button
	if not stats.game_active and stats.turtles_left == 0 : 
		game_over_button.draw_button()
		pygame.mouse.set_visible(True)
	elif not stats.game_active and stats.turtles_left>0 :
		play_button.draw_button()

	# Make the most recently drawn screen visible, gives the illusion of smooth mouvement
	pygame.display.flip() 

def fire_bullet(opi_set,screen, turtle, bullets):
	#create a new bullet and add it to the bullets group
		if len(bullets)< opi_set.bullets_allowed:
			new_bullet = Bullet(opi_set,screen,turtle)
			bullets.add(new_bullet)


def update_bullets(opi_set, screen,stats,sb, turtle, plastics, bullets):
		bullets.update()
		#getting rid of old bullets
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		#check for bullet collision with alien and immediately eliminate both
		check_bullet_plastic_collision(opi_set, screen,stats,sb, turtle, plastics, bullets)


def check_bullet_plastic_collision(opi_set, screen,stats,sb, turtle, plastics, bullets):
		
		collision = pygame.sprite.groupcollide(bullets,plastics, True, True)

		if collision: 
			for plastics in collision.values():
				stats.score += opi_set.plastic_points * len(plastics)
				sb.prep_score()
			check_high_score(stats,sb)

		if len(plastics) == 0:
			#Destroy existing bullets and create and create new fleet
			bullets.empty()
			create_fleet(opi_set,screen, turtle, plastics)
			opi_set.increase_speed()

			#increase level
			stats.level += 1
			sb.prep_level()

def get_number_plastics_x(opi_set,plastic_width):
	""" determine the number of plastic waistes that will fit in a row"""
	available_space_x = opi_set.screen_width - 2 * plastic_width
	plastic_number_x =  int(available_space_x/ (2 *plastic_width))
	return plastic_number_x

def get_number_rows(opi_set,turtle_height, plastic_height):
	""" determine the number of rows of plastic rubbish that fit on the screen"""
	available_space_y = (opi_set.screen_height - (3 * plastic_height)-turtle_height)
	number_rows = int(available_space_y/(2*plastic_height))
	return number_rows


def create_plastic(opi_set,screen,plastics, plastic_number,row_number):
	"""create a waiste and place in a row"""
	plastic = Plastic (opi_set,screen)
	plastic_width = plastic.rect.width
	plastic_height = plastic.rect.height
	plastic.x = plastic_width + 2 * plastic_width * plastic_number
	plastic.rect.x = plastic.x
	plastic.rect.y = plastic_height + 2 * plastic_height * row_number
	plastics.add(plastic)

def create_fleet(opi_set,screen, turtle, plastics):
	""" create a full fleet of plastic rubbish"""
	#create a plastic waste and find the number of plastic wastes
	plastic = Plastic (opi_set,screen)
	plastic_number_x = get_number_plastics_x(opi_set,plastic.rect.width)
	number_rows = get_number_rows(opi_set, turtle.rect.height, plastic.rect.height)
	#create the first row of plastic rubbish
	for row_number in range(number_rows):
		for plastic_number in range(plastic_number_x):
			opi_set.plastic_num = randint(1,3)
			create_plastic(opi_set,screen,plastics, plastic_number,row_number)
			
def update_plastic(opi_set,stats, sb, screen, turtle, plastics, bullets):
	"""check if fleet is at and edge and update the position of all plastic wastes"""
	check_fleet_edges(opi_set, plastics)
	plastics.update()

	#look for turtle_plastic collision
	if pygame.sprite.spritecollideany(turtle,plastics):
		turtle_hit(opi_set, stats,sb,screen,turtle,plastics,bullets)

	#look for plastics hitting the bottom of the screen 
	check_plastics_bottom(opi_set,stats,sb,screen,turtle,plastics,bullets)

def check_fleet_edges(opi_set, plastics):
	""" respond  appropriately if any plastic wastes have reached an edge"""
	for plastic in plastics.sprites(): 
		if plastic.check_edges():
			change_fleet_direction(opi_set,plastics)
			break

def change_fleet_direction(opi_set,plastics):
	"""drop the entire fleet and change its direction"""
	for plastic in plastics.sprites(): 
		plastic.rect.y += opi_set.fleet_drop_speed	
	opi_set.fleet_direction *= -1

def turtle_hit(opi_set,stats,sb,screen,turtle,plastics,bullets):
	""" respond to turtle being hit by plastic"""
	if stats.turtles_left > 0:
		#decrement turtle_lefts
		stats.turtles_left -= 1
		sb.prep_turtles()

		#empty the list of plastics and bullets
		plastics.empty()
		bullets.empty()

		#create a new fleet and center the turtle
		create_fleet(opi_set,screen,turtle,plastics)
		turtle.center_turtle()

		#pause
		sleep(0.5)
	else:
		stats.game_active = False

def check_plastics_bottom(opi_set,stats,sb,screen,turtle,plastics,bullets):
	""" check if any plastics have reached the bottom of the screen"""

	screen_rect = screen.get_rect()
	for plastic in plastics.sprites():
		if plastic.rect.bottom >= screen_rect.bottom:
			#treat this the same as if the turtle got hit 
			turtle_hit(opi_set,stats, sb, screen,turtle,plastics,bullets)
			break

def check_high_score(stats,sb):
	""" check to see if there is a new score"""
	if stats.score > stats.high_score:
		stats.high_score =stats.score
		sb.prep_high_score()






