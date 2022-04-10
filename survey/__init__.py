from otree.api import (
    Page,
    WaitPage,
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import pandas as pd


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age_group = models.IntegerField(label='What is your age?', min=18, max=125)
    gender = models.IntegerField(
        choices=[[0, 'Male'], [1, 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    weight = models.IntegerField(label='What is your weight (lbs)?', min=80, max=350)
    height = models.IntegerField(label='What is your height (inches)?', min=48, max=84)
    race = models.IntegerField(
        choices=[[1, 'White'], [2, 'Black or African American'], [3, 'American Indian or Alaska Native'], [4, 'Asian'],
                 [5, 'Native Hawaiian or Other Pacific Islander'], [6, 'Hispanic'], [7, 'Other']],
        label='Which one of these groups would you say best represents your race or ethnicity?',
        widget=widgets.RadioSelect,
    )


# FUNCTIONS
# PAGES
class Introduction(Page):
    pass


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age_group', 'gender', 'weight', 'height', 'race']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.race = player.race
        participant.age_group = player.age_group
        if player.age_group <= 24:
            participant.age_group = 1
        elif player.age_group <= 29:
            participant.age_group = 2
        elif player.age_group <= 34:
            participant.age_group = 3
        elif player.age_group <= 39:
            participant.age_group = 4
        elif player.age_group <= 44:
            participant.age_group = 5
        elif player.age_group <= 49:
            participant.age_group = 6
        elif player.age_group <= 54:
            participant.age_group = 7
        elif player.age_group <= 59:
            participant.age_group = 8
        elif player.age_group <= 64:
            participant.age_group = 9
        elif player.age_group <= 69:
            participant.age_group = 10
        elif player.age_group <= 74:
            participant.age_group = 11
        elif player.age_group <= 79:
            participant.age_group = 12
        else:
            participant.age_group = 13

        participant.gender = player.gender
        participant.height = player.height
        participant.weight = player.weight
        participant.bmi = player.weight / (player.height * player.height) * 703
        if participant.bmi <= 19:
            participant.bmi_cat = 1
        elif participant.bmi <= 25:
            participant.bmi_cat = 2
        elif participant.bmi <= 30:
            participant.bmi_cat = 3
        else:
            participant.bmi_cat = 4
        print('age group', participant.age_group, 'gender', participant.gender, 'bmi_cat', participant.bmi_cat,
              'race', participant.race)

        df = pd.read_csv('health_beliefs/subpop_means.csv')

        mean_arthritis = 100 * df[
            (df['Condition'] == 'arthritis') &
            (df['Female'] == participant.gender) &
            (df['Age Group'] == participant.age_group) &
            (df['BMI category'] == participant.bmi_cat)].iloc[0]['Mean']
        print('arthritis', mean_arthritis)
        if mean_arthritis <= 5:
            participant.correct_bin_ar = 0
        elif mean_arthritis <= 10:
            participant.correct_bin_ar = 1
        elif mean_arthritis <= 15:
            participant.correct_bin_ar = 2
        elif mean_arthritis <= 20:
            participant.correct_bin_ar = 3
        elif mean_arthritis <= 25:
            participant.correct_bin_ar = 4
        elif mean_arthritis <= 30:
            participant.correct_bin_ar = 5
        elif mean_arthritis <= 35:
            participant.correct_bin_ar = 6
        elif mean_arthritis <= 40:
            participant.correct_bin_ar = 7
        else:
            participant.correct_bin_ar = 8

        mean_heart_disease = 100 * df[
            (df['Condition'] == 'heart_disease') &
            (df['Female'] == participant.gender) &
            (df['Age Group'] == participant.age_group) &
            (df['BMI category'] == participant.bmi_cat)].iloc[0]['Mean']

        print('heart_disease', mean_heart_disease)
        if mean_heart_disease <= 5:
            participant.correct_bin_hd = 0
        elif mean_heart_disease <= 10:
            participant.correct_bin_hd = 1
        elif mean_heart_disease <= 15:
            participant.correct_bin_hd = 2
        elif mean_heart_disease <= 20:
            participant.correct_bin_hd = 3
        elif mean_heart_disease <= 25:
            participant.correct_bin_hd = 4
        elif mean_heart_disease <= 30:
            participant.correct_bin_hd = 5
        elif mean_heart_disease <= 35:
            participant.correct_bin_hd = 6
        elif mean_heart_disease <= 40:
            participant.correct_bin_hd = 7
        else:
            participant.correct_bin_hd = 8

        mean_other_cancer = 100 * df[
            (df['Condition'] == 'other_cancer') &
            (df['Female'] == participant.gender) &
            (df['Age Group'] == participant.age_group) &
            (df['BMI category'] == participant.bmi_cat)].iloc[0]['Mean']
        print('other_cancer', mean_other_cancer)
        if mean_other_cancer <= 5:
            participant.correct_bin_oc = 0
        elif mean_other_cancer <= 10:
            participant.correct_bin_oc = 1
        elif mean_other_cancer <= 15:
            participant.correct_bin_oc = 2
        elif mean_other_cancer <= 20:
            participant.correct_bin_oc = 3
        elif mean_other_cancer <= 25:
            participant.correct_bin_oc = 4
        elif mean_other_cancer <= 30:
            participant.correct_bin_oc = 5
        elif mean_other_cancer <= 35:
            participant.correct_bin_oc = 6
        elif mean_other_cancer <= 40:
            participant.correct_bin_oc = 7
        else:
            participant.correct_bin_oc = 8

        mean_diabetes = 100 * df[
            (df['Condition'] == 'diabetes') &
            (df['Female'] == participant.gender) &
            (df['Age Group'] == participant.age_group) &
            (df['BMI category'] == participant.bmi_cat)].iloc[0]['Mean']
        print('diabetes', mean_diabetes)
        if mean_diabetes <= 5:
            participant.correct_bin_di = 0
        elif mean_diabetes <= 10:
            participant.correct_bin_di = 1
        elif mean_diabetes <= 15:
            participant.correct_bin_di = 2
        elif mean_diabetes <= 20:
            participant.correct_bin_di = 3
        elif mean_diabetes <= 25:
            participant.correct_bin_di = 4
        elif mean_diabetes <= 30:
            participant.correct_bin_di = 5
        elif mean_diabetes <= 35:
            participant.correct_bin_di = 6
        elif mean_diabetes <= 40:
            participant.correct_bin_di = 7
        else:
            participant.correct_bin_di = 8

        mean_stroke = 100 * df[
            (df['Condition'] == 'stroke') &
            (df['Female'] == participant.gender) &
            (df['Age Group'] == participant.age_group) &
            (df['BMI category'] == participant.bmi_cat)].iloc[0]['Mean']
        print('stroke', mean_stroke)
        if mean_stroke <= 5:
            participant.correct_bin_st = 0
        elif mean_stroke <= 10:
            participant.correct_bin_st = 1
        elif mean_stroke <= 15:
            participant.correct_bin_st = 2
        elif mean_stroke <= 20:
            participant.correct_bin_st = 3
        elif mean_stroke <= 25:
            participant.correct_bin_st = 4
        elif mean_stroke <= 30:
            participant.correct_bin_st = 5
        elif mean_stroke <= 35:
            participant.correct_bin_st = 6
        elif mean_stroke <= 40:
            participant.correct_bin_st = 7
        else:
            participant.correct_bin_st = 8

        df2 = pd.read_csv('health_beliefs/subpop_mean_skincancer.csv')

        mean_skin_cancer = 100 * df2[
            (df2['Age Group'] == participant.age_group) &
            (df2['Race'] == participant.race) &
            (df2['BMI Category'] == participant.bmi_cat) &
            (df2['Gender'] == participant.gender)].iloc[0]['Mean']

        print('skin_cancer', mean_skin_cancer)
        if mean_skin_cancer <= 5:
            participant.correct_bin_sc = 0
        elif mean_skin_cancer <= 10:
            participant.correct_bin_sc = 1
        elif mean_skin_cancer <= 15:
            participant.correct_bin_sc = 2
        elif mean_skin_cancer <= 20:
            participant.correct_bin_sc = 3
        elif mean_skin_cancer <= 25:
            participant.correct_bin_sc = 4
        elif mean_skin_cancer <= 30:
            participant.correct_bin_sc = 5
        elif mean_skin_cancer <= 35:
            participant.correct_bin_sc = 6
        elif mean_skin_cancer <= 40:
            participant.correct_bin_sc = 7
        else:
            participant.correct_bin_sc = 8


class Continue(Page):
    pass





# class CognitiveReflectionTest(Page):
#     form_model = 'player'
#     form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


page_sequence = [Introduction, Demographics, Continue]
