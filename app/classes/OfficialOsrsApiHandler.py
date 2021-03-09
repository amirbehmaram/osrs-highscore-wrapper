# Regular imports
import requests

# Custom classes importing
from .PlayerDataDecoder import PlayerDataDecoder

######################################################################################################
#### Class for interacting with the actual OSRS API
#### located here: https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=darkstar1405
######################################################################################################
class OsrsApiHandler:

    base_url = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws'
    
    # Get all the info from the API corresponding to the player_name
    def get_player(self, player_name):

        player_request = requests.get(self.base_url + '?player=' + player_name)

        if player_request:
            decoder = PlayerDataDecoder()
            return decoder.decode_player_data(player_request.text)
        else :
            return 'Error with request!'


    



