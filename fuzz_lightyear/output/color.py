from enum import Enum

from fuzz_lightyear.settings import get_settings


class AnsiColor(Enum):
    RESET = '[0m'
    BOLD = '[1m'
    RED = '[91m'
    RED_BACKGROUND = '[41m'
    YELLOW = '[33m'
    LIGHT_GREEN = '[92m'
    PURPLE = '[95m'


def colorize(text: str, color: AnsiColor) -> str:
    return (
        f'\x1b{color.value}{text}\x1b{AnsiColor.RESET.value}'
        if get_settings().enable_color
        else text
    )
