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


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=18, max=125)
    gender = models.IntegerField(
        choices=[[0, 'Male'], [1, 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    weight = models.IntegerField(label='What is your weight (lbs)?', min=80, max=350)
    height = models.IntegerField(label='What is your height (inches)?', min=48, max=84)



# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'weight', 'height']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.age=player.age
        if player.age <= 24:
            participant.age_group = 1
        elif player.age <= 34:
            participant.age_group = 2
        elif player.age <= 44:
            participant.age_group = 3
        elif player.age <= 54:
            participant.age_group = 4
        elif player.age <= 64:
            participant.age_group = 5
        else:
            participant.age_group = 6
        participant.gender = player.gender
        participant.height = player.height
        participant.weight = player.weight
        participant.bmi = player.weight / (player.height*player.height) * 703
        if participant.bmi <= 19:
            participant.bmi_cat = 1
        elif participant.bmi <= 25:
            participant.bmi_cat = 2
        elif participant.bmi <= 30:
            participant.bmi_cat = 3
        else:
            participant.bmi_cat = 4




# class CognitiveReflectionTest(Page):
#     form_model = 'player'
#     form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


page_sequence = [Demographics, ]
