# alien_invasion.py
# Created by: John Gawlik
# Campus ID: 889752424
# Due: September 21st, 2018
########################################################################################################################
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import PlayButton
from scoreboard import Scoreboard
from alien import Ufo
import game_functions as gf
from button import HighScoresButton


def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ufo_sound = pygame.mixer.Sound('sounds/UFO_Sound_Effect.wav')

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    ufo = Ufo(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    lasers = Group()
    bunkers = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Play Button.
    play_button = PlayButton(ai_settings, screen, "Play")
    high_scores_button = HighScoresButton(ai_settings, screen, "High Scores")

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, high_scores_button, ship, aliens, ufo, bullets, bunkers)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_ufo(ai_settings, stats, sb, ufo, bullets, ufo_sound)
            #gf.update_bunkers(ai_settings, bullets, lasers, bunkers)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, ufo, bullets, play_button, high_scores_button,
                         bunkers)


run_game()
