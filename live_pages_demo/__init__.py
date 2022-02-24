from otree.api import *
import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'live_pages_demo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    numA = models.IntegerField()
    numB = models.IntegerField()
    answer = models.IntegerField()
    countCorrect = models.IntegerField(initial=0)
    countIncorrect = models.IntegerField(initial=0)


# FUNCTIONS

def creating_session(subsession):
    for p in subsession.get_players():
        p.numA = round(random.random() * 10)
        p.numB = round(random.random() * 10)


# PAGES
class MyPage(Page):
    @staticmethod
    def live_method(player, data):
        print(data)
        print(player.numA, player.numB)
        print(player.numA + player.numB == int(data))
        if player.numA + player.numB == int(data):
            player.countCorrect += 1
        else:
            player.countIncorrect += 1
        # print('Player ', player.id_in_subsession, ' correct=', player.numCorrect, ' incorrect=', player.numIncorrect)

        player.numA = round(random.random() * 10)
        player.numB = round(random.random() * 10)

        msg = {
            'num_a': player.numA,
            'num_b': player.numB,
            'count_correct': player.countCorrect,
            'count_incorrect': player.countIncorrect,
        }
        return {player.id_in_group: msg}


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass





page_sequence = [MyPage, ResultsWaitPage, Results]
