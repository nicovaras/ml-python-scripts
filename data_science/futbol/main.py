import json
import pandas as pd
from peewee import SqliteDatabase
from models import Player,Country,League, Team, Match, PlayerAttributes, TeamAttributes
import seaborn as sns
import numpy as np
from matplotlib.pyplot import show
import re

LB_TO_KG_RATIO = 0.453592
DB = SqliteDatabase('database.sqlite')

class Dataset(object):

    def __init__(self):
        self.players = pd.DataFrame(list(Player.select().dicts()))
        self.country = pd.DataFrame(list(Country.select().dicts()))
        self.league = pd.DataFrame(list(League.select().dicts()))
        self.team = pd.DataFrame(list(Team.select().dicts()))
        self.match = pd.DataFrame(list(Match.select().dicts()))
        self.player_attributes = pd.DataFrame(list(PlayerAttributes.select().dicts()))
        self.team_attributes = pd.DataFrame(list(TeamAttributes.select().dicts()))
        self.preprocess()

    def preprocess(self):
        self.add_players_nationalities()
        self.player_weight_to_kg()
        self.players_add_bmi()


    def add_players_nationalities(self):
        nac = json.loads(open('nationalities.json','r').read())
        nac_df = pd.DataFrame(list(nac.items()))
        nac_df.columns = ["player_api", "nationality"]
        nac_df["player_api"] = nac_df["player_api"].astype('int64')
        self.players = self.players.join(nac_df.set_index('player_api'), on="player_api")

    def player_weight_to_kg(self):
        self.players['weight'] = np.round(self.players['weight'] * LB_TO_KG_RATIO)

    def players_add_bmi(self):
        BMI = (self.players['weight']/self.players['height']**2)*10000
        self.players = pd.concat((self.players,BMI.rename('BMI')), axis=1)

def plot_height_vs_weight(df):
    colors = np.array([""]*len(df), dtype=object)
    colors[df['BMI']<25] = '#ff0000'
    colors[df['BMI']>=25] = '#00ff00'
    g = sns.regplot(x="height", y="weight", data=df[['height','weight']], ci=0,
                    scatter_kws={'c':colors,'color':None})
    bmi_x = np.linspace(150,200)
    g.plot(bmi_x, (25*bmi_x**2)/10000, ':k')
    show()

    sns.regplot(x=np.array(range(len(df))), y=np.sort(df['BMI']), fit_reg=False)
    show()

def print_top_bmi(df):
    df_bmi = df[['player_name','height','weight','BMI']]
    low_bmi = df_bmi.sort_values(by='BMI')[:10]
    high_bmi = df_bmi.sort_values(by='BMI', ascending=False)[:10]
    print low_bmi
    print high_bmi

def columns_with_regex(regex,columns):
    ids_regex = re.compile(regex)
    return filter(ids_regex.search, columns)

def filter_matches_with_players(matches, players):
    ids_cols = columns_with_regex(r'(away|home)_player_\d+', matches.columns)
    ids_players = set(players['player_api'])

    filtered_matches_ids = matches.loc[:,ids_cols].apply(
            lambda x: len(ids_players.intersection(set(x))) > 0, axis=1)
    return matches[filtered_matches_ids]

def get_team_of_player_when_playing(home_or_away, id_player, player_df, matches_df, teams_df):
    home_or_away_cols = columns_with_regex(home_or_away + r'_(team.*|player_\d+)',
                                           matches_df.columns) + ['id']
    x = matches_df.loc[:, home_or_away_cols].apply(lambda x: id_player in x.values, axis=1)
    mat = matches_df.ix[x,:]
    if len(mat):
        mat = mat[['id', home_or_away + '_team_api']].join(
                teams_df[['team_long_name','team_api']].set_index('team_api'),
                 on=home_or_away + '_team_api')
        mat['name'] = player_df[player_df.player_api == id_player].player_name.max()
        return mat[['name','team_long_name','id']]
    return pd.DataFrame()

def get_teams_of_players(player_df, matches_df, ds):
    teams_of_player_df = pd.DataFrame()
    for id_player in set(player_df['player_api']):
        teams_of_player_df = pd.concat(
                [teams_of_player_df,
                 get_team_of_player_when_playing('home',
                                                  id_player,
                                                  player_df,
                                                  matches_df,
                                                  ds.team)], ignore_index=True)
        teams_of_player_df = pd.concat(
                [teams_of_player_df,
                 get_team_of_player_when_playing('away',
                                                  id_player,
                                                  player_df,
                                                  matches_df,
                                                  ds.team)], ignore_index=True)
    return teams_of_player_df


if __name__ == '__main__':
    ds = Dataset()

    print ds.league
    print ds.match[['date']].sort('date').min()
    print ds.match[['date']].sort('date').max()


    argentina_df = ds.players[ds.players['nationality'] == 'Argentina']
    argentina_matches_df = filter_matches_with_players(ds.match, argentina_df)

#    plot_height_vs_weight(argentina_df)
#    print_top_bmi(argentina_df)

    teams_of_player_df = get_teams_of_players(argentina_df, argentina_matches_df, ds)
    matches_by_player_count = teams_of_player_df.groupby('name').count().sort_values(by='id', ascending=False)
#    top_number_of_matches = matches_by_player_count.head(10)
#    print top_number_of_matches

    # argentina_matches_df has 1 entry if there is an argentinian player
    # teams_of_player_df  has 1 entry per player per match -> repeated matchs
    matches_with_most_argentinians = teams_of_player_df.groupby('id').count().sort_values(by='name', ascending=False).head(10)
    print matches_with_most_argentinians
    print teams_of_player_df[teams_of_player_df['id']==12119] # inter catania 21-10-2012
    print teams_of_player_df[teams_of_player_df['id']==12247] # inter catania  2013


