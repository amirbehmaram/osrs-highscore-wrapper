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

    if player_name:
        api_handler = OsrsApiHandler()
        data = api_handler.get_player(player_name)

        return data
