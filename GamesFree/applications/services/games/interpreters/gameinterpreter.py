import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from entities.game import Game

class GameInterpreter():
    
    def interpret(self, raw_game):
        title = raw_game["title"]        
        return Game(title)