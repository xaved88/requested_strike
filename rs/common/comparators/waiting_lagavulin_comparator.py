from rs.common.comparators.common_general_comparator import default_comparisons, add_to_comparison_list, \
    move_in_comparison_list, CommonGeneralComparator
from rs.common.comparators.core.comparisons import *

comparisons = default_comparisons.copy()
comparisons.remove(lowest_health_monster)
comparisons.remove(lowest_total_monster_health)
move_in_comparison_list(comparisons, comparison_to_move=most_good_player_powers, after=PLACEHOLDER_EXTREMELY_IMPORTANT)
add_to_comparison_list(comparisons, comparison_to_add=highest_health_monster, after=PLACEHOLDER_EXTREMELY_IMPORTANT)


# Differences to normal comparator:
# Do not cause damage, instead play powers and debuffs.
class WaitingLagavulinComparator(CommonGeneralComparator):
    def __init__(self):
        super().__init__(comparisons)
