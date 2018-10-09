# game_functions.py
# Created by: John Gawlik
# Campus ID: 889752424
# Due: September 21st, 2018
########################################################################################################################
import sys
import pygame
from bullet import Bullet
from alien import AlienTop
from alien import AlienMiddle
from alien import AlienBottom
from alien import Ufo
from bunker import Bunker
from time import sleep
import random


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions"""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        """aliens.sprite.blow_up()"""
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def check_events(ai_settings, screen, stats, sb, play_button, high_scores_button, ship, aliens, ufo, bullets, bunkers):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, ufo, bullets, mouse_x, mouse_y, bunkers)
            check_high_scores_button(ai_settings, screen, stats, sb, play_button, high_scores_button, ship, aliens, ufo,
                                     bullets, mouse_x, mouse_y)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_high_scores_button(ai_settings, screen, stats, sb, play_button, high_scores_button, ship, aliens, ufo, bullets, mouse_x, mouse_y):
    button_clicked = high_scores_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        show_high_scores_screen(ai_settings, screen, play_button)


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, ufo, bullets, mouse_x, mouse_y, bunkers):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        pygame.mixer.init()
        pygame.mixer.music.load('sounds/Space_Invaders_Theme_Song.wav')
        pygame.mixer.music.play(-1)
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        create_bunkers_fleet(ai_settings, screen, bunkers)
        ship.center_ship()
        ufo.center_ufo()


def create_alien_top(ai_settings, screen, aliens, alien_number, row_number):
    alien = AlienTop(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 0.7 * alien.rect.height * row_number
    aliens.add(alien)


def create_alien_middle(ai_settings, screen, aliens, alien_number, row_number):
    alien = AlienMiddle(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 0.7 * alien.rect.height * row_number
    aliens.add(alien)


def create_alien_bottom(ai_settings, screen, aliens, alien_number, row_number):
    alien = AlienBottom(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 0.7 * alien.rect.height * row_number
    aliens.add(alien)


def create_bunker(ai_settings, screen, bunkers, bunker_number):
    bunker = Bunker(ai_settings, screen)
    bunker_width = bunker.rect.width
    bunker.x = bunker_width + 2 * bunker_width * bunker_number
    bunker.rect.x = bunker.x
    bunker.rect.y = bunker.rect.height + 7 * bunker.rect.height
    bunkers.add(bunker)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = AlienBottom(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        if row_number < 1:
            for alien_number in range(number_aliens_x):
                create_alien_top(ai_settings, screen, aliens, alien_number, row_number)
        if 1 <= row_number <= 2:
            for alien_number in range(number_aliens_x):
                create_alien_middle(ai_settings, screen, aliens, alien_number, row_number)
        if row_number >= 3:
            for alien_number in range(number_aliens_x):
                create_alien_bottom(ai_settings, screen, aliens, alien_number, row_number)


def create_bunkers_fleet(ai_settings, screen, bunkers):
    bunker = Bunker(ai_settings, screen)
    number_bunkers_x = get_number_bunkers_x(ai_settings, bunker.rect.width)

    for bunker_number in range(number_bunkers_x):
        create_bunker(ai_settings, screen, bunkers, bunker_number)


def draw_space_text(text, font, screen, x, y):
    text_obj = font.render(text, 1, (255, 255, 255))
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)


def draw_invaders_text(text, font, screen, x, y):
    text_obj = font.render(text, 1, (128, 255, 0))
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_bunkers_x(ai_settings, bunker_width):
    available_space_x = ai_settings.screen_width - 2 * bunker_width
    number_bunkers_x = int(available_space_x / (2 * bunker_width))
    return number_bunkers_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (2 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    ship.hit = True

    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # Update Scoreboard.
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause.
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def show_high_scores_screen(ai_settings, screen, play_button):
    screen.fill(ai_settings.start_screen_bg_color)
    font = pygame.font.SysFont('freesansbold.ttf', 50)
    high_score_file = open("high_scores.txt", "r")
    for line in high_score_file:
        draw_space_text(line, font, screen, (ai_settings.screen_width / 2), ((ai_settings.screen_height / 4) - 90))
    play_button.draw_button()
    pygame.display.update()


def show_start_screen(ai_settings, screen, play_button, high_scores_button):
    screen.fill(ai_settings.start_screen_bg_color)
    space_font = pygame.font.SysFont('freesansbold.ttf', 300)
    invaders_font = pygame.font.SysFont('freesansbold.ttf', 200)
    points_font = pygame.font.SysFont('freesansbold.ttf', 70)
    draw_space_text('SPACE', space_font, screen, (ai_settings.screen_width / 2), ((ai_settings.screen_height / 4) - 90))
    draw_invaders_text('INVADERS', invaders_font, screen, (ai_settings.screen_width / 2), ((ai_settings.screen_height / 2) - 140))
    draw_space_text('= 50 pts', points_font, screen, ((ai_settings.screen_width / 2) + 100), ((ai_settings.screen_height / 2) - 10))
    draw_space_text('= 50 pts', points_font, screen, ((ai_settings.screen_width / 2) + 100), ((ai_settings.screen_height / 2) + 40))
    draw_space_text('= 50 pts', points_font, screen, ((ai_settings.screen_width / 2) + 100), ((ai_settings.screen_height / 2) + 90))
    draw_space_text('= ???', points_font, screen, ((ai_settings.screen_width / 2) + 72), ((ai_settings.screen_height / 2) + 140))
    alien_top = AlienTop(ai_settings, screen)
    alien_top.rect.x = (ai_settings.screen_width / 2) - 100
    alien_top.rect.y = ((ai_settings.screen_height / 2) - 30)
    alien_top.blitme()
    alien_middle = AlienMiddle(ai_settings, screen)
    alien_middle.rect.x = (ai_settings.screen_width / 2) - 100
    alien_middle.rect.y = ((ai_settings.screen_height / 2) + 15)
    alien_middle.blitme()
    alien_bottom = AlienBottom(ai_settings, screen)
    alien_bottom.rect.x = (ai_settings.screen_width / 2) - 100
    alien_bottom.rect.y = ((ai_settings.screen_height / 2) + 65)
    alien_bottom.blitme()
    ufo = Ufo(ai_settings, screen)
    ufo.rect.x = (ai_settings.screen_width / 2) - 100
    ufo.rect.y = ((ai_settings.screen_height / 2) + 115)
    ufo.blitme()
    play_button.draw_button()
    high_scores_button.draw_button()
    pygame.display.update()


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if the fleet is at and edge and
        then update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


"""def update_bunkers(ai_settings, bullets, lasers, bunkers):
    bunkers.update()
    if pygame.sprite.spritecollideany(ship, aliens):"""


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_ufo(ai_settings, stats, sb, ufo, bullets, ufo_sound):
    move = random.randint(0, 70)
    if move == 1:
        ufo.update()
    elif ufo.rect.right >= 0:
        ufo_sound.play()
        ufo.update()
    else:
        ufo_sound.stop()

    if ufo.check_edges():
        ufo_sound.stop()
        ufo.reset_image()
        ufo.center_ufo()
    # Look for ufo and bullet collisions
    if pygame.sprite.spritecollideany(ufo, bullets):
        ufo_points = ufo.blow_up()
        stats.score += ufo_points
        sb.prep_score()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, ufo, bullets, play_button, high_scores_button, bunkers):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    ufo.blitme()
    aliens.draw(screen)
    bunkers.draw(screen)

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    """mouse_x, mouse_y = pygame.mouse.get_pos()
    button_clicked = high_scores_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        show_high_scores_screen(ai_settings, screen, play_button)
    else:
        show_start_screen(ai_settings, screen, play_button, high_scores_button)"""
    if not stats.game_active:
        show_start_screen(ai_settings, screen, play_button, high_scores_button)
    # Make the most recently drawn screen visible.
    pygame.display.flip()
