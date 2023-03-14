from rs.calculator.cards import CardId

SynergyBeneficiaries = {
    CardId.ANGER: [],
    CardId.APOTHEOSIS: [SynergyTag.EXHAUST],
    CardId.APPARITION: [SynergyTag.EXHAUST, SynergyTag.EXHAUST],
    CardId.BANDAGE_UP: [SynergyTag.EXHAUST],
    CardId.BASH: [SynergyTag.STRENGTH],
    CardId.BATTLE_TRANCE: [],
    CardId.BLOODLETTING: [],
    CardId.BLOOD_FOR_BLOOD: [],
    CardId.BLUDGEON: [],
    CardId.BODY_SLAM: [],
    CardId.BURN: [SynergyTag.STATUS],
    CardId.CARNAGE: [],
    CardId.CLASH: [],
    CardId.CLEAVE: [SynergyTag.STRENGTH],
    CardId.CLOTHESLINE: [],
    CardId.DARK_SHACKLES: [SynergyTag.EXHAUST, SynergyTag.EXHAUST],
    CardId.DAZED: [SynergyTag.EXHAUST, SynergyTag.EXHAUST,
                   SynergyTag.STATUS],
    CardId.DISARM: [SynergyTag.EXHAUST, SynergyTag.EXHAUST],
    CardId.DROPKICK: [SynergyTag.STRENGTH],
    CardId.DEFEND_R: [SynergyTag.DEXTERITY],
    CardId.DEFEND_G: [SynergyTag.DEXTERITY],
    CardId.ENTRENCH: [],
    CardId.FEED: [SynergyTag.STRENGTH, SynergyTag.EXHAUST],
    CardId.FIEND_FIRE: [SynergyTag.STRENGTH, SynergyTag.STRENGTH, SynergyTag.STRENGTH,
                        SynergyTag.EXHAUST, SynergyTag.EXHAUST, SynergyTag.EXHAUST],
    CardId.FLAME_BARRIER: [SynergyTag.DEXTERITY],
    CardId.FLASH_OF_STEEL: [SynergyTag.STRENGTH],
    CardId.FLEX: [],
    CardId.GHOSTLY_ARMOR: [SynergyTag.EXHAUST],
    CardId.HAND_OF_GREED: [SynergyTag.STRENGTH],
    CardId.HEAVY_BLADE: [SynergyTag.STRENGTH, SynergyTag.STRENGTH, SynergyTag.STRENGTH],
    CardId.HEMOKINESIS: [SynergyTag.STRENGTH],
    CardId.IMMOLATE: [SynergyTag.STRENGTH,
                      SynergyTag.STATUS, SynergyTag.STATUS],
    CardId.IMPERVIOUS: [SynergyTag.EXHAUST, SynergyTag.EXHAUST],
    CardId.INFLAME: [],
    CardId.INTIMIDATE: [],
    CardId.IRON_WAVE: [],
    CardId.JAX: [],
    CardId.LIMIT_BREAK: [SynergyTag.STRENGTH, SynergyTag.STRENGTH, SynergyTag.STRENGTH, SynergyTag.STRENGTH],
    CardId.MASTER_OF_STRATEGY: [],
    CardId.METALLICIZE: [],
    CardId.NEUTRALIZE: [SynergyTag.STRENGTH],
    CardId.OFFERING: [SynergyTag.EXHAUST, SynergyTag.EXHAUST],
    CardId.PAIN: [],
    CardId.PERFECTED_STRIKE: [],
    CardId.POMMEL_STRIKE: [SynergyTag.STRENGTH],
    CardId.POWER_THROUGH: [SynergyTag.DEXTERITY,
                           SynergyTag.STATUS, SynergyTag.STATUS, SynergyTag.STATUS],
    CardId.PUMMEL: [SynergyTag.STRENGTH, SynergyTag.STRENGTH, SynergyTag.STRENGTH, SynergyTag.STRENGTH,
                    SynergyTag.EXHAUST],
    CardId.RAGE: [],
    CardId.RAMPAGE: [SynergyTag.STRENGTH],
    CardId.REAPER: [SynergyTag.STRENGTH, SynergyTag.STRENGTH, SynergyTag.STRENGTH, SynergyTag.EXHAUST],
    CardId.REGRET: [],
    CardId.RECKLESS_CHARGE: [SynergyTag.STATUS, SynergyTag.STATUS],
    CardId.SEEING_RED: [SynergyTag.EXHAUST],
    CardId.SHOCKWAVE: [SynergyTag.EXHAUST, SynergyTag.EXHAUST],
    CardId.SHRUG_IT_OFF: [SynergyTag.DEXTERITY],
    CardId.SLIMED: [SynergyTag.EXHAUST,
                    SynergyTag.STATUS, SynergyTag.STATUS],
    CardId.SPOT_WEAKNESS: [SynergyTag.STRENGTH],
    CardId.STRIKE_R: [SynergyTag.STRENGTH],
    CardId.SWIFT_STRIKE: [SynergyTag.STRENGTH],
    CardId.THUNDERCLAP: [SynergyTag.STRENGTH, SynergyTag.STRENGTH],
    CardId.TRIP: [],
    CardId.TWIN_STRIKE: [SynergyTag.STRENGTH],
    CardId.UPPERCUT: [SynergyTag.STRENGTH],
    CardId.WILD_STRIKE: [SynergyTag.STATUS],
    CardId.WOUND: [SynergyTag.STATUS, SynergyTag.STATUS, SynergyTag.STATUS, SynergyTag.STATUS],
    CardId.FEEL_NO_PAIN: [],
    CardId.DARK_EMBRACE: [],
    CardId.BLADE_DANCE: [SynergyTag.SHIVS, SynergyTag.SHIVS, SynergyTag.SHIVS],
    CardId.EVOLVE: [SynergyTag.STATUS],
    CardId.FIRE_BREATHING: [SynergyTag.STATUS, SynergyTag.STATUS],
    CardId.BURNING_PACT: [SynergyTag.STATUS, SynergyTag.EXHAUST, SynergyTag.EXHAUST, SynergyTag.EXHAUST]
}


def synergyBeneficiariesCardIdStrings():
    return [v.value for v in SynergyBeneficiaries.keys()]