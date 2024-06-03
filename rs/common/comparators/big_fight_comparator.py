from rs.common.comparators.common_general_comparator import default_comparisons, add_to_comparison_list, \
    move_in_comparison_list, CommonGeneralComparator
from rs.common.comparators.core.comparisons import *

comparisons = default_comparisons.copy()
move_in_comparison_list(comparisons, comparison_to_move=most_good_player_powers, after=PLACEHOLDER_IMPORTANT)
move_in_comparison_list(comparisons, comparison_to_move=least_enemy_artifacts, after=most_enemy_vulnerable)
move_in_comparison_list(comparisons, comparison_to_move=most_powered_up_ritual_dagger, after=PLACEHOLDER_OPTIMIZATIONS)
move_in_comparison_list(comparisons, comparison_to_move=killed_with_lesson_learned, after=PLACEHOLDER_OPTIMIZATIONS)
add_to_comparison_list(comparisons, comparison_to_add=avoid_inconvenient_time_warp, after=PLACEHOLDER_IMPORTANT)

if most_tranquility in comparisons:
    add_to_comparison_list(comparisons, comparison_to_add=most_crescendo, after=most_tranquility)


class BigFightComparator(CommonGeneralComparator):
    def __init__(self):
        super().__init__(comparisons)
