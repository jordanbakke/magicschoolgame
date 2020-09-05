class HogwartsCard:
    
    def __init__ (self, Type = None, Effect1 = None, Effect2 = None, Condition1 = None, Condition2 = None, inHandEffect = None, Special = None):
        self.type = Type
        self.effect1 = Effect1
        self.effect2 = Effect2
        self.condition1 = Condition1
        self.condition2 = Condition2
        self.inhandeffect = inHandEffect
        self.special = Special
        #condition1 triggers effect1 and condition2 triggers effect2

    def evalConditions(self):
        '''
        returns a list of two boolean values, representing self.condition1 and self.condition2. Values are true if the consition is met and false otherwise.
        '''
        conditionsMet = [False, False]

        if self.condition1 is None:
            conditionsMet[0] = True

        if self.condition2 is None:
            conditionsMet[1] = True

        print(conditionsMet)

        return conditionsMet

    def play(self, player, tag = None):

        try:
            player.quickTest()
        
        except AttributeError:
            raise Exception("Not a valid player state")

        conditionsMet = self.evalConditions()

        for i in self.effect1:
            if conditionsMet[0]:

                if i[0] == "influence":
                    player.influence += i[1]

                elif i[0] == "attack":
                    player.attack += i[1]

                elif i[0] == "health":
                    player.health += i[1]

                elif i[0] == "card":
                    player.drawCards(i[1])

SUPPLY_DECK = (
        ['big balls'] * 4 +
        ['elusive ball'] +
        ['groundskeeper'] +
        ['headmaster'] +
        ['healing herb'] * 4 +
        ['illuminate'] * 2 +
        ['levitate'] * 3 +
        ['lower'] * 2 +
        ['make fire'] * 4 +
        ['personality test'] +
        ['repair'] * 6 +
        ['team captain']
)

HERO_TO_STARTER_DECK = {
        'hairy': (
            ['chameleon skin'] +
            ['hairy\'s broom'] +
            ['hairy\'s owl'] +
            ['unlock'] * 7
        ),
        'weasel boy': (
            ['mystery beans'] +
            ['unlock'] * 7 +
            ['weasel\'s broom'] +
            ['weasel\'s owl']
        ),
        'nerd girl': (
            ['bardic lore'] +
            ['nerd\'s cat'] +
            ['time machine'] +
            ['unlock'] * 7
        ),
        'forgetter': (
            ['pet toad'] +
            ['reminder'] +
            ['screaming root'] +
            ['unlock'] * 7
        )
}

#Commented cards are not implemented yet

CARD_OBJECTS = {
    #"bardic lore" : #item; {+2 influence} or {+1 influence (all heroes)}
    #"big balls" : #item; +1 attack; +1 heart
    #"chameleon skin" : #item; +1 influence; can't lose >1 heart per evildoing or evildoer
    #"elusive ball" : #item; +2 influence; +1 card
    #"groundskeeper" : #ally; +1 attack; +1 heart (all heroes)
    #"hairy's broom" : #item; +1 attack; {defeat evildoer} triggers {+1 influence}
    #"hairy's owl" : #ally; +1 attack or +2 heart
    #"headmaster" : #ally; {+1 attack; +1 influence; +1 heart; +1 card} (all heroes)
    #"healing herb" : #item; +2 heart (any 1 hero)
    #"illuminate" : #spell; +1 card (all heroes)
    #"lower" : #spell; +2 attack
    #"make fire" : #spell; +1 attack; +1 card
    #"mystery beans" : #item; +1 influence; {play own ally} triggers {+1 attack}
    #"nerd's cat" : #ally; +1 attack or +2 heart
    #"personality test" : #item; +2 influence; when buying ally, may place on top of deck
    #"pet frog" : #ally; +1 attack or +2 heart
    #"reminder" : #item; +1 influence; {discard this} triggers {+2 influence}
    #"repair" : #spell; +2 influence or +1 card
    #"screaming root" : #item; +1 attack or {+2 heart (any 1 hero)}
    #"team captain" : #ally; +1 attack; {defeat evildoer} triggers {+2 heart (any 1 hero)}
    #"time machine" : #item; +1 influence; when buying spell, may place on top of deck
    "unlock" : HogwartsCard("spell", [["influence", 1]])#spell; +1 influence
    #"weasel's broom" : #item; +1 attack; {defeat evildoer} triggers {+1 influence}
    #"weasel's owl" : #ally; +1 attack or +2 heart
}