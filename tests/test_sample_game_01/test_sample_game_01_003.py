
import magicschoolgame.rules
import yaml

TRANSITIONS = yaml.safe_load('''
- - play card
  - 0
  - heart

''')

INITIAL_STATE = yaml.safe_load('''
evildoers active: [dragon's cronies]
evildoers reserve: [dragon boy, two-face]

evildoings active: [breathe fire]
evildoings reserve: [ breathe fire, breathe fire, knockback,
                      knockback, scary name, scary name, scary name,
                      stone state, stone state ]

players:
    hudson:
        hero: forgetter
        hearts: 10
        influence: 0
        attacks: 0
        deck: [pet toad, reminder, unlock, unlock, unlock]
        hand: [screaming root, unlock, unlock, unlock, unlock]
        played cards: []
        discard: []
    jordan:
        hero: hairy
        hearts: 8
        influence: 0
        attacks: 0
        deck: [chameleon skin, hairy's broom, unlock, unlock, unlock]
        hand: [hairy's owl, unlock, unlock, unlock, unlock]
        played cards: []
        discard: []

shop: [big balls, levitate, lower, make fire, make fire, repair]

supply: [ big balls, big balls, big balls, elusive ball, groundskeeper,
          headmaster, healing herb, healing herb, healing herb, healing herb,
          illuminate, illuminate, levitate, levitate, lower, make fire,
          make fire, personality test, repair, repair, repair, repair, repair,
          team captain ]

turn order: [jordan, hudson]
current player: jordan
phase: [[hero actions]]

''')

FINAL_STATE = yaml.safe_load('''
evildoers active: [dragon's cronies]
evildoers reserve: [dragon boy, two-face]

evildoings active: [breathe fire]
evildoings reserve: [ breathe fire, breathe fire, knockback,
                      knockback, scary name, scary name, scary name,
                      stone state, stone state ]

players:
    hudson:
        hero: forgetter
        hearts: 10
        influence: 0
        attacks: 0
        deck: [pet toad, reminder, unlock, unlock, unlock]
        hand: [screaming root, unlock, unlock, unlock, unlock]
        played cards: []
        discard: []
    jordan:
        hero: hairy
        hearts: 10
        influence: 0
        attacks: 0
        deck: [chameleon skin, hairy's broom, unlock, unlock, unlock]
        hand: [unlock, unlock, unlock, unlock]
        played cards: [hairy's owl]
        discard: []

shop: [big balls, levitate, lower, make fire, make fire, repair]

supply: [ big balls, big balls, big balls, elusive ball, groundskeeper,
          headmaster, healing herb, healing herb, healing herb, healing herb,
          illuminate, illuminate, levitate, levitate, lower, make fire,
          make fire, personality test, repair, repair, repair, repair, repair,
          team captain ]

turn order: [jordan, hudson]
current player: jordan
phase: [[hero actions]]

''')

def test_sample_game_01_003():
    state = INITIAL_STATE
    for transition in TRANSITIONS:
        state = magicschoolgame.rules.do_transition(state, transition)
    assert state == FINAL_STATE 
