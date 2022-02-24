from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'regroup'
    players_per_group = 3
    num_rounds = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS

def creating_session(subsession):
    pass
    # print('in creating session')
    # print('round', subsession.round_number, 'group matrix is', subsession.get_group_matrix())


def regroup(subsession):
    for subses in [subsession.in_round(x) for x in range(1, Constants.num_rounds)]:
        rnd = subses.round_number
        mtx = subses.get_group_matrix()
        print(rnd, mtx)
        new_mtx = [[1],[2,3],[4,5,6]]
        subses.set_group_matrix(new_mtx)
        print(rnd, subses.get_group_matrix())





# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'regroup'


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
