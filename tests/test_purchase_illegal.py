import magicschoolgame.rules
import yaml

TRANSITIONS = yaml.safe_load('''
- [purchase, 0]
''')

INITIAL_STATE = yaml.safe_load('''
players:
    alice:
        hero: hairy
        hearts: 10
        influence: 1
        attacks: 0
        deck: [chameleon skin, hairy's broom, unlock, unlock, unlock]
        hand: [hairy's owl]
        played cards: [unlock, unlock, unlock, unlock]
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

shop: [big balls, elusive ball, groundskeeper, illuminate, illuminate, repair]

turn order: [alice, bob]
current player: alice
phase: [[hero actions]]
''')

def test_purchase_illegal():
    state = INITIAL_STATE
    for transition in TRANSITIONS:
        transition = magicschoolgame.rules.do_transition(state, transition)
    assert isinstance(state, magicschoolgame.rules.Illegal)
