from typing import List

from rs.machine.command import Command
from rs.machine.handlers.handler import Handler
from rs.machine.state import GameState


class DefaultConfirmHandler(Handler):

    def can_handle(self, state: GameState) -> bool:
        return state.has_command(Command.CONFIRM) or state.has_command(Command.PROCEED)

    def handle(self, state: GameState) -> List[str]:
        return ["proceed"]
