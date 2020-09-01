import magicschoolgame.cards

class Player:

    nPlayers = 0

    def __init__ (self):
        self.n = nPlayers + 1
        nPlayers += 1

        self.attack = 0
        self.influence = 0
        self.health = 0
        self.name = ""
        self.hero_name = ""
        self.deck = []
        self.hand = []
        self.played = []

def initialize(config):
    pass

def do_transition(old_state, transition):
    game_state = {}