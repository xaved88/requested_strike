class CustomState:
    attacks_played_this_turn = 0
    extra_ritual_dagger_damage_by_card = dict()

    # for test purposes
    extra_ritual_dagger_damage_by_card.update({"test_uuid_powered_up_ritual_dagger": 3})


def set_new_game_state():
    CustomState.attacks_played_this_turn = 0
    CustomState.extra_ritual_dagger_damage_by_card.clear()


def set_new_turn_state():
    CustomState.attacks_played_this_turn = 0