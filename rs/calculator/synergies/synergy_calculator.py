from typing import List

from rs.calculator.cards import CardId
from rs.calculator.synergies.synergy_beneficiaries import SynergyBeneficiaries
from rs.calculator.synergies.synergy_providers import SynergyProviders
from rs.calculator.synergies.synergy_tags import SynergyTag


def getSynergy(cardId: CardId, deck: List[CardId]):

    deck_length = len(deck)
    if cardId in SynergyProviders:
        tags = SynergyProviders[cardId]

        # Count the number of times each tag appears in the beneficiaries
        final_count = {}
        for tag in tags:
            final_count[tag] = 0
            element_count = 0
            for element in deck:
                #print(element)
                if element in SynergyBeneficiaries:
                    for synergy in SynergyBeneficiaries.get(element):
                        #print(synergy)
                        if synergy == tag:
                            element_count += 1
                final_count[tag] = element_count
                #print(final_count)

        # Sum up the tag counts and return the result
        return sum(final_count.values()) / deck_length


def get_beneficiary_scores(cardId: CardId, deck: List[CardId]):
    if cardId in SynergyBeneficiaries:
        tags = SynergyBeneficiaries[cardId]

        # Count the number of times each tag appears in the beneficiaries
        final_count = {}
        for tag in tags:
            final_count[tag] = 0
            element_count = 0
            for element in deck:
                # print(element)
                if element in SynergyProviders:
                    for synergy in SynergyProviders.get(element):
                        if synergy == tag:
                            element_count += 1

                final_count[tag] = element_count
                # print(final_count)

        # Sum up the tag counts and return the result
        return sum(final_count.values())


def get_provider_scores(cardId: CardId, deck: List[CardId]):
    if cardId in SynergyProviders:
        tags = SynergyProviders[cardId]

        # Count the number of times each tag appears in the beneficiaries
        final_count = {}
        for tag in tags:
            final_count[tag] = 0
            element_count = 0
            for element in deck:
                # print(element)
                if element in SynergyBeneficiaries:
                    for synergy in SynergyBeneficiaries.get(element):
                        # print(synergy)
                        if synergy == tag:
                            element_count += 1
                final_count[tag] = element_count
                # print(final_count)

        # Sum up the tag counts and return the result
        return sum(final_count.values())

