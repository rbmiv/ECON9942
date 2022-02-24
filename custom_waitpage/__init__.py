from otree.api import *
import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'custom_waitpage'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    random_draw = models.IntegerField(initial=-1)


# FUNCTIONS

def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.random_draw = random.randint(0, 100)


# PAGES
class MyPage(Page):
    def vars_for_template(player):
        return dict(
            a=9999,
        )


class MyWaitPage(WaitPage):
    template_name = 'custom_waitpage/MyWaitPage.html'

    def vars_for_template(player):
        return dict(
            a=9999,
        )


class Results(Page):
    pass


page_sequence = [MyPage, MyWaitPage, Results]
