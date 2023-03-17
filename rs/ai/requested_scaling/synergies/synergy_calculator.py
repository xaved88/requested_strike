from typing import List

from rs.calculator.cards import CardId
from rs.ai.requested_scaling.synergies.synergy_beneficiaries import SynergyBeneficiaries
from rs.ai.requested_scaling.synergies.synergy_providers import SynergyProviders


def get_synergy(card_id: CardId, deck: List[CardId]) -> float:
    deck_length = len(deck)
    if card_id not in SynergyProviders:
        return 0
    else:
        tags = SynergyProviders[card_id]
        tag_counts = {tag: 0 for tag in tags}  # Initialize all tag counts to 0

        # Count the number of times each tag appears in the deck
        for element in deck:
            if element in SynergyBeneficiaries:
                for synergy in SynergyBeneficiaries[element]:
                    if synergy in tags:
                        tag_counts[synergy] += 1

        # Calculate the total tag count and return the result
        total_tag_count = sum(tag_counts.values())
        if deck_length > 0:
            return round(total_tag_count / deck_length, 1)
        else:
            return 0


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

