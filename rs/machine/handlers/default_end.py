from rs.machine.command import Command
from rs.machine.handlers.handler import Handler
from rs.machine.handlers.handler_action import HandlerAction
from rs.machine.state import GameState


class DefaultEndHandler(Handler):

    def can_handle(self, state: GameState) -> bool:
        return state.has_command(Command.END)

    def handle(self, state: GameState) -> HandlerAction:
        return HandlerAction(commands=["end"])
