import sys
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from settings.settings import Settings

def check_events(ai_settings, screen, ship:Ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings:Settings, screen, ship:Ship, bullets):
    """Respond to keypresses events."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
            sys.exit()

def check_keyup_events(event, ship:Ship):
    """Respond to keypresses events."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = False
        
            

def update_screen(ai_settings, screen, ship:Ship, bullets, aliens):
    """Update images on the screen and flip to the new screen"""

    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    for alien in aliens.sprites():
        alien.blitme()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.fire()


    # make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings, screen, ship, bullets):
    # Redraw all bullets behind ship and aliens.
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_fleet_aliens(aliens, ai_settings, screen):
    # print(len(aliens))
    if len(aliens) < ai_settings.bullet_limit + 5:
        alien = Alien(screen, ai_settings)
        aliens.add(alien)
        alien = Alien(screen, ai_settings,2)
        aliens.add(alien)
        alien = Alien(screen, ai_settings,3)
        aliens.add(alien)
        alien = Alien(screen, ai_settings,4)
        aliens.add(alien)

