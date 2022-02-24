from otree.api import *
import random
import json
import csv
import pandas as pd

c = Currency

doc = """

"""
#test


class Constants(BaseConstants):
    name_in_url = 'health_beliefs'
    players_per_group = None
    num_rounds = 3
    alpha = 5
    beta = 5
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

        print(player.payoff)
        print(player.bin_labels)
        print(player.response)
        print(player.qid)
        print(player.correct_index)
        print(player.bin_labels)

        df = pd.read_csv('health_beliefs/subpopmeans.csv')

        if player.qid == 'diabetes':

            subpopmean = 100 *  df[(df['Female'] == player.participant.gender) &
                                 (df['Age group'] == player.participant.age_group) &
                                 (df['BMI category'] == player.participant.bmi_cat) &
                                 (df['EverDiabetes'] == 1)].iloc[0]['Mean']
            print(subpopmean)
            if subpopmean <= 5:
                player.correct_index = 0
            elif subpopmean <= 10:
                player.correct_index = 1
            elif subpopmean <= 15:
                player.correct_index = 2
            elif subpopmean <= 20:
                player.correct_index = 3
            elif subpopmean <= 25:
                player.correct_index = 4
            elif subpopmean <= 30:
                player.correct_index = 5
            elif subpopmean <= 35:
                player.correct_index = 6
            elif subpopmean <= 40:
                player.correct_index = 7
            else:
                player.correct_index = 8

        if player.qid == 'heart_condition':
            subpopmean = 100 * df[(df['Female'] == player.participant.gender) &
                                 (df['Age group'] == player.participant.age_group) &
                                 (df['BMI category'] == player.participant.bmi_cat) &
                                 (df['EverHeartCondition'] == 1)].iloc[0]['Mean']
            print(subpopmean)
            if subpopmean <= 5:
                player.correct_index = 0
            elif subpopmean <= 10:
                player.correct_index = 1
            elif subpopmean <= 15:
                player.correct_index = 2
            elif subpopmean <= 20:
                player.correct_index = 3
            elif subpopmean <= 25:
                player.correct_index = 4
            elif subpopmean <= 30:
                player.correct_index = 5
            elif subpopmean <= 35:
                player.correct_index = 6
            elif subpopmean <= 40:
                player.correct_index = 7
            else: player.correct_index = 8
        print(player.correct_index)
        print(response_list)
        print(player.participant.gender, player.participant.age_group, player.participant.bmi_cat)

        ss = 0
        for i in range(len(response_list)):
            ss = ss + (response_list[i] / Constants.num_tokens) * (response_list[i] / Constants.num_tokens)
        player.payoff = (
                Constants.alpha +
                Constants.beta * ((2 * response_list[player.correct_index] / Constants.num_tokens) - ss)
        )



class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        bin_labels_list = player.bin_labels
        bin_labels_list = bin_labels_list.replace(']', '')
        bin_labels_list = bin_labels_list.replace('[', '')
        bin_labels_list = bin_labels_list.split(',')
        response_list = player.response.replace(']', '')
        response_list = response_list.replace('[', '')
        response_list = response_list.split(',')
        response_list = list(map(int, response_list))
        df = pd.read_csv('health_beliefs/subpopmeans.csv')
        return dict(
            correct_label=bin_labels_list[player.correct_index],
            correct_response=response_list[player.correct_index]
        )


page_sequence = [Beliefs, Results]
