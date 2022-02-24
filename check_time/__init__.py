from otree.api import *
import datetime

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'check_time'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


def creating_session(subsession):

    if subsession.round_number == 1:
        print(subsession.session.vars)
        subsession.session.vars['start_time'] = datetime.datetime.now()
        print(subsession.session.vars['start_time'])



# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
