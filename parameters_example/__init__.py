from otree.api import *
import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'parameters_example'
    players_per_group = None
    num_rounds = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    image = models.StringField()


# FUNCTIONS

def creating_session(subsession):
    # create our own 'last round' variable based on how many images we have to show
    subsession.session.vars['last_round'] = len(subsession.session.config['images'])
    n = subsession.session.vars['last_round']

    # randomly order images for each player
    for p in subsession.get_players():
        if subsession.round_number == 1:
            p.participant.vars['image_sequence'] = random.sample(range(n), n)
        if subsession.round_number <= n:
            image_index = p.participant.vars['image_sequence'][subsession.round_number - 1]
            p.image = subsession.session.config['images'][image_index]


# PAGES
class MyPage(Page):
    form_model = 'player'


class Results(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.subsession.round_number == player.subsession.session.vars['last_round']

    # def vars_for_template(p: Player):
    #     image_list = []
    #     for i in p.participant.vars['image_sequence']:




        # return dict(
        #     my_images=2
        # )


page_sequence = [MyPage, Results]
