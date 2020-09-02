import magicschoolgame.cards

class Player:

    nPlayers = 0
    player_list = []

    def __init__ (self, IRL_Name, Hero_Name, Health, Influence, Attack, Deck, Hand, Played, Discard):
        self.n = Player.nPlayers + 1
        Player.nPlayers += 1
        Player.player_list += [self]

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
    j = 0
    Player1 = None
    Player2 = None
    Player3 = None
    Player4 = None
    players = [Player1, Player2, Player3, Player4]
    Deck = []
    Hand = []
    game_state = {"players" : {}, "turn order" : config["turn order"], "current player" : config["turn order"][0], "phase" : [["hero actions"]]}

    for i in config["players"]:
        Deck = magicschoolgame.cards.HERO_TO_STARTER_DECK[config[players][i]["hero"]]

        Hand = [Deck[h] for h in range(len(Deck)) if h in config[players][i]["hand"]]
        Deck = [Deck[h] for h in range(len(Deck)) if h not in config[players][i]["hand"]]

        players[j] = Player(i, config[players][i]["hero"], 10, 0, 0, Deck, Hand, [], [])
        j += 1

    for i in players:
        if i:
            game_state["players"][i.name] = {
                "hero" : i.hero_name,
                "hearts" : i.health,
                "influence" : i.influence,
                "attacks" : i.attack,
                "deck" : i.deck,
                "hand" : i.hand,
                "played cards" : i.played,
                "discard" : i.discard
            }

    return game_state

def do_transition(old_state, transition):
    game_state = {}
