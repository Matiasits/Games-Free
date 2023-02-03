import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gameclient import GamesClient
from entities.freegames import FreeGames
from gameinterpreter import GameInterpreter

class FreeGamesInterpreter():
    
    def interpret(self):
        gameinterpreter = GameInterpreter()
        client = GamesClient()
        response = client.get_freegames_response()
    
        current_json = response['current']
        upcoming_json = response['upcoming']
        
        current = [ gameinterpreter.interpret(game) for game in current_json ]
        upcoming = [ gameinterpreter.interpret(game) for game in upcoming_json]
        
        return FreeGames(current, upcoming)

