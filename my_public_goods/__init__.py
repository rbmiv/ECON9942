from otree.api import *


doc = """
Simple provision game - 4 players, 10 rounds, initial endowment of 30 tokens, MPCR of 0.75 for rounds 1-5, and MPCR of 0.3 for rounds 6-10
"""


class C(BaseConstants):
    NAME_IN_URL = 'my_public_goods'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 0
    MID_ROUND = int(NUM_ROUNDS/2)    #wanted to report the middle round in the Contribute HTML page
                                # but wasn't sure how to do a mathematical operation in an HTML file
    MULTIPLIER1 = 0.75
    MULTIPLIER2 = 1/3
    ENDOWMENT = cu(30)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    total_contribution_multiplied = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min = 0, max = C.ENDOWMENT, label = "Please enter your contribution for this round."
    )

# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution=sum(contributions)
    group.total_contribution_multiplied = sum(contributions)*C.PLAYERS_PER_GROUP
    for p in players:
        if group.round_number <= C.MID_ROUND:
            group.individual_share = (
                    group.total_contribution_multiplied*C.MULTIPLIER1/C.PLAYERS_PER_GROUP
            )
        if group.round_number > C.MID_ROUND:
            group.individual_share = (
                    group.total_contribution_multiplied * C.MULTIPLIER2 / C.PLAYERS_PER_GROUP
            )
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share

# PAGES
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs




class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results]
