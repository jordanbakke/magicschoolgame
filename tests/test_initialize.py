import magicschoolgame.rules
import yaml

CONFIG = yaml.safe_load('''
players:
    alice:
        hero: hairy
        hand: [4, 7, 6, 9, 3]
    bob:
        hero: weasel boy
        hand: [4, 8, 7, 0, 9]
    carol:
        hero: nerd girl
        hand: [9, 8, 7, 6, 0]

turn order: [bob, carol, alice]
''')

FINAL_STATE = yaml.safe_load('''
players:
    alice:
        hero: hairy
        hearts: 10
        influence: 0
        attacks: 0
        deck: [chameleon skin, hairy's broom, hairy's owl, unlock, unlock]
        hand: [unlock, unlock, unlock, unlock, unlock]
        played cards: []
        discard: []
    bob:
        hero: weasel boy
        hearts: 10
        influence: 0
        attacks: 0
        deck: [unlock, unlock, unlock, unlock, unlock]
        hand: [mystery beans, unlock, unlock, weasel's broom, weasel's owl]
        played cards: []
        discard: []
    carol:
        hero: nerd girl
        hearts: 10
        influence: 0
        attacks: 0
        deck: [nerd's cat, time machine, unlock, unlock, unlock]
        hand: [bardic lore, unlock, unlock, unlock, unlock]
        played cards: []
        discard: []

turn order: [bob, carol, alice]
current player: bob
phase: [[hero actions]]
''')

def test_init():
    state = magicschoolgame.rules.initialize(CONFIG)
    assert state == FINAL_STATE
