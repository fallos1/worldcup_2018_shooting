import requests
import pandas as pd

# World Cup 2018 data for every match
matches = requests.get(
    "https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/43/3.json"
).json()
match_ids = [str(game["match_id"]) for game in matches]

# Output to pandas dataframe
rows = []
for match in matches:
    rows.append(
        {
            "match_id": match["match_id"],
            "home_team": match["home_team"]["home_team_name"],
            "away_team": match["away_team"]["away_team_name"],
        }
    )
# Save to csv
pd.DataFrame(rows).to_csv("matches.csv")

# World Cup 2018 data for every event for every match
url = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/"
match_events = {}
for i in match_ids:
    events = requests.get(url + i + ".json").json()
    match_events[i] = events

# Output to pandas dataframe
rows = []
for key in match_events.keys():
    for event in match_events[key]:
        if event["type"]["name"] == "Shot":
            z_end_location = None
            if len(event["shot"]["end_location"]) > 2:
                z_end_location = event["shot"]["end_location"][2]
            rows.append(
                {
                    "game_id": key,
                    "x_location": event["location"][0],
                    "y_location": event["location"][1],
                    "outcome": event["shot"]["outcome"]["name"],
                    "xg": event["shot"]["statsbomb_xg"],
                    # "player_id": event["player"]["id"],
                    "player": event["player"]["name"],
                    "x_end_location": event["shot"]["end_location"][0],
                    "y_end_location": event["shot"]["end_location"][1],
                    "z_end_location": z_end_location,
                    "minute": event["minute"],
                    "team": event["possession_team"]["name"],
                }
            )

# Save to csv
pd.DataFrame(rows).to_csv("shots.csv")