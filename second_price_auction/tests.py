from otree.api import Currency as c, currency_range
from . import *
from otree.api import Bot


# BOTS
class PlayerBot(Bot):
    @staticmethod
    def play_round(self):
        # Bid, ResultsWaitPage, Results
        yield Bid, dict(bid=9)
        yield Results

