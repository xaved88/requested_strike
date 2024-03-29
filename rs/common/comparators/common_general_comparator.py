from typing import Callable, List

from rs.calculator.battle_state import BattleState
from rs.calculator.interfaces.comparator_interface import ComparatorInterface
from rs.calculator.enums.power_id import PowerId
from rs.common.comparators.core.assessment import ComparatorAssessmentConfig
from rs.common.comparators.core.comparisons import *

Comparison = Callable[[CA, CA], Optional[bool]]

default_comparisons = [
    battle_not_lost,
    battle_is_won,
    most_optimal_winning_battle,
    most_free_early_draw,
    most_free_draw,
    most_lasting_intangible,
    least_incoming_damage_over_1,
    most_dead_monsters,
    most_enemy_vulnerable,
    most_enemy_weak,
    least_awkward_shivs,
    lowest_health_monster,
    lowest_total_monster_health,
    lowest_barricaded_block,
    most_draw_pay_early,
    most_draw_pay,
    most_good_player_powers,
    least_bad_player_powers,
    most_less_good_player_powers,
    least_enemy_artifacts,
    most_bad_cards_exhausted,
    least_incoming_damage,
    most_ethereal_cards_saved_for_later,
    most_energy,
]

powers_we_like: List[PowerId] = [
    PowerId.ACCURACY,
    PowerId.AFTER_IMAGE,
    PowerId.ARTIFACT,
    PowerId.BERSERK,
    PowerId.BUFFER,
    PowerId.DEMON_FORM,
    PowerId.ELECTRO,
    PowerId.ENVENOM,
    PowerId.EVOLVE,
    PowerId.FIRE_BREATHING,
    PowerId.FOCUS,
    PowerId.HEATSINK,
    PowerId.INFINITE_BLADES,
    PowerId.INTANGIBLE_PLAYER,
    PowerId.JUGGERNAUT,
    PowerId.LOOP,
    PowerId.MACHINE_LEARNING,
    PowerId.MAYHEM,
    PowerId.METALLICIZE,
    PowerId.NOXIOUS_FUMES,
    PowerId.PANACHE,
    PowerId.PHANTASMAL,
    PowerId.PLATED_ARMOR,
    PowerId.REPAIR,
    PowerId.SADISTIC,
    PowerId.THORNS,
    PowerId.THOUSAND_CUTS,
    PowerId.TOOLS_OF_THE_TRADE,
]


def add_to_comparison_list(comparisons: List[Comparison], comparison_to_add: Comparison, after: Comparison):
    index = comparisons.index(after) + 1
    comparisons.insert(index, comparison_to_add)


def move_in_comparison_list(comparisons: List[Comparison], comparison_to_move: Comparison, after: Comparison):
    comparisons.remove(comparison_to_move)
    add_to_comparison_list(comparisons, comparison_to_move, after)


powers_we_like_less: List[PowerId] = [
    PowerId.DEXTERITY,
    PowerId.STRENGTH,
    PowerId.ENERGIZED,
]

powers_we_dislike: List[PowerId] = [
    PowerId.FRAIL,
    PowerId.VULNERABLE,
    PowerId.WEAKENED,
    PowerId.BIAS,
]


class CommonGeneralComparator(ComparatorInterface):

    def __init__(self, comparisons: List[Comparison] = None, assessment_config: ComparatorAssessmentConfig = None):
        self.comparisons: List[Comparison] = default_comparisons if comparisons is None else comparisons
        self.assessment_config: ComparatorAssessmentConfig = \
            ComparatorAssessmentConfig(powers_we_like, powers_we_like_less, powers_we_dislike) \
                if assessment_config is None else assessment_config

    def does_challenger_defeat_the_best(self, best_state: BattleState, challenger_state: BattleState,
                                        original: BattleState) -> bool:
        best = CA(best_state, original, self.assessment_config)
        challenger = CA(challenger_state, original, self.assessment_config)

        for c in self.comparisons:
            v = c(best, challenger)
            if v is not None:
                del best
                del challenger
                return v
        del best
        del challenger
        return False
