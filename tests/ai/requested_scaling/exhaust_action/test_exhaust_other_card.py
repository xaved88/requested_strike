from ai.requested_scaling.exhaust_action.exhaust_test_fixture import ExhaustHandlerFixture
from rs.ai.requested_scaling.handlers.synergy_handlers.exhaust_action.exhaust_handler import ExhaustHandler


class ExhaustHandlerTest(ExhaustHandlerFixture):
    handler = ExhaustHandler

    def test_exhaust_others(self):
        self.execute_handler_tests('battles/synergy_statessynergy_states/learn_to_choose_cards.json', [])