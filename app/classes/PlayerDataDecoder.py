from flask import Flask
import logging
import json

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

######################################################################################################
#### The response from the OSRS API is just a string where groups of data are separated by spaces
#### and then for each spaced item, then are separated by commas.
######################################################################################################
class PlayerDataDecoder:

    skill_order_dict = dict({
        0: 'overall',
        1: 'attack',
        2: 'defence',
        3: 'strength',
        4: 'hitpoints',
        5: 'ranged',
        6: 'prayer',
        7: 'magic',
        8: 'cooking',
        9: 'woodcutting',
        10: 'fletching',
        11: 'fishing',
        12: 'firemaking',
        13: 'crafting',
        14: 'smithing',
        15: 'mining',
        16: 'herblore',
        17: 'agility',
        18: 'thieving',
        19: 'slayer',
        20: 'farming',
        21: 'runecrafting',
        22: 'hunter',
        23: 'construction',
        24: 'easyClueScrolls',
        25: 'mediumClueScrolls',
        26: 'clueScrolls',
        27:  'bountyHunter',
        28: 'bountyHunterRogues',
        29: 'hardClueScrolls',
        30: 'lastManStanding',
        31: 'eliteClueScrolls',
        32: 'masterClueScrolls'
    })

    skill_dict = dict({
        'overall': { 'rank': '', 'level': '', 'experience': '' },
        'attack': { 'rank': '', 'level': '', 'experience': '' },
        'defence': { 'rank': '', 'level': '', 'experience': '' },
        'strength': { 'rank': '', 'level': '', 'experience': '' },
        'hitpoints': { 'rank': '', 'level': '', 'experience': '' },
        'ranged': { 'rank': '', 'level': '', 'experience': '' },
        'prayer': { 'rank': '', 'level': '', 'experience': '' },
        'magic': { 'rank': '', 'level': '', 'experience': '' },
        'cooking': { 'rank': '', 'level': '', 'experience': '' },
        'woodcutting': { 'rank': '', 'level': '', 'experience': '' },
        'fletching': { 'rank': '', 'level': '', 'experience': '' },
        'fishing': { 'rank': '', 'level': '', 'experience': '' },
        'firemaking': { 'rank': '', 'level': '', 'experience': '' },
        'crafting': { 'rank': '', 'level': '', 'experience': '' },
        'smithing': { 'rank': '', 'level': '', 'experience': '' },
        'mining': { 'rank': '', 'level': '', 'experience': '' },
        'herblore': { 'rank': '', 'level': '', 'experience': '' },
        'agility': { 'rank': '', 'level': '', 'experience': '' },
        'thieving': { 'rank': '', 'level': '', 'experience': '' },
        'slayer': { 'rank': '', 'level': '', 'experience': '' },
        'farming': { 'rank': '', 'level': '', 'experience': '' },
        'runecrafting': { 'rank': '', 'level': '', 'experience': '' },
        'hunter': { 'rank': '', 'level': '', 'experience': '' },
        'construction': { 'rank': '', 'level': '', 'experience': '' },
        'easyClueScrolls': { 'rank': '', 'score': '' },
        'mediumClueScrolls': { 'rank': '', 'score': '' },
        'clueScrolls': { 'rank': '', 'score': '' },
        'bountyHunter': { 'rank': '', 'score': '' },
        'bountyHunterRogues': { 'rank': '', 'score': '' },
        'hardClueScrolls': { 'rank': '', 'score': '' },
        'lastManStanding': { 'rank': '', 'score': '' },
        'eliteClueScrolls': { 'rank': '', 'score': '' },
        'masterClueScrolls': { 'rank': '', 'score': '' },
    })    
    
    # Get all the info from the API corresponding to the player_name
    def decode_player_data(self, player_data_str):

        if (player_data_str):

            # Split the full data string into a list where each entry represents 
            # a skill and its corresponding values
            split_data = player_data_str.splitlines()

            if split_data:

                # Loop over our split data and capturing the index
                for index in range(len(split_data)):

                    # There are a whole bunch of Boss scores after 32, I don't care about those right now.
                    if index < 33:

                        # Clone our dictionaries
                        skill_dict = self.skill_dict
                        skill_order_dict = self.skill_order_dict

                        # Split this current skills data into a list
                        split_skill_data = split_data[index].split(',')

                        if split_skill_data:

                            if index < 24:

                                for skill_index in range(len(split_skill_data)):
                                    if skill_index == 0:
                                        skill_dict[skill_order_dict[index]]['rank'] = split_skill_data[skill_index]
                                    elif skill_index == 1:
                                        skill_dict[skill_order_dict[index]]['level'] = split_skill_data[skill_index]
                                    else:
                                        skill_dict[skill_order_dict[index]]['experience'] = split_skill_data[skill_index]
                            
                            else:
                                
                                for skill_index in range(len(split_skill_data)):
                                    if skill_index == 0:
                                        skill_dict[skill_order_dict[index]]['rank'] = split_skill_data[skill_index]
                                    else:
                                        skill_dict[skill_order_dict[index]]['score'] = split_skill_data[skill_index]

                # Logger for debugging
                #app.logger.info(skill_dict)

        return json.dumps(skill_dict, indent = 4)
