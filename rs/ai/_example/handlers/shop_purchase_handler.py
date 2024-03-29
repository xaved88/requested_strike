from typing import List

from config import presentation_mode, p_delay, p_delay_s
from rs.game.screen_type import ScreenType
from rs.machine.handlers.handler import Handler
from rs.machine.state import GameState

standard_cards_to_purge: list[str] = [
    'Strike',
    'Defend',
    'Strike+',
    'Defend+',
]


# TODO -> find a nice way to configure this and extract it to commons
class ShopPurchaseHandler(Handler):

    def __init__(self):
        self.relics_to_buy = [
            'Kunai',
            'Shuriken',
            'Ornamental Fan',
            'Preserved Insect',
            'Bag of Marbles',
            'Pen Nib',
            'Toxic Egg',
            'Orichalcum',
            'Torii',
            'Vajra',
            'Eternal Feather',
            'Meal Ticket',
            'Anchor',
            'Horn Cleat',
            'Bronze Scales',
        ]

        self.cards_to_buy = [
            "Perfected Strike",
            "Accuracy",
            "Blade Dance",
        ]

    def can_handle(self, state: GameState) -> bool:
        return state.screen_type() == ScreenType.SHOP_SCREEN.value

    def handle(self, state: GameState) -> List[str]:
        choice = self.find_choice(state)
        if choice:
            idx = state.get_choice_list().index(choice)
            if presentation_mode:
                return [p_delay, "choose " + str(idx), p_delay_s, "wait 30"]
            return ["choose " + str(idx), "wait 30"]
        if presentation_mode:
            return ["wait " + p_delay, "return", "proceed"]
        return ["return", "proceed"]

    def find_choice(self, state: GameState) -> str:
        gold = state.game_state()['gold']
        screen_state = state.game_state()['screen_state']
        can_purge = screen_state['purge_available'] and gold >= screen_state['purge_cost']

        # 1. Kunai/Shuriken
        for relic in screen_state['relics']:
            if relic['name'] == 'Kunai' and gold >= relic['price']:
                return "kunai"

        for relic in screen_state['relics']:
            if relic['name'] == 'Shuriken' and gold >= relic['price']:
                return "shuriken"

        # 2. Purge curses
        if can_purge and state.deck.contains_curses():
            return "purge"

        # 3. Kunai/Shuriken
        for relic in screen_state['relics']:
            if relic['name'] == 'Kunai' and gold >= relic['price']:
                return "kunai"

        for relic in screen_state['relics']:
            if relic['name'] == 'Shuriken' and gold >= relic['price']:
                return "shuriken"

        # 4. Membership Card
        for relic in screen_state['relics']:
            if relic['name'] == 'Membership Card' and gold >= relic['price']:
                return "membership card"

        # 5. Kunai/Shuriken
        for relic in screen_state['relics']:
            if relic['name'] == 'Kunai' and gold >= relic['price']:
                return "kunai"

        for relic in screen_state['relics']:
            if relic['name'] == 'Shuriken' and gold >= relic['price']:
                return "shuriken"

        # 6. Cards based on list
        deck_card_list = state.get_deck_card_list()
        for p in self.cards_to_buy:
            for card in screen_state['cards']:
                if card['id'] == p and gold >= card['price']:
                    if p.lower not in deck_card_list:
                        return card['name'].lower()

        # 7. Relics based on list
        for p in self.relics_to_buy:
            for relic in screen_state['relics']:
                if relic['name'] == p and gold >= relic['price']:
                    return relic['name'].lower()

        # 8. Purge in general
        # Would be nicer to not essentially duplicate the list from purge_handler.py here but oh well. Note: NAMES here, not IDs.
        if can_purge and state.deck.contains_cards(standard_cards_to_purge):
            return "purge"

        # Nothing we want / can afford, leave.
        return ''
