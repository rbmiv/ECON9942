from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'template_looping'
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
    def vars_for_template(player):
        return dict(
            list_1=['ann', 'bob', 'cary'],
            list_2=[],
            list_3=['morton', 'nancy'],
            list_4=['zeke'],
        )

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage]
