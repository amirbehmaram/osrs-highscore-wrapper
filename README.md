# OSRS Highscore API Wrapper
This idea came about after doing some reasearch on a similar project and coming across the current format of the OSRS
highscore API results and how unclear the results are initially.

The wrapper should provide some basic endpoints to return highscore data in a more descriptive JSON format. 

## Local Development

This project is built using (flask)[https://flask.palletsprojects.com/en/1.1.x/]. Follow their (installation)[https://flask.palletsprojects.com/en/1.1.x/installation/#installation] guide to get things setup.

To run the app locally:

1) Export our app so Flask can use it: `export FLASK_APP=main.py`
2) Activate the virtual environment with `. venv/bin/activate`
3) Then use `flask run` to start the 

## Endpoints

The endpoints will be documented as this project progresses.

### Home
Base API URL. Returns a simple HTML page about the application.

__URL__: `/`

__Method__: `GET`

---
### Player
Returns all of the player's stats and rankings.

__URL__: `/api/v1/player?player_name=example`

__URL Parameters__: `player_name` is a string representing the OSRS player you'd like to retreive information on.

__Method__: `GET`

#### Success Response

__Condition__: playerName is a valid OSRS player name

__Code__: `200 OK`

__Example__: 
```json
"data":"[
  {
    "rank":"1469527",
    "level":"848",
    "xp":"2840563"
  },
  {
    "rank":"1223120",
    "level":"63",
    "xp":"372297"
  },
  ...,
  {
    "rank":"",
    "level":"",
    "xp":""
  }
  ]",
  "status":200
}
```
---

## Development
This app is hosted on Heroku and uses the Heroku cli to deploy updates.

## Other Info

### Loging
Heroku keeps logs running on the production server that can be view by running `heroku logs --tail`

### Reference
Just for reference, this is the order that skills are received from the official OSRS API.

  overall: { rank: "", level: "", experience: "" }

  attack: { rank: "", level: "", experience: "" }

  defence: { rank: "", level: "", experience: "" }

  strength: { rank: "", level: "", experience: "" }

  hitpoints: { rank: "", level: "", experience: "" }

  ranged: { rank: "", level: "", experience: "" }

  prayer: { rank: "", level: "", experience: "" }

  magic: { rank: "", level: "", experience: "" }

  cooking: { rank: "", level: "", experience: "" }

  woodcutting: { rank: "", level: "", experience: "" }

  fletching: { rank: "", level: "", experience: "" }

  fishing: { rank: "", level: "", experience: "" }

  firemaking: { rank: "", level: "", experience: "" }

  crafting: { rank: "", level: "", experience: "" }

  smithing: { rank: "", level: "", experience: "" }

  mining: { rank: "", level: "", experience: "" }

  herblore: { rank: "", level: "", experience: "" }

  agility: { rank: "", level: "", experience: "" }

  thieving: { rank: "", level: "", experience: "" }

  slayer: { rank: "", level: "", experience: "" }

  farming: { rank: "", level: "", experience: "" }

  runecrafting: { rank: "", level: "", experience: "" }

  hunter: { rank: "", level: "", experience: "" }

  construction: { rank: "", level: "", experience: "" }

  easyClueScrolls: { rank: "", score: "" }

  mediumClueScrolls: { rank: "", score: "" }

  clueScrolls: { rank: "", score: "" }

  bountyHunter: { rank: "", score: "" }

  bountyHunterRogues: { rank: "", score: "" }

  hardClueScrolls: { rank: "", score: "" }

  lastManStanding: { rank: "", score: "" }

  eliteClueScrolls: { rank: "", score: "" }

  masterClueScrolls: { rank: "", score: "" }

