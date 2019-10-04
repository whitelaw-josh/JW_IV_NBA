import string
from nba_api.stats.static import players as p
from nba_api.stats.endpoints import commonplayerinfo as common

request = ""

while request != "quit":
    # print("Enter player name you wish to lookup: ")
    request = input("Enter player name you wish to lookup: ")

    if request != "quit":
        player =  p.find_players_by_full_name(request)
        print(player)