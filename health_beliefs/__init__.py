from otree.api import *
import random
import json
import csv
import pandas as pd

c = Currency

doc = """

"""


# test


class Constants(BaseConstants):
    name_in_url = 'health_beliefs'
    players_per_group = None
    num_rounds = 7
    alpha = 10
    beta = 10
    num_tokens = 100
    color = '--blue'


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


# class Question:
#     def __init__(self, text, bin_labels, correct_index):
#         self.text = text
#         self.bin_labels = bin_labels
#         self.correct_index = correct_index

class Player(BasePlayer):
    qid = models.StringField()
    question = models.StringField()
    alpha = models.FloatField()
    num_tokens = models.IntegerField()
    beta = models.FloatField()
    color = models.StringField()
    correct_index = models.IntegerField()
    response = models.StringField(initial=-999)
    bin_labels = models.StringField()
    correct_bin = models.StringField()
    correct_label = models.StringField()
    enumerator_id = models.StringField(label="Enumerator ID")


# FUNCTIONS

def creating_session(subsession):
    if subsession.round_number == 1:
        subsession.session.vars['last_round'] = len(subsession.session.config['params'])
        # print(subsession.session.vars)

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
            p.correct_index = question[7]
            p.correct_label = json.dumps(question[5])


# PAGES

class Beliefs(Page):
    form_model = 'player'
    form_fields = ['response']

    def is_displayed(player):
        return player.subsession.round_number <= player.subsession.session.vars['last_round']

    def vars_for_template(player):
        return dict(
            qid=player.qid,
            question=player.question,
            alpha=player.alpha,
            num_tokens=player.num_tokens,
            beta=player.beta,
            color=json.loads(player.color),
            bin_labels=json.loads(player.bin_labels),
            response=json.loads(player.response),
            correct_index=player.correct_index
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        response_list = player.response.replace(']', '')
        response_list = response_list.replace('[', '')
        response_list = response_list.split(',')
        response_list = list(map(int, response_list))
        bin_labels_list = player.bin_labels
        bin_labels_list = bin_labels_list.replace(']', '')
        bin_labels_list = bin_labels_list.replace('[', '')
        bin_labels_list = bin_labels_list.replace('"', '')
        bin_labels_list = bin_labels_list.split(',')

        if player.qid == 'arthritis':
            player.correct_index = player.participant.correct_bin_ar
            player.participant.correct_label_ar = bin_labels_list[player.correct_index]
        if player.qid == 'heart_disease':
            player.correct_index = player.participant.correct_bin_hd
            player.participant.correct_label_hd = bin_labels_list[player.correct_index]
        if player.qid == 'skin_cancer':
            player.correct_index = player.participant.correct_bin_sc
            player.participant.correct_label_sc = bin_labels_list[player.correct_index]
        if player.qid == 'other_cancer':
            player.correct_index = player.participant.correct_bin_oc
            player.participant.correct_label_oc = bin_labels_list[player.correct_index]
        if player.qid == 'diabetes':
            player.correct_index = player.participant.correct_bin_di
            player.participant.correct_label_di = bin_labels_list[player.correct_index]
        if player.qid == 'stroke':
            player.correct_index = player.participant.correct_bin_st
            player.participant.correct_label_st = bin_labels_list[player.correct_index]
        if player.qid == 'smoking':
            player.correct_index = 1
            player.participant.correct_label_sm = bin_labels_list[1]

        ss = 0
        for i in range(len(response_list)):
            ss = ss + (response_list[i] / Constants.num_tokens) * (response_list[i] / Constants.num_tokens)
        player.payoff = (
                Constants.alpha +
                Constants.beta * ((2 * response_list[player.correct_index] / Constants.num_tokens) - ss)
        )
        if player.qid == 'arthritis':
            player.participant.answer_bin_ar = response_list[player.correct_index]
            player.participant.payoff_ar = player.payoff
        if player.qid == 'heart_disease':
            player.participant.answer_bin_hd = response_list[player.correct_index]
            player.participant.payoff_hd = player.payoff
        if player.qid == 'skin_cancer':
            player.participant.answer_bin_sc = response_list[player.correct_index]
            player.participant.payoff_sc = player.payoff
        if player.qid == 'other_cancer':
            player.participant.answer_bin_oc = response_list[player.correct_index]
            player.participant.payoff_oc = player.payoff
        if player.qid == 'diabetes':
            player.participant.answer_bin_di = response_list[player.correct_index]
            player.participant.payoff_di = player.payoff
        if player.qid == 'stroke':
            player.participant.answer_bin_st = response_list[player.correct_index]
            player.participant.payoff_st = player.payoff
        if player.qid == 'smoking':
            player.participant.answer_bin_sm = response_list[player.correct_index]
            player.participant.payoff_sm = player.payoff
        print('=======before next page:', player.qid, '========')
        print('player payoff: ', player.payoff)
        print('question correct index: ', player.correct_index)


# class Results(Page):
#     @staticmethod
#     def vars_for_template(player: Player):
#         bin_labels_list = player.bin_labels
#         bin_labels_list = bin_labels_list.replace(']', '')
#         bin_labels_list = bin_labels_list.replace('[', '')
#         bin_labels_list = bin_labels_list.split(',')
#         response_list = player.response.replace(']', '')
#         response_list = response_list.replace('[', '')
#         response_list = response_list.split(',')
#         response_list = list(map(int, response_list))
#         return dict(
#             correct_label=bin_labels_list[player.correct_index],
#             correct_response=response_list[player.correct_index]
#         )


page_sequence = [Beliefs]
