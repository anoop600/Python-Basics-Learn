import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def colour_print(text: str, *effects: tuple) -> None:
    """Print `text` using the ANSI sequences to change colour etc

    Args:
        text (`str`): [string to print]
        effects (tuple): [color constant value]
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)

colorama.init()
colour_print("This will be in red", RED)
colour_print("This will be in red with bold", RED, BOLD)
colour_print("This will be in green", GREEN)
colour_print("This will be in blue", BLUE)
colour_print("This will be in blue in reversed", BLUE, REVERSE)
colour_print("This will be in blue in reversed and underlined", BLUE, REVERSE, UNDERLINE)
colorama.deinit()