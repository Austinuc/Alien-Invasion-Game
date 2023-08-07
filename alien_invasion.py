import pygame
from settings.settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.screen_title)
	# screen.get_rect().topleft = (20,20)
	# print(screen.get_rect().topleft)
	

	# Make a ship.
	ship = Ship(screen,ai_settings)

	# make a group to store bullets
	bullets = Group()

	# make fleet of aliens
	aliens = Group()

	# aliens.add(Alien(screen,ai_settings))

	# Start the main loop for the game.
	while True:

		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)

		# Update ship position
		ship.update()

		# Update the bullet position
		bullets.update()

		# aliens.add(Alien(screen,ai_settings))
		# Get fleet of aliens
		gf.get_fleet_aliens(aliens, ai_settings, screen)

		# Update the alens position
		aliens.update()
		
		# Remove bullets that are no longer visible
		gf.update_bullets(bullets)

		# Redraw the screen during each pass through the loop.
		gf.update_screen(ai_settings,screen,ship,bullets, aliens)

run_game()
