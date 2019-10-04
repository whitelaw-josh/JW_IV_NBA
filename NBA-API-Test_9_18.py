import requests as r
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

# !!! nba_api.stats.static --> players !!!
# # Find players by full name.
# players.find_players_by_full_name('james')

# # Find players by first name.
# players.find_players_by_first_name('lebron')

# # Find players by last name.
# players.find_players_by_last_name('^(james|love)$')

# Get all players.
# print(players.get_players()) 

# !!! nba_api.stats.static --> players !!!
player = commonplayerinfo.CommonPlayerInfo(player_id = 2544)
print(player.common_player_info.get_json())
