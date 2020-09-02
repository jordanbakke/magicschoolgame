import magicschoolgame.cards

class Player:

    nPlayers = 0
    player_list = []

    def __init__ (self, IRL_Name, Hero_Name, Health, Influence, Attack, Deck, Hand, Played, Discard):
        self.n = nPlayers + 1
        nPlayers += 1
        player_list += [self]

        self.attack = Attack
        self.influence = Influence
        self.health = Health
        self.name = IRL_Name
        self.hero_name = Hero_Name
        self.deck = Deck
        self.hand = Hand
        self.played = Played
        self.discard = Discard

def initialize(config):
    '''
    So far, this function is only able to deal with the kind of configuration represented in test_unlock
    '''
    j = 1
    Player1 = None
    Player2 = None
    Player3 = None
    Player4 = None
    players = [Player1, Player2, Player3, Player4]
    Deck = []
    Hand = []

    for i in config["players"]:
        players[j] = Player(i, config[i]["hero"], 10, 0, 0, [], [], [], [])
        j += 1

def do_transition(old_state, transition):
    game_state = {}