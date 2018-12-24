#!/usr/bin/env python
import requests
import django
import os

# Need to properly set DJANGO_SETTINGS_MODULE environment variable in order to properly alter SQLite database
os.environ['DJANGO_SETTINGS_MODULE'] = 'nba_app.settings'
django.setup()



# from nba.models import Player
# from nba.models import Profile
from nba.models import Team



# URLs all have the same base address. Only thing that changes is filepath
# which is all kept in urls dictionary
base = 'http://data.nba.net/10s'
urls = {
	'teams': '/prod/v2/2018/teams.json',
	'players': '/prod/v2/2018/players.json',
	'player_profile': '/prod/v1/{year}/players/{personId}_profile.json'
}



def initialize_db():
	get_teams()
	# get_players()
	# get_profiles()




'''
	Gets the list of NBA teams from the data source and has the corresponding fields
	that match with team model
'''
def get_teams():

	req = requests.get( base+urls['teams'] )
	res = req.json()

	teams = res['league']['standard']

	for t in teams:

		if t['isNBAFranchise']:
			print('Uploading ' + t['fullName'] + ' to database')

			team = Team(
				teamId = t['teamId'],
				city = t['city'],
				full_name = t['fullName'],
				nickname = t['nickname'],
				tricode = t['tricode'],
				conference = t['confName'],
				divison = t['divName']
			)

			# Save into database. Changes should be reflected.
			team.save()


			print('Done uploading')


# def get_players():
# 	req = requests.get(base + urls['players'])
# 	res = req.json()
# 	players = req['league']['standard']

# def get_profiles():

initialize_db()