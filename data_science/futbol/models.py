from peewee import *

database = SqliteDatabase('database.sqlite', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Country(BaseModel):
    name = TextField(null=True, unique=True)

    class Meta:
        db_table = 'Country'

class Country(BaseModel):
    name = TextField(null=True, unique=True)

    class Meta:
        db_table = 'Country'

class League(BaseModel):
    country = ForeignKeyField(db_column='country_id', null=True, rel_model=Country)
    name = TextField(null=True, unique=True)

    class Meta:
        db_table = 'League'

class Player(BaseModel):
    birthday = TextField(null=True)
    height = IntegerField(null=True)
    player_api = IntegerField(db_column='player_api_id', null=True, unique=True)
    player_fifa_api = IntegerField(db_column='player_fifa_api_id', null=True, unique=True)
    player_name = TextField(null=True)
    weight = IntegerField(null=True)

    class Meta:
        db_table = 'Player'

class Team(BaseModel):
    team_api = IntegerField(db_column='team_api_id', null=True, unique=True)
    team_fifa_api = IntegerField(db_column='team_fifa_api_id', null=True)
    team_long_name = TextField(null=True)
    team_short_name = TextField(null=True)

    class Meta:
        db_table = 'Team'

class Match(BaseModel):
    b365a = DecimalField(db_column='B365A', null=True)  # NUMERIC
    b365d = DecimalField(db_column='B365D', null=True)  # NUMERIC
    b365h = DecimalField(db_column='B365H', null=True)  # NUMERIC
    bsa = DecimalField(db_column='BSA', null=True)  # NUMERIC
    bsd = DecimalField(db_column='BSD', null=True)  # NUMERIC
    bsh = DecimalField(db_column='BSH', null=True)  # NUMERIC
    bwa = DecimalField(db_column='BWA', null=True)  # NUMERIC
    bwd = DecimalField(db_column='BWD', null=True)  # NUMERIC
    bwh = DecimalField(db_column='BWH', null=True)  # NUMERIC
    gba = DecimalField(db_column='GBA', null=True)  # NUMERIC
    gbd = DecimalField(db_column='GBD', null=True)  # NUMERIC
    gbh = DecimalField(db_column='GBH', null=True)  # NUMERIC
    iwa = DecimalField(db_column='IWA', null=True)  # NUMERIC
    iwd = DecimalField(db_column='IWD', null=True)  # NUMERIC
    iwh = DecimalField(db_column='IWH', null=True)  # NUMERIC
    lba = DecimalField(db_column='LBA', null=True)  # NUMERIC
    lbd = DecimalField(db_column='LBD', null=True)  # NUMERIC
    lbh = DecimalField(db_column='LBH', null=True)  # NUMERIC
    psa = DecimalField(db_column='PSA', null=True)  # NUMERIC
    psd = DecimalField(db_column='PSD', null=True)  # NUMERIC
    psh = DecimalField(db_column='PSH', null=True)  # NUMERIC
    sja = DecimalField(db_column='SJA', null=True)  # NUMERIC
    sjd = DecimalField(db_column='SJD', null=True)  # NUMERIC
    sjh = DecimalField(db_column='SJH', null=True)  # NUMERIC
    vca = DecimalField(db_column='VCA', null=True)  # NUMERIC
    vcd = DecimalField(db_column='VCD', null=True)  # NUMERIC
    vch = DecimalField(db_column='VCH', null=True)  # NUMERIC
    wha = DecimalField(db_column='WHA', null=True)  # NUMERIC
    whd = DecimalField(db_column='WHD', null=True)  # NUMERIC
    whh = DecimalField(db_column='WHH', null=True)  # NUMERIC
    away_player_1 = ForeignKeyField(db_column='away_player_1', null=True, rel_model=Player, to_field='player_api')
    away_player_10 = ForeignKeyField(db_column='away_player_10', null=True, rel_model=Player, related_name='Player_away_player_10_set', to_field='player_api')
    away_player_11 = ForeignKeyField(db_column='away_player_11', null=True, rel_model=Player, related_name='Player_away_player_11_set', to_field='player_api')
    away_player_2 = ForeignKeyField(db_column='away_player_2', null=True, rel_model=Player, related_name='Player_away_player_2_set', to_field='player_api')
    away_player_3 = ForeignKeyField(db_column='away_player_3', null=True, rel_model=Player, related_name='Player_away_player_3_set', to_field='player_api')
    away_player_4 = ForeignKeyField(db_column='away_player_4', null=True, rel_model=Player, related_name='Player_away_player_4_set', to_field='player_api')
    away_player_5 = ForeignKeyField(db_column='away_player_5', null=True, rel_model=Player, related_name='Player_away_player_5_set', to_field='player_api')
    away_player_6 = ForeignKeyField(db_column='away_player_6', null=True, rel_model=Player, related_name='Player_away_player_6_set', to_field='player_api')
    away_player_7 = ForeignKeyField(db_column='away_player_7', null=True, rel_model=Player, related_name='Player_away_player_7_set', to_field='player_api')
    away_player_8 = ForeignKeyField(db_column='away_player_8', null=True, rel_model=Player, related_name='Player_away_player_8_set', to_field='player_api')
    away_player_9 = ForeignKeyField(db_column='away_player_9', null=True, rel_model=Player, related_name='Player_away_player_9_set', to_field='player_api')
    away_player_x1 = IntegerField(db_column='away_player_X1', null=True)
    away_player_x10 = IntegerField(db_column='away_player_X10', null=True)
    away_player_x11 = IntegerField(db_column='away_player_X11', null=True)
    away_player_x2 = IntegerField(db_column='away_player_X2', null=True)
    away_player_x3 = IntegerField(db_column='away_player_X3', null=True)
    away_player_x4 = IntegerField(db_column='away_player_X4', null=True)
    away_player_x5 = IntegerField(db_column='away_player_X5', null=True)
    away_player_x6 = IntegerField(db_column='away_player_X6', null=True)
    away_player_x7 = IntegerField(db_column='away_player_X7', null=True)
    away_player_x8 = IntegerField(db_column='away_player_X8', null=True)
    away_player_x9 = IntegerField(db_column='away_player_X9', null=True)
    away_player_y1 = IntegerField(db_column='away_player_Y1', null=True)
    away_player_y10 = IntegerField(db_column='away_player_Y10', null=True)
    away_player_y11 = IntegerField(db_column='away_player_Y11', null=True)
    away_player_y2 = IntegerField(db_column='away_player_Y2', null=True)
    away_player_y3 = IntegerField(db_column='away_player_Y3', null=True)
    away_player_y4 = IntegerField(db_column='away_player_Y4', null=True)
    away_player_y5 = IntegerField(db_column='away_player_Y5', null=True)
    away_player_y6 = IntegerField(db_column='away_player_Y6', null=True)
    away_player_y7 = IntegerField(db_column='away_player_Y7', null=True)
    away_player_y8 = IntegerField(db_column='away_player_Y8', null=True)
    away_player_y9 = IntegerField(db_column='away_player_Y9', null=True)
    away_team_api = ForeignKeyField(db_column='away_team_api_id', null=True, rel_model=Team, to_field='team_api')
    away_team_goal = IntegerField(null=True)
    card = TextField(null=True)
    corner = TextField(null=True)
    country = ForeignKeyField(db_column='country_id', null=True, rel_model=Country)
    cross = TextField(null=True)
    date = TextField(null=True)
    foulcommit = TextField(null=True)
    goal = TextField(null=True)
    home_player_1 = ForeignKeyField(db_column='home_player_1', null=True, rel_model=Player, related_name='Player_home_player_1_set', to_field='player_api')
    home_player_10 = ForeignKeyField(db_column='home_player_10', null=True, rel_model=Player, related_name='Player_home_player_10_set', to_field='player_api')
    home_player_11 = ForeignKeyField(db_column='home_player_11', null=True, rel_model=Player, related_name='Player_home_player_11_set', to_field='player_api')
    home_player_2 = ForeignKeyField(db_column='home_player_2', null=True, rel_model=Player, related_name='Player_home_player_2_set', to_field='player_api')
    home_player_3 = ForeignKeyField(db_column='home_player_3', null=True, rel_model=Player, related_name='Player_home_player_3_set', to_field='player_api')
    home_player_4 = ForeignKeyField(db_column='home_player_4', null=True, rel_model=Player, related_name='Player_home_player_4_set', to_field='player_api')
    home_player_5 = ForeignKeyField(db_column='home_player_5', null=True, rel_model=Player, related_name='Player_home_player_5_set', to_field='player_api')
    home_player_6 = ForeignKeyField(db_column='home_player_6', null=True, rel_model=Player, related_name='Player_home_player_6_set', to_field='player_api')
    home_player_7 = ForeignKeyField(db_column='home_player_7', null=True, rel_model=Player, related_name='Player_home_player_7_set', to_field='player_api')
    home_player_8 = ForeignKeyField(db_column='home_player_8', null=True, rel_model=Player, related_name='Player_home_player_8_set', to_field='player_api')
    home_player_9 = ForeignKeyField(db_column='home_player_9', null=True, rel_model=Player, related_name='Player_home_player_9_set', to_field='player_api')
    home_player_x1 = IntegerField(db_column='home_player_X1', null=True)
    home_player_x10 = IntegerField(db_column='home_player_X10', null=True)
    home_player_x11 = IntegerField(db_column='home_player_X11', null=True)
    home_player_x2 = IntegerField(db_column='home_player_X2', null=True)
    home_player_x3 = IntegerField(db_column='home_player_X3', null=True)
    home_player_x4 = IntegerField(db_column='home_player_X4', null=True)
    home_player_x5 = IntegerField(db_column='home_player_X5', null=True)
    home_player_x6 = IntegerField(db_column='home_player_X6', null=True)
    home_player_x7 = IntegerField(db_column='home_player_X7', null=True)
    home_player_x8 = IntegerField(db_column='home_player_X8', null=True)
    home_player_x9 = IntegerField(db_column='home_player_X9', null=True)
    home_player_y1 = IntegerField(db_column='home_player_Y1', null=True)
    home_player_y10 = IntegerField(db_column='home_player_Y10', null=True)
    home_player_y11 = IntegerField(db_column='home_player_Y11', null=True)
    home_player_y2 = IntegerField(db_column='home_player_Y2', null=True)
    home_player_y3 = IntegerField(db_column='home_player_Y3', null=True)
    home_player_y4 = IntegerField(db_column='home_player_Y4', null=True)
    home_player_y5 = IntegerField(db_column='home_player_Y5', null=True)
    home_player_y6 = IntegerField(db_column='home_player_Y6', null=True)
    home_player_y7 = IntegerField(db_column='home_player_Y7', null=True)
    home_player_y8 = IntegerField(db_column='home_player_Y8', null=True)
    home_player_y9 = IntegerField(db_column='home_player_Y9', null=True)
    home_team_api = ForeignKeyField(db_column='home_team_api_id', null=True, rel_model=Team, related_name='Team_home_team_api_set', to_field='team_api')
    home_team_goal = IntegerField(null=True)
    league = ForeignKeyField(db_column='league_id', null=True, rel_model=League, to_field='id')
    match_api = IntegerField(db_column='match_api_id', null=True, unique=True)
    possession = TextField(null=True)
    season = TextField(null=True)
    shotoff = TextField(null=True)
    shoton = TextField(null=True)
    stage = IntegerField(null=True)

    class Meta:
        db_table = 'Match'

class PlayerAttributes(BaseModel):
    acceleration = IntegerField(null=True)
    aggression = IntegerField(null=True)
    agility = IntegerField(null=True)
    attacking_work_rate = TextField(null=True)
    balance = IntegerField(null=True)
    ball_control = IntegerField(null=True)
    crossing = IntegerField(null=True)
    curve = IntegerField(null=True)
    date = TextField(null=True)
    defensive_work_rate = TextField(null=True)
    dribbling = IntegerField(null=True)
    finishing = IntegerField(null=True)
    free_kick_accuracy = IntegerField(null=True)
    gk_diving = IntegerField(null=True)
    gk_handling = IntegerField(null=True)
    gk_kicking = IntegerField(null=True)
    gk_positioning = IntegerField(null=True)
    gk_reflexes = IntegerField(null=True)
    heading_accuracy = IntegerField(null=True)
    interceptions = IntegerField(null=True)
    jumping = IntegerField(null=True)
    long_passing = IntegerField(null=True)
    long_shots = IntegerField(null=True)
    marking = IntegerField(null=True)
    overall_rating = IntegerField(null=True)
    penalties = IntegerField(null=True)
    player_api = ForeignKeyField(db_column='player_api_id', null=True, rel_model=Player, to_field='player_api')
    player_fifa_api = ForeignKeyField(db_column='player_fifa_api_id', null=True, rel_model=Player, related_name='Player_player_fifa_api_set', to_field='player_fifa_api')
    positioning = IntegerField(null=True)
    potential = IntegerField(null=True)
    preferred_foot = TextField(null=True)
    reactions = IntegerField(null=True)
    short_passing = IntegerField(null=True)
    shot_power = IntegerField(null=True)
    sliding_tackle = IntegerField(null=True)
    sprint_speed = IntegerField(null=True)
    stamina = IntegerField(null=True)
    standing_tackle = IntegerField(null=True)
    strength = IntegerField(null=True)
    vision = IntegerField(null=True)
    volleys = IntegerField(null=True)

    class Meta:
        db_table = 'Player_Attributes'

class TeamAttributes(BaseModel):
    buildupplaydribbling = IntegerField(db_column='buildUpPlayDribbling', null=True)
    buildupplaydribblingclass = TextField(db_column='buildUpPlayDribblingClass', null=True)
    buildupplaypassing = IntegerField(db_column='buildUpPlayPassing', null=True)
    buildupplaypassingclass = TextField(db_column='buildUpPlayPassingClass', null=True)
    buildupplaypositioningclass = TextField(db_column='buildUpPlayPositioningClass', null=True)
    buildupplayspeed = IntegerField(db_column='buildUpPlaySpeed', null=True)
    buildupplayspeedclass = TextField(db_column='buildUpPlaySpeedClass', null=True)
    chancecreationcrossing = IntegerField(db_column='chanceCreationCrossing', null=True)
    chancecreationcrossingclass = TextField(db_column='chanceCreationCrossingClass', null=True)
    chancecreationpassing = IntegerField(db_column='chanceCreationPassing', null=True)
    chancecreationpassingclass = TextField(db_column='chanceCreationPassingClass', null=True)
    chancecreationpositioningclass = TextField(db_column='chanceCreationPositioningClass', null=True)
    chancecreationshooting = IntegerField(db_column='chanceCreationShooting', null=True)
    chancecreationshootingclass = TextField(db_column='chanceCreationShootingClass', null=True)
    date = TextField(null=True)
    defenceaggression = IntegerField(db_column='defenceAggression', null=True)
    defenceaggressionclass = TextField(db_column='defenceAggressionClass', null=True)
    defencedefenderlineclass = TextField(db_column='defenceDefenderLineClass', null=True)
    defencepressure = IntegerField(db_column='defencePressure', null=True)
    defencepressureclass = TextField(db_column='defencePressureClass', null=True)
    defenceteamwidth = IntegerField(db_column='defenceTeamWidth', null=True)
    defenceteamwidthclass = TextField(db_column='defenceTeamWidthClass', null=True)
    team_api = ForeignKeyField(db_column='team_api_id', null=True, rel_model=Team, to_field='team_api')
    team_fifa_api = ForeignKeyField(db_column='team_fifa_api_id', null=True, rel_model=Team, related_name='Team_team_fifa_api_set', to_field='team_fifa_api')

    class Meta:
        db_table = 'Team_Attributes'

class SqliteSequence(BaseModel):
    name = UnknownField(null=True)  #
    seq = UnknownField(null=True)  #

    class Meta:
        db_table = 'sqlite_sequence'
        primary_key = False

