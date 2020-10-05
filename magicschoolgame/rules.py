import magicschoolgame.cards
import random

class Player:

    nPlayers = 0
    player_list = []

    def __init__ (self, IRL_Name = "", Hero_Name = "", Health = -1, Influence = -1, Attack = -1, Deck = [], Hand = [], Played = [], Discard = []):
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

    def init_from_state (self, player_state):
        '''
        takes player state in terms of part of a game state as input and assigns all class members accordingly
        '''
        self.attack = player_state["attacks"]
        self.influence = player_state["influence"]
        self.health = player_state["hearts"]
        self.hero_name = player_state["hero"]
        self.deck = player_state["deck"]
        self.hand = player_state["hand"]
        self.played = player_state["played cards"]
        self.discard = player_state["discard"]

        return self

    def quickTest(self):
        pass

    def drawCards(self, n = 1):

        for i in range(0, n):
            self.hand += [self.deck.pop(random.randint(0, len(self.deck)-1))]

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
        Deck = magicschoolgame.cards.HERO_TO_STARTER_DECK[config["players"][i]["hero"]]

        Hand = [Deck[h] for h in range(len(Deck)) if h in config["players"][i]["hand"]]
        Deck = [Deck[h] for h in range(len(Deck)) if h not in config["players"][i]["hand"]]

        players[j] = Player(i, config["players"][i]["hero"], 10, 0, 0, Deck, Hand, [], [])
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
    '''
    So far, this function is only able to deal with the kind of configuration represented in test_unlock
    '''
    #this section initializes all of the objects

    new_state = old_state
    
    players = {k: Player(k).init_from_state(v) for k, v in old_state["players"].items()}
    current_player = players[old_state["current player"]]

    #now for the transitions

    if type(transition) is not list:
        raise Exception("transition is not in proper format") 

    if transition[0] == "play card":
        card = magicschoolgame.cards.CARD_OBJECTS[current_player.hand[transition[1]]]
        card.play(current_player)
        current_player.played += [current_player.hand.pop(transition[1])]

        current_player.deck.sort()
        current_player.hand.sort()
        current_player.played.sort()
        current_player.discard.sort()

    elif transition[0] == "purchase":
        card = magicschoolgame.cards.CARD_OBJECTS[old_state["shop"][transition[1]]]

        if current_player.influence < card.cost:
            raise Exception("Current Player is make")

        current_player.discard += [old_state["shop"].pop(transition[1])]

        #This line will be replaced with a line that finds the cost of the card, but as of now that is not stored anywhere
        current_player.influence -= card.cost

    for k, v in players.items():
        new_state["players"][k] = {
            "hero" : v.hero_name,
            "hearts" : v.health,
            "influence" : v.influence,
            "attacks" : v.attack,
            "deck" : v.deck,
            "hand" : v.hand,
            "played cards" : v.played,
            "discard" : v.discard
        }
    
    new_state["shop"] = old_state["shop"]

    return new_state