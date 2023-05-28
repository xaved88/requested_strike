import math

from rs.calculator.cards import get_card
from rs.calculator.enums.card_id import CardId
from rs.calculator.interfaces.card_effects_interface import CardEffectsInterface
from rs.calculator.interfaces.battle_state_interface import BattleStateInterface
from rs.calculator.interfaces.card_interface import CardInterface
from rs.calculator.enums.power_id import PowerId
from rs.game.card import CardType


def dropkick_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    if target_index > -1:
        if state.monsters[target_index].powers.get(PowerId.VULNERABLE):
            state.player.energy += 1
            state.draw_cards(1)


def entrench_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.player.block *= 2


def feed_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    __feed_post_hook(state, target_index, 3)


def feed_upgraded_post_hook(state: BattleStateInterface, target_index: int = -1):
    __feed_post_hook(state, target_index, 4)


def __feed_post_hook(state: BattleStateInterface, target_index: int, amount: int):
    if state.monsters[target_index].current_hp <= 0:
        state.player.max_hp += amount
        state.player.current_hp += amount


def fiend_fire_pre_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    effect.hits = len(state.hand) - 1


def fiend_fire_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    while state.hand:
        state.exhaust_pile.append(state.hand.pop())


def immolate_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.discard_pile.append(get_card(CardId.BURN))


def limit_break_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    if state.player.powers.get(PowerId.STRENGTH):
        state.player.powers[PowerId.STRENGTH] *= 2


def wild_strike_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.draw_pile.append(get_card(CardId.WOUND))


def reckless_charge_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.draw_pile.append(get_card(CardId.DAZED))


def power_through_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.add_cards_to_hand(get_card(CardId.WOUND), 2)


def spot_weakness_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    __spot_weakness_post_hook(state, target_index, 3)


def spot_weakness_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    __spot_weakness_post_hook(state, target_index, 4)


def __spot_weakness_post_hook(state: BattleStateInterface, target_index: int, amount: int):
    if state.monsters[target_index].hits:
        state.player.add_powers({PowerId.STRENGTH: amount}, state.player.relics, state.player.powers)


def reaper_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    if hasattr(effect, 'hp_damage'):
        state.player.heal(effect.hp_damage)


def apotheosis_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    for i in range(len(state.draw_pile)):
        c = state.draw_pile[i]
        state.draw_pile[i] = get_card(c.id, upgrade=c.upgrade + 1)


def heel_hook_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    if target_index > -1:
        if state.monsters[target_index].powers.get(PowerId.WEAKENED):
            state.player.energy += 1
            state.draw_cards(1)


def storm_of_steel_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    amount = len(state.hand)
    for _ in range(amount):
        state.discard_card(state.hand[0])
    state.add_cards_to_hand(get_card(CardId.SHIV), amount)


def storm_of_steel_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                      target_index: int = -1):
    amount = len(state.hand)
    for _ in range(amount):
        state.discard_card(state.hand[0])
    state.add_cards_to_hand(get_card(CardId.SHIV, upgrade=1), amount)


def eviscerate_post_others_discarded_hook(card: CardInterface):
    card.cost = max(0, card.cost - 1)


def sneaky_strike_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    if state.cards_discarded_this_turn:
        state.player.energy += 2


def unload_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    for idx in reversed(range(len(state.hand))):
        if state.hand[idx].type != CardType.ATTACK:
            state.discard_card(state.hand[idx])


def tactician_post_self_discarded_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                       target_index: int = -1):
    state.player.energy += 1


def tactician_upgraded_post_self_discarded_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                                target_index: int = -1):
    state.player.energy += 2


def reflex_post_self_discarded_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.draw_cards(2)


def reflex_upgraded_post_self_discarded_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                             target_index: int = -1):
    state.draw_cards(3)


def bane_pre_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    if target_index > -1:
        if state.monsters[target_index].powers.get(PowerId.POISON):
            effect.hits = 2


def bullet_time_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    for card in state.hand:
        if card.cost != -1:
            card.cost = 0


def catalyst_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    if target_index > -1:
        if state.monsters[target_index].powers.get(PowerId.POISON):
            base_poison = state.monsters[target_index].powers.get(PowerId.POISON)
            state.monsters[target_index].add_powers({PowerId.POISON: base_poison}, state.player.relics,
                                                    state.player.powers)


def catalyst_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    if target_index > -1:
        if state.monsters[target_index].powers.get(PowerId.POISON):
            base_poison = state.monsters[target_index].powers.get(PowerId.POISON)
            state.monsters[target_index].add_powers({PowerId.POISON: base_poison * 2}, state.player.relics,
                                                    state.player.powers)


def sword_boomerang_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    __sword_boomerang_post_hook(state, 3)


def sword_boomerang_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                       target_index: int = -1):
    __sword_boomerang_post_hook(state, 4)


def __sword_boomerang_post_hook(state: BattleStateInterface, hits: int):
    state.inflict_random_target_damage(3, hits, True, 1.5, True, 1)


def bouncing_flask_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    __bouncing_flask_post_hook(state, 3)


def bouncing_flask_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                      target_index: int = -1):
    __bouncing_flask_post_hook(state, 4)


def __bouncing_flask_post_hook(state: BattleStateInterface, hits: int):
    state.add_random_poison(3, hits)


def deep_breath_pre_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.draw_pile.extend(state.discard_pile)
    state.discard_pile.clear()


def enlightenment_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    for card in state.hand:
        if card.cost >= 2:
            card.cost = 1


def impatience_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    attacks_in_hand = len([True for c in state.hand if c.type == CardType.ATTACK])
    if attacks_in_hand == 0:
        state.draw_cards(2)


def impatience_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    attacks_in_hand = len([True for c in state.hand if c.type == CardType.ATTACK])
    if attacks_in_hand == 0:
        state.draw_cards(3)


def rip_and_tear_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    __rip_and_tear_post_hook(state, 7)


def rip_and_tear_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                       target_index: int = -1):
    __rip_and_tear_post_hook(state, 9)


def __rip_and_tear_post_hook(state: BattleStateInterface, damage: int):
    state.inflict_random_target_damage(damage, 2, True, 1.5, True, 1)


def stack_pre_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    block = len(state.discard_pile)
    state.player.block += block


def stack_upgraded_pre_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    block = len(state.discard_pile) + 3
    state.player.block += block


def mind_blast_pre_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    effect.damage = len(state.draw_pile)
    effect.hits = 1


def auto_shields_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    __auto_shields_post_hook(state, 11)


def auto_shields_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                       target_index: int = -1):
    __auto_shields_post_hook(state, 15)


def __auto_shields_post_hook(state: BattleStateInterface, block: int):
    if state.player.block == 0:
        state.player.block = block


def turbo_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.discard_pile.append(get_card(CardId.VOID))


def aggregate_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    __aggregate_post_hook(state, 4)


def aggregate_upgraded_post_hook(state: BattleStateInterface, effect: CardEffectsInterface,
                                       target_index: int = -1):
    __aggregate_post_hook(state, 3)


def __aggregate_post_hook(state: BattleStateInterface, divide_by_this: int):
    energy_gain = math.floor(len(state.draw_pile) / divide_by_this)
    state.player.energy += energy_gain


def double_energy_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.player.energy *= 2


def overclock_post_hook(state: BattleStateInterface, effect: CardEffectsInterface, target_index: int = -1):
    state.discard_pile.append(get_card(CardId.BURN))
