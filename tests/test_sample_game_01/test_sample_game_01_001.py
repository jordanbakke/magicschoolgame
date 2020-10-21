
import magicschoolgame.rules
import yaml

TRANSITIONS = yaml.safe_load('''
- - reveal evildoer
  - 1

''')

INITIAL_STATE = yaml.safe_load('''
evildoers active: []
evildoers reserve: [dragon boy, dragon's cronies, two-face]

evildoings active: []
evildoings reserve: [ breathe fire, breathe fire, breathe fire, knockback,
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
phase: [[reveal evildoer], [reveal evildoing]]

''')

FINAL_STATE = yaml.safe_load('''
evildoers active: [dragon's cronies]
evildoers reserve: [dragon boy, two-face]

evildoings active: []
evildoings reserve: [ breathe fire, breathe fire, breathe fire, knockback,
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
phase: [[reveal evildoing]]

''')

def test_sample_game_01_001():
    state = INITIAL_STATE
    for transition in TRANSITIONS:
        state = magicschoolgame.rules.do_transition(state, transition)
    assert state == FINAL_STATE 
