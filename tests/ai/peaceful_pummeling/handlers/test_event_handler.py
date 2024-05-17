from ai.peaceful_pummeling.pp_test_handler_fixture import PpTestHandlerFixture
from rs.ai.peaceful_pummeling.handlers.event_handler import EventHandler


class TestEventHandler(PpTestHandlerFixture):
    handler = EventHandler

    def test_council_of_ghosts(self):
        self.execute_handler_tests('/event/council_of_ghosts.json', ['choose accept', 'wait 30'])

    def test_council_of_ghosts_skip_because_we_have_bites(self):
        self.execute_handler_tests('/event/council_of_ghosts_with_bite.json', ['choose refuse', 'wait 30'])

    def test_vampires(self):
        self.execute_handler_tests('/event/vampires.json', ['choose accept', 'wait 30'])

    def test_vampires_with_apparition(self):
        self.execute_handler_tests('/event/vampires_with_apparition.json', ['choose refuse', 'wait 30'])

    def test_vampires_with_few_strikes(self):
        self.execute_handler_tests('/event/vampires_with_few_strikes.json', ['choose refuse', 'wait 30'])

    def test_vampires_with_many_strikes(self):
        self.execute_handler_tests('/event/vampires_with_many_strikes.json', ['choose accept', 'wait 30'])