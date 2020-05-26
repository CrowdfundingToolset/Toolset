from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


SESSION_CONFIG_DEFAULTS = dict(

    # Faktor zur Umrechnung von Punkten zu Euro: Bsp.: 0.01 -> 0,01€ pro Punkt
    real_world_currency_per_point=0.01,

    # Grundvergütung für die Teilnahme am Experiment (in Euro)
    participation_fee=5.00,

    doc=""

)

SESSION_CONFIGS = [
    dict(
        name='crowdfunding',
        display_name="Crowdfunding",
        num_demo_participants=2,
        app_sequence=['crowdfunding'],

        # Gibt an, ob die "Alles oder Nichts"-Regel gelten soll
        # True: Aktiviert
        # False: Deaktiviert
        All_Or_Nothing=True,

        # Gibt den Faktor an, welcher zur Berechnung der Rückzahlungs-Boni verwendet werden soll
        # Beispiel: 0.2 => Spieler erhält einen Rückzahlungs-Bonus von 20% auf die Spenden, welche im Bonus-Zeitraum abgegeben wurden
        # Hinweis: Ist auf 0 zu stellen, falls es keine Rückzahlungs-Boni geben soll
        # Hinweis: Rückzahlungs-Boni können nur in Verbindung mit "Alles oder nichts"-Regel aktiviert werden (All_Or_Nothing=True)
        Refund_Bonus=0.2,

        # Gibt den Faktor an, welcher zur Berechnung der Early-Bird-Boni verwendet werden soll
        # Beispiel: 0.1 => Early Bird Bonus beträgt 10% der Spenden, welche im Bonus-Zeitraum abgegeben wurden
        # Hinweis: Ist auf 0 zu stellen, falls es keine Early-Bird-Boni geben soll
        Early_Bird_Bonus=0.1,

        # Gibt an, ob es möglich sein soll, aus Projekten auszusteigen
        # True: Aktiviert
        # False: Deaktiviert
        Enable_Backout=True,

        # Kosten, welche beim Ausstieg aus einem Projekt anfallen (können auf 0 gesetzt werden)
        Backout_Fees=10,

        # Gibt an, ob die Anzahl der Spieler, welche ein Projekt unterstützen, angezeigt werden soll
        # True: Unterstützer werden angezeigt
        # False: Unterstützer werden nicht angezeigt
        Show_Backers=True,

        # Gibt an, ob die Projekte öffentliche Güter sein sollen
        # True: Projekte sind öffentliche Güter -> Spieler erhalten Auszahlungen für erfolgreiche Projekte, auch sie nichts gespendet haben
        # False: Projekte sind private Güter -> Spieler erhalten Auszahlungen für erfolgreiche Projekte nur, wenn sie mindestens (Min_Factor * Spendenziel) Punkte an das Projekt gespendet haben
        Public_Goods=False,

        # Nur relevant, falls die Projekte private Güter sind (Public_Goods=False)
        # Spieler müssen mindestens (Min_Factor * Spendenziel) Punkte an ein erfolgreiches Projekt gespendet habe, um ihre zugehörige Auszahlung zu erhalten
        Min_Factor=0.01,

        # Dauer einer Crowdfunding Runde in Sekunden
        Round_Duration=300,

        # Zeitraum nach Rundenbeginn, in dem Boni gewährt werden (in Sekunden)
        Bonus_Duration=60,

        # Startkapital eines jeden Spielers zu Beginn jeder Runde
        Endowment=150,

        # Anzahl der Projekte (auf maximal 4 begrenzt)
        Num_Projects = 4,

        # Spendenziel des Projektes A
        Project_A_Goal=300,

        # Spendenziel des Projektes B
        Project_B_Goal=200,

        # Spendenziel des Projektes C
        Project_C_Goal=350,

        # Spendenziel des Projektes D
        Project_D_Goal=400,

        # Startkapital für Projekt A
        Project_A_Seed=0,

        # Startkapital für Projekt B
        Project_B_Seed=0,

        # Startkapital für Projekt C
        Project_C_Seed=0,

        # Startkapital für Projekt D
        Project_D_Seed=0,


    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 2

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'jimw*p5ifm$!**s883tzph(zshvdtl2061tkhb#nl7a3v9dg=h'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
EXTENSION_APPS = ['bachelor']


