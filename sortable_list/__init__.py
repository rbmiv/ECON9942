from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'sortable_list'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response = models.StringField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['response']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
