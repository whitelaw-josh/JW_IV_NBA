from nba_api.stats.static import players as p
from nba_api.stats.endpoints import playercareerstats as pcs
import pandas as pd

# useful for id, first_name, last_name
players_df = pd.DataFrame(p.get_active_players())
# players_df[['id', 'first_name', 'last_name']]

# player = pcs.PlayerCareerStats(player_id = 2544)
# put ids into PlayerCareerStats checkker to grab career stats of all
# use BoxScoreTraditional library to start with for good base stats; use above 2 comments for help to start
