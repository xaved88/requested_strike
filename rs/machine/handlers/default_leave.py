from rs.machine.command import Command
from rs.machine.handlers.handler import Handler
from rs.machine.handlers.handler_action import HandlerAction
from rs.machine.state import GameState


class DefaultLeaveHandler(Handler):

    def can_handle(self, state: GameState) -> bool:
        return state.has_command(Command.LEAVE)

    def handle(self, state: GameState) -> HandlerAction:
        return HandlerAction(commands=["return"])
