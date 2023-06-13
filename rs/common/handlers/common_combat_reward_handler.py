from typing import List

from config import presentation_mode, p_delay, p_delay_s
from rs.game.screen_type import ScreenType
from rs.machine.command import Command
from rs.machine.handlers.handler import Handler
from rs.machine.state import GameState

# most important on top
default_desired_potions = [
    'fruit juice',
    'fairy in a bottle',
    'focus potion',
    'cultist potion',
    'power potion',
    'potion of capacity',
    'heart of iron',
    'duplication potion',
    'distilled chaos',
    'blessing of the forge',
    'attack potion',
    'dexterity potion',
    'ambrosia',
    'fear potion',
    'essence of steel',
    'strength potion',
    'regen potion',
    'blood potion',
    'entropic brew',
    'liquid bronze',
    'energy potion',
    'skill potion',
    'ancient potion',
    'weak potion',
    'gambler\u0027s brew',
    'poison potion',
    'colorless potion',
    'flex potion',
    'swift potion',
    'bottled miracle',
    'essence of darkness'
    'fire potion',
    'explosive potion',
    'speed potion',
    'block potion',
    'cunning potion',
    'ghost in a jar',
    'stance potion',
    'smoke bomb',
    'elixir potion',
    'liquid memories',
    'snecko oil',
]
default_desired_potions.reverse()


class CommonCombatRewardHandler(Handler):

    def __init__(self, undesired_relics: List[str] = None, desired_potions: List[str] = None):
        self.undesired_relics: List[str] = [] if undesired_relics is None else undesired_relics
        self.desired_potions: List[str] = default_desired_potions if desired_potions is None else desired_potions

    def can_handle(self, state: GameState) -> bool:
        return state.has_command(Command.CHOOSE) \
               and state.screen_type() == ScreenType.COMBAT_REWARD.value

    def handle(self, state: GameState) -> List[str]:

        # Chug a Fruit Juice straight away
        for idx, pot in enumerate(state.get_held_potion_names()):
            if pot == 'fruit juice':
                if presentation_mode:
                    return [p_delay, "potion use " + str(idx), p_delay_s]
                return ["wait 30", "potion use " + str(idx)]

        # Do pickups
        choice = 'did not choose'

        if 'gold' in state.get_choice_list():
            choice = 'gold'

        elif 'stolen_gold' in state.get_choice_list():
            choice = 'stolen_gold'

        elif 'relic' in state.get_choice_list() and state.game_state()["screen_state"]["rewards"][0]["relic"][
            "name"] not in self.undesired_relics:
            choice = 'relic'

        # potentially too fragile check for if the second relic might be desirable even though the first one isn't that I'll leave disabled for safety
        # elif state.get_choice_list().count('relic') >= 1 and \
        #         state.game_state()["screen_state"]["rewards"][1]["relic"]["id"] not in undesired_relics:
        #     choice = '1'

        elif 'potion' in state.get_choice_list():
            if state.are_potions_full():
                all_potions = state.get_held_potion_names() + state.get_reward_potion_names()
                for least_desired_potion in self.desired_potions:
                    if least_desired_potion not in all_potions:
                        continue
                    if least_desired_potion in state.get_reward_potion_names():
                        break
                    for idx, pot in enumerate(state.get_held_potion_names()):
                        if pot == least_desired_potion:
                            return ["wait 30", "potion discard " + str(idx)]

                    # edge-case:
                    # full potions + two waiting potions: one strongly desired (more than our inventory potions), and one not desired (less than our inventory potions)
                    # in this case we will simply ignore the potions instead of juggling to pick up the strongly desired potion

            else:
                choice = 'potion'

        elif 'card' in state.get_choice_list():
            choice = 'card'

        if choice != 'did not choose':
            if presentation_mode:
                return [p_delay, "choose " + choice, p_delay_s]
            return ["choose " + choice]

        return ["proceed"]
