# game_stats.py
# Created by: John Gawlik
# Campus ID: 889752424
# Due: September 21st, 2018
########################################################################################################################
class GameStats():
    """Track statistics foe Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        high_scores_file = open("high_scores.txt", "r+")
        high_score_str = high_scores_file.readline(1)
        self.high_score = int(high_score_str)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
