from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'baby_livepage'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    @staticmethod
    def live_method(player, data):
        print('received a message from', player.id_in_group, ':', data)
        txt = "Player "
        txt += str(player.id_in_group)
        txt += " says: "
        txt += str(data)
        return {0: txt}


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
