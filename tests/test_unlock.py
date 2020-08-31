import magicschoolgame.rules
import yaml

CONFIG = yaml.safe_load('''
players:
    alice:
        hero: hairy
        hand: [9, 3, 7, 2, 8]
    bob:
        hero: weasel boy
        hand: [6, 9, 3, 7, 1]

turn order: [alice, bob]
''')

TRANSITIONS = yaml.safe_load('''
- [play card, 1]
- [play card, 2]
''')

FINAL_STATE = yaml.safe_load('''
players:
    alice:
        hero: hairy
        hearts: 10
        influence: 2
        attacks: 0
        deck: [chameleon skin, hairy's broom, unlock, unlock, unlock]
        hand: [hary's owl, unlock, unlock]
        played cards: [unlock, unlock]
        discard: []
    bob:
        hero: weasel boy
        hearts: 10
        influence: 0
        attacks: 0
        deck: [mystery beans, unlock, unlock, unlock, weasel's broom]
        hand: [unlock,  unlock, unlock, unlock, weasel's owl]
        played cards: []
        discard: []

turn order: [alice, bob]
current player: alice
phase: [[hero actions]]
''')

def test_unlock():
    state = magicschoolgame.rules.initialize(CONFIG)
    for transition in TRANSITIONS:
        transition = magicschoolgame.rules.do_transition(state, transition)
    assert state == FINAL_STATE
