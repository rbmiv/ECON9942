from os import environ

SESSION_CONFIGS = [
    {
        'name': 'health_beliefs_practice',
        'language': 'english',
        'display_name': 'health beliefs practice questions',
        'num_demo_participants': 3,
        'app_sequence': ['survey', 'health_beliefs'],
        # params format: [ 'question text...',
        #               alpha, beta, num_tokens
        #               ['bin 1 label', 'bin 2 label', ... 'bin N label'],
        #               color, correct bin index]
        'params': [
            ['smoking',
             'Among 100 cigarette smokers, how many of them do you think will get lung cancer'
             'because they smoke?',
             5, 5, 100,
             ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100'],
             '--blue', 1],

            ['diabetes',
             'Among 100 people like you (sharing the same age group, bmi, and biological sex), '
             'how many do you expect to have ever had diabetes?',
             5, 5, 100,
             ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '40 or more'],
             '--blue', 0],

            ['heart_condition',
             'Among 100 people like you (sharing the same age group, bmi, and biological sex), '
             'how many do you expect to have ever had a heart problem (heart attack, coronary heart disease, angina)?',
             5, 5, 100,
             ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '40 or more'],
             '--blue', 0],
        ]
    },
    dict(
        name='sortable_list',
        display_name='sortable list',
        num_demo_participants=1,
        app_sequence=['sortable_list'],
    ),

    dict(
        name='pub_goods_test',
        display_name='my pub goods',
        num_demo_participants=2,
        app_sequence=['my_pub_goods'],
    ),
    dict(
        name='ben_pub_goods_test',
        display_name='Bens Public Goods Test',
        num_demo_participants=2,
        app_sequence=['my_public_goods'],
    ),
    dict(
        name='second_price_auction',
        display_name='second price auction',
        num_demo_participants=3,
        app_sequence=['second_price_auction'],
    ),
    dict(
        name='input_examples',
        display_name='examples of different inputs',
        num_demo_participants=1,
        app_sequence=['input_examples'],
    ),
    dict(
        name='livepage1',
        display_name='our first live page example',
        num_demo_participants=2,
        app_sequence=['baby_livepage'],
    ),
    dict(
        name='live_pages',
        display_name='simple live pages demo',
        num_demo_participants=2,
        app_sequence=['live_pages_demo'],
    ),
    dict(
        name='images_1',
        display_name='randomizing image sequences',
        num_demo_participants=3,
        app_sequence=['parameters_example'],
        images=['duck.png', 'fish.jpg', 'pinguin.jpg']
    ),
    dict(
        name='circle',
        display_name='circle demo',
        num_demo_participants=1,
        app_sequence=['circle_example']

    ),
    dict(
        name='mpl_1',
        display_name='multiple price list example',
        num_demo_participants=1,
        app_sequence=['mpl_example'],
    ),
    dict(
        name='regroup',
        display_name='demo regrouping subjects during session',
        num_demo_participants=6,
        app_sequence=['regroup'],
    ),
    dict(
        name='video_demo',
        display_name='video demo',
        num_demo_participants=2,
        app_sequence=['video'],
    ),
    dict(
        name='template_looping',
        display_name='template looping',
        num_demo_participants=1,
        app_sequence=['template_looping'],
    ),
    dict(
        name='check_time',
        display_name='check time',
        num_demo_participants=1,
        app_sequence=['check_time'],
    ),
    dict(
        name='custom_waitpage',
        display_name='custom waitpage example',
        num_demo_participants=2,
        app_sequence=['custom_waitpage'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['age', 'age_group', 'height', 'weight','bmi', 'bmi_cat', 'gender']
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
