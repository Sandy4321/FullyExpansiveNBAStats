import requests


class NBABroadHeadlines:

    def __init__(self):
        self.url = 'http://stats.nba.com/feeds/StatsBeyondTheNumbersV2-594371/json.js'

        self.data = requests.get(self.url)

    def convert_to_dict(self):
        return {entry['ListItemCaption']: [entry['ListItemLink'], entry['ListItemPubDate'], entry['ListItemCaption']]
                for entry in self.data.json()['ListItems']}




c = NBABroadHeadlines()
