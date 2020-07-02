class GameStats():
    """跟蹤遊戲的統計信息"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.high_score = 0
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1