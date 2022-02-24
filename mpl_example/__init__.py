from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mpl_example'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response = models.StringField()
    risky_low = models.IntegerField()
    risky_high = models.IntegerField()


# PAGES

class MyPage(Page):
    form_model = 'player'
    form_fields = ['response']

    def vars_for_template(player):

        # Add code here to construct the wording that will be displayed in your MPL.
        # For this example I just used silly static text below.

        # I am using only 3 rows for this example. You must add additional code for more rows. Both below
        # and also in the HTML page.

        player.risky_low = 1
        player.risky_high = 111


        return dict(
            num_rows=3,
            L1="10% chance of $" + str(player.risky_low) + " and 90% of $" + str(player.risky_high),
            R1='first row right option',
            L2='second row left option',
            R2='second row right option',
            L3='third row left option',
            R3='third row right option',
        )


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
