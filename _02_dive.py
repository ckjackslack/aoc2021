import pyparsing as pp
from dataclasses import dataclass
from typing import Tuple, List
from aoc_helpers import fcommands

class DebugMixin:
    def _debug(self, *args):
        if hasattr(self, 'debug') and self.debug:
            d = {
                k[0]: v
                for k, v
                in self.__dict__.items()
                if k != 'debug'
            }
            print(f"[DEBUG: {repr(args[0]):>16} {d!r}]")

@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0
    debug: bool = False
    def update_position(self, cmd: Tuple[str, int]) -> None:
        match cmd[0]:
            case 'forward':
                self.horizontal += cmd[1]
            case 'up':
                self.depth -= cmd[1]
            case 'down':
                self.depth += cmd[1]
    def get_result(self):
        return self.horizontal * self.depth

@dataclass
class ExtraPosition(Position, DebugMixin):
    aim: int = 0
    def update_position(self, cmd: Tuple[str, int]) -> None:
        match cmd[0]:
            case 'forward':
                self.horizontal += cmd[1]
                self.depth += self.aim * cmd[1]
            case 'up':
                self.aim -= cmd[1]
            case 'down':
                self.aim += cmd[1]
        self._debug(cmd)

command = pp.oneOf('forward down up') + pp.Word(pp.nums)
def command_parse(string, location, tokens):
    tokens[1] = int(tokens[1])
command.setParseAction(command_parse)

def calculate_final_position(pos: Position,
    commands: List[str]) -> Position:
    for cmd in commands:
        parsed_cmd = tuple(command.parseString(cmd))
        pos.update_position(parsed_cmd)
    return pos

def main():
    pos = Position()
    print(pos)
    pos = calculate_final_position(pos, fcommands())
    print(pos)
    print(pos.get_result())

if __name__ == '__main__':
    main()