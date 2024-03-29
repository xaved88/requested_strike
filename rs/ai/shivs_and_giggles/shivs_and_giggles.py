from typing import List

from rs.ai.shivs_and_giggles.config import CARD_REMOVAL_PRIORITY_LIST, HIGH_PRIORITY_UPGRADES
from rs.ai.shivs_and_giggles.handlers.boss_relic_handler import BossRelicHandler
from rs.ai.shivs_and_giggles.handlers.card_reward_handler import CardRewardHandler
from rs.ai.shivs_and_giggles.handlers.combat_reward_handler import CombatRewardHandler
from rs.ai.shivs_and_giggles.handlers.event_handler import EventHandler
from rs.ai.shivs_and_giggles.handlers.potions_handler import PotionsBossHandler, PotionsEventFightHandler, \
    PotionsEliteHandler
from rs.ai.shivs_and_giggles.handlers.shop_purchase_handler import ShopPurchaseHandler
from rs.ai.shivs_and_giggles.handlers.upgrade_handler import UpgradeHandler
from rs.common.handlers.common_astrolabe_handler import CommonAstrolabeHandler
from rs.common.handlers.common_battle_handler import CommonBattleHandler
from rs.common.handlers.common_campfire_handler import CommonCampfireHandler
from rs.common.handlers.common_chest_handler import CommonChestHandler
from rs.common.handlers.common_discard_handler import CommonDiscardHandler
from rs.common.handlers.common_map_handler import CommonMapHandler
from rs.common.handlers.common_neow_handler import CommonNeowHandler
from rs.common.handlers.common_purge_handler import CommonPurgeHandler
from rs.common.handlers.common_shop_entrance_handler import CommonShopEntranceHandler
from rs.common.handlers.common_transform_handler import CommonTransformHandler
from rs.machine.ai_strategy import AiStrategy
from rs.machine.character import Character
from rs.machine.handlers.handler import Handler

shivs_and_giggles_battle_potion_handlers: List[Handler] = [
    # Potions Handlers First
    PotionsBossHandler(),
    PotionsEventFightHandler(),
    PotionsEliteHandler(),
]

SHIVS_AND_GIGGLES: AiStrategy = AiStrategy(
    character=Character.SILENT,
    handlers=shivs_and_giggles_battle_potion_handlers + [
        # Some edge cases
        CommonAstrolabeHandler(CARD_REMOVAL_PRIORITY_LIST),

        # Battle Handler
        CommonBattleHandler(),

        # General Stuff
        BossRelicHandler(),
        UpgradeHandler(),
        CommonTransformHandler(CARD_REMOVAL_PRIORITY_LIST),
        CommonPurgeHandler(CARD_REMOVAL_PRIORITY_LIST),
        CombatRewardHandler(),
        CardRewardHandler(),
        CommonNeowHandler(),
        EventHandler(),
        CommonChestHandler(),
        CommonMapHandler(),
        CommonCampfireHandler(HIGH_PRIORITY_UPGRADES),
        CommonShopEntranceHandler(),
        ShopPurchaseHandler(),
        CommonDiscardHandler(),
    ]
)
