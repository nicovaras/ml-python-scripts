import json
from models import Player
from peewee import SqliteDatabase
import requests
from bs4 import BeautifulSoup


def get_nation_from(n):
    url = 'http://football-data.mx-api.enetscores.com/page/xhr/player/' + str(n) + '/0/1/extended/'
    bs = BeautifulSoup(requests.get(url).content, 'html.parser')
    return bs.find_all(class_='mx-break-micro')[1].text.strip()


def save(d):
    f = open('nationalities.json', 'w')
    f.write(json.dumps(d))
    f.close()


if __name__ == '__main__':
    db = SqliteDatabase('database.sqlite')
    nationalities = {}
    for p in Player.select():
        nationalities[p.player_api] = get_nation_from(p.player_api)
        save(nationalities)
