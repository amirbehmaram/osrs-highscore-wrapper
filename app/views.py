from app import app
from flask import render_template
from flask import request

# Custom classes importing
from .classes import OsrsApiHandler

@app.route("/")
def index():
    return render_template("index.html")


####################################################
#### API Routes
####################################################

@app.route('/api/v1/player')
def get_player_data():
    player_name = request.args.get('player_name')
    specific_skill = request.args.get('skill')

    if player_name and not specific_skill:
        api_handler = OsrsApiHandler()
        json_data = api_handler.get_player(player_name)

        return json_data
    elif player_name and specific_skill:
        api_handler = OsrsApiHandler()
        json_data = api_handler.get_player_skill(player_name, specific_skill)

        return json_data
