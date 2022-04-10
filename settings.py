from os import environ

SESSION_CONFIGS = [
    {
        'name': 'health_beliefs_practice',
        'language': 'english',
        'display_name': 'health beliefs practice questions',
        'num_demo_participants': 15,
        'app_sequence': ['survey', 'instructions', 'health_beliefs', 'results'], #SUBJECT INSTRUCTIONS AND RESULTS PAGES GO HERE
        # params format: [ 'question text...',
        #               alpha, beta, num_tokens
        #               ['bin 1 label', 'bin 2 label', ... 'bin N label'],
        #               color, correct bin index]
        'params':
        [
            ['diabetes',
             'Among 100 people like you (sharing the same age group, bmi, and biological sex), '
             'how many do you expect to have ever had diabetes?',
             10, 10, 100,
             ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '40 or more'],
             '--blue', 0],

            ['heart_disease',
             'Among 100 people like you (sharing the same age group, bmi, and biological sex), '
             'how many do you expect to have ever had a heart problem (heart attack, coronary heart disease, angina)?',
             10, 10, 100,
             ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '40 or more'],
             '--blue', 0],
#
            ['skin_cancer',
             'Among 100 people like you (sharing the same race and age group),'
             'how many do you expect to have ever been diagnosed with skin cancer?',
             10, 10, 100,
             ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '40 or more'],
             '--blue', 0],

            ['other_cancer',
             'Among 100 people like you (sharing the same age group, bmi, and biological sex), '
             'how many do you expect to have ever been diagnosed with any type of cancer (other than skin cancer)?',
             10, 10, 100,
             ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '40 or more'],
             '--blue', 0],

            ['stroke',
             'Among 100 people like you (sharing the same age group, bmi, and biological sex), '
             'how many do you expect to have ever had a stroke ?',
             10, 10, 100,
             ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '40 or more'],
             '--blue', 0],

            ['arthritis',
             'Among 100 people like you (sharing the same age group, bmi, and biological sex), '
             'how many do you expect to have ever had some form of '
             'arthritis, rheumatoid arthritis, gout, lupus, or fibromyalgia? ',
             10, 10, 100,
             ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '40 or more'],
             '--blue', 0],

            ['smoking',
             'Among 100 cigarette smokers, how many of them do you think will get lung cancer '
             ' because they smoke?',
             10, 10, 100,
             ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100'],
             '--blue', 1],
        ]
    },
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = ['age', 'age_group', 'height', 'weight', 'bmi', 'bmi_cat', 'gender', 'race',
                      'correct_bin_ar', 'answer_bin_ar', 'payoff_ar', 'correct_label_ar',
                      'correct_bin_hd', 'answer_bin_hd', 'payoff_hd', 'correct_label_hd',
                      'correct_bin_sc', 'answer_bin_sc', 'payoff_sc', 'correct_label_sc',
                      'correct_bin_oc', 'answer_bin_oc', 'payoff_oc', 'correct_label_oc',
                      'correct_bin_di', 'answer_bin_di', 'payoff_di', 'correct_label_di',
                      'correct_bin_st', 'answer_bin_st', 'payoff_st', 'correct_label_st',
                      'correct_bin_sm', 'answer_bin_sm', 'payoff_sm', 'correct_label_sm',
                      ]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(
        name='econ9942',
        display_name='Econ 9942 class',
        participant_label_file='_rooms/econ9942.txt',
        use_secure_urls=True,
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = '7267278848110'

INSTALLED_APPS = ['otree']

# use_browser_bots = True
