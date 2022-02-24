from otree.api import *
import random
import json
import csv

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'beliefs'
    players_per_group = None
    num_rounds = 30


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    qid = models.StringField()
    question = models.StringField()
    alpha = models.FloatField()
    num_tokens = models.IntegerField()
    beta = models.FloatField()
    color = models.StringField()
    bin_labels = models.StringField()
    response = models.StringField(initial=-999)
    enumerator_id = models.StringField(label="Enumerator ID")
    household_id = models.StringField(label="Participant ID 1")
    household_id_2 = models.StringField(label="Participant ID 2")


# FUNCTIONS

def creating_session(subsession):
    if subsession.round_number == 1:
        subsession.session.vars['last_round'] = len(subsession.session.config['params'])
        # print(subsession.session.vars)
        if 'language' in subsession.session.config:
            subsession.session.vars['language'] = subsession.session.config['language']
        else:
            subsession.session.vars['language'] = 'english'

    for p in subsession.get_players():
        if subsession.round_number == 1:
            # Beliefs questions will be in fixed order, so skip the random reordering
            # p.participant.vars['beliefs_sequence'] = random.sample(range(n), n)
            p.participant.vars['beliefs_sequence'] = range(subsession.session.vars['last_round'])

        if subsession.round_number <= subsession.session.vars['last_round']:
            question_number = p.participant.vars['beliefs_sequence'][subsession.round_number - 1]
            question = subsession.session.config['params'][question_number]

            p.qid = question[0]
            p.question = question[1]
            p.alpha = question[2]
            p.beta = question[3]
            p.num_tokens = question[4]
            p.bin_labels = json.dumps(question[5])
            p.color = json.dumps([question[6]])

            print(p.question)
            print(p.alpha)
            print(p.beta)
            print(p.bin_labels)


# def household_id_error_message(player, value):
#     print('hhid value is', value)
#     lst = open('_static/HHIDs.txt').read().splitlines()
#     if lst.count(value) != 1:
#         return 'Household ID does not match. Try again.'




# PAGES

class MyPage(Page):
    form_model = 'player'
    form_fields = ['response']

    def is_displayed(player):
        return player.subsession.round_number <= player.subsession.session.vars['last_round']

    def vars_for_template(player):
        return dict(
            language=player.session.vars['language'],
            qid=player.qid,
            question=player.question,
            alpha=player.alpha,
            num_tokens=player.num_tokens,
            beta=player.beta,
            color=json.loads(player.color),
            bin_labels=player.bin_labels,
            response=player.response,
        )


page_sequence = [MyPage,]
