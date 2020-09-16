import magicschoolgame.rules
import yaml

TRANSITIONS = yaml.safe_load('''
- [play card, 0]
''')

INITIAL_STATE = yaml.safe_load('''
players:
    alice:
        hero: hairy
        hearts: 8
        influence: 0
        attacks: 0
        deck: [chameleon skin, hairy's broom, unlock, unlock, unlock, unlock]
        hand: [big balls, hairy's owl, unlock, unlock, unlock]
        played cards: []
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

FINAL_STATE = yaml.safe_load('''
players:
    alice:
        hero: hairy
        hearts: 9
        influence: 0
        attacks: 1
        deck: [chameleon skin, hairy's broom, unlock, unlock, unlock, unlock]
        hand: [hairy's owl, unlock, unlock, unlock]
        played cards: [big balls]
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

def test_big_balls():
    state = INITIAL_STATE
    for transition in TRANSITIONS:
        transition = magicschoolgame.rules.do_transition(state, transition)
    assert state == FINAL_STATE
