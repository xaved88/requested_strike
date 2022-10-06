import json
import unittest
from typing import List

from definitions import ROOT_DIR
from rs.machine.handlers.handler import Handler
from rs.machine.state import GameState


class BaseTestHandlerFixture(unittest.TestCase):
    ai_handlers: List[Handler]  # should be overriden by AI package fixture
    handler: Handler  # should be overridden by children - the expected handler to respond to this state.

    def execute_handler_tests(self, state_path: str, expected: List[str]):
        f = open(f"{ROOT_DIR}/tests/res/{state_path}", "r")
        state = f.read()
        f.close()
        state = GameState(json.loads(state))

        actual = None
        for h in self.ai_handlers:
            if h.can_handle(state):
                if type(h) is self.handler:
                    actual = h.handle(state)
                    break
                else:
                    self.fail(f"Expected handler {self.handler}, instead got {type(h)}")

        if actual is None:
            self.fail("No handler found that could handle")

        self.assertEqual(expected, actual)
