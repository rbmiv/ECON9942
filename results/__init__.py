from otree.api import *
import random

doc = """
Results and payoffs for health_beliefs module
"""


class Constants(BaseConstants):
    name_in_url = 'results'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    randint = random.randint(0, 6)


# PAGES
class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            label_ar=player.participant.correct_label_ar,
            answer_ar=player.participant.answer_bin_ar,
            payoff_ar=player.participant.payoff_ar,
            label_hd=player.participant.correct_label_hd,
            answer_hd=player.participant.answer_bin_hd,
            payoff_hd=player.participant.payoff_hd,
            label_sc=player.participant.correct_label_sc,
            answer_sc=player.participant.answer_bin_sc,
            payoff_sc=player.participant.payoff_sc,
            label_oc=player.participant.correct_label_oc,
            answer_oc=player.participant.answer_bin_oc,
            payoff_oc=player.participant.payoff_oc,
            label_di=player.participant.correct_label_di,
            answer_di=player.participant.answer_bin_di,
            payoff_di=player.participant.payoff_di,
            label_st=player.participant.correct_label_st,
            answer_st=player.participant.answer_bin_st,
            payoff_st=player.participant.payoff_st,
            label_sm=player.participant.correct_label_sm,
            answer_sm=player.participant.answer_bin_sm,
            payoff_sm=player.participant.payoff_sm,
        )


class Payment(Page):
    @staticmethod
    def vars_for_template(player: Player):
        payoff_ar = player.participant.payoff_ar
        payoff_hd = player.participant.payoff_hd
        payoff_sc = player.participant.payoff_sc
        payoff_oc = player.participant.payoff_oc
        payoff_di = player.participant.payoff_di
        payoff_st = player.participant.payoff_st
        payoff_sm = player.participant.payoff_sm
        question_set = ['Arthritis', 'Heart Disease', 'Skin Cancer', 'Other Cancer', 'Diabetes', 'Stroke', 'Smoking']
        payoff_set = [payoff_ar, payoff_hd, payoff_sc, payoff_oc, payoff_di, payoff_st, payoff_sm]
        question_label = question_set[player.randint]
        task_payoff = payoff_set[player.randint]
        participation_payment = player.session.config['participation_fee']
        total_payoff = task_payoff + participation_payment
        return dict(
            task_payoff=task_payoff,
            question_label=question_label,
            participation_payment=participation_payment,
            total_payoff=total_payoff
        )


page_sequence = [Results, Payment]
