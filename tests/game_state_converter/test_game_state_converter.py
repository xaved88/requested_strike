import unittest

from test_helpers.resources import load_resource_state


class GameStateConverterTest(unittest.TestCase):

    def test_loading_all_potions(self):
        state = load_resource_state("other/combat_reward_full_potions.json")
        potions = state.get_held_potion_names() + state.get_reward_potion_names()
        self.assertEqual(['cultist potion', 'speed potion', 'power potion', 'ancient potion'], potions)

    def test_get_relic_counter(self):
        state = load_resource_state("campfire/campfire_girya_lift.json")
        counter = state.get_relic_counter("Girya")
        self.assertEqual(0, counter)

    def test_get_relic_counter_failure(self):
        state = load_resource_state("campfire/campfire_rest.json")
        counter = state.get_relic_counter("Girya")
        self.assertEqual(False, counter)

    def test_get_choice_list(self):
        state = load_resource_state("card_reward/card_reward_skip_upgraded_card_because_amount.json")
        choices = state.get_choice_list()
        self.assertEqual(['pommel strike', 'heel hook', 'twin strike+'], choices)

    def test_get_choice_list_upgrade_stripped_from_choice(self):
        state = load_resource_state("card_reward/card_reward_skip_upgraded_card_because_amount.json")
        choices = state.get_choice_list_upgrade_stripped_from_choice()
        self.assertEqual(['pommel strike', 'heel hook', 'twin strike'], choices)

    def test_get_deck_card_list(self):
        state = load_resource_state("card_reward/card_reward_skip_because_amount_and_some_in_deck_are_upgraded.json")
        deck_list = state.get_deck_card_list()
        self.assertEqual({'bash+': 1, 'defend': 4, 'strike': 3, 'twin strike': 1, 'twin strike+': 1}, deck_list)

    def test_get_deck_card_list_upgrade_stripped_from_name(self):
        state = load_resource_state("card_reward/card_reward_skip_because_amount_and_some_in_deck_are_upgraded.json")
        deck_list = state.get_deck_card_list_upgrade_stripped_from_name()
        self.assertEqual({'bash': 1, 'defend': 4, 'strike': 3, 'twin strike': 2}, deck_list)
