import os
from time import sleep
from colorama import Fore


def fprint(*message: str or list, erase: bool = False, sep: str = '', end: str = '\r') -> None:
    """Substitutes the normal printing for the error of line misarrangement (text-screen transformations).
    ** Use this instead of normal print. **
    (You cand always make 'print = fprint' to use default, although losing some capabilities of print)

    Args:
        message (string or list): text to be displayed.
        erase (bool, optional): flag if the text should be erased next print. Defaults to False.
        set (str, optional): separator of args (like normal print).
        end (string): like normal end on print for end of the line char. default: '\\r'
    """

    size = os.get_terminal_size().columns
    str_jump = ' ' * size

    print(str_jump, end=end)

    if erase:
        print(*message, sep=sep, end=end)
    else:
        print(*message, sep=sep)


def lprint(percentage: float, text: str = 'Loading: ', show: bool = False, colors: bool = False, sep: list = ['[', ']'], char_load: str = '#', char_unload: str = '.') -> None:
    """Prints a loading bar at the end of the cmd line screen.
    ** Let this be the last print on you execution flow. **

    Args:
        percentage (float): percentage of completion [0.0 - 1.0]
        text (string, optional): string to be presentend; default: 'Loading: '
        show (bool, optional): flag to show the percentage
        colors (bool, optional): flag to predetermined color output
        sep (list, optional): separators of loading bar. Defaults to ['[', ']'].
        char_load (str, optional): loaded char. Defaults to '#'.
        char_unload (str, optional): unloaded char. Defaults to '.'.
    """

    size = os.get_terminal_size().columns
    str_jump = ' ' * size

    string_percentage = str(round(percentage*100)) + '%' if show else ''
    size_load = size - len(text) - len(sep) - \
        len(string_percentage) - 2

    if colors:

        if percentage < 1:
            color_percentage = Fore.YELLOW
        else:
            color_percentage = Fore.GREEN

    if colors:
        loadbar = color_percentage + text + sep[0] + (char_load * int(size_load * percentage)) + \
            (char_unload * int(size_load * (1-percentage))) + \
            sep[1] + Fore.RESET

        loadbar += ' ' + color_percentage + string_percentage + Fore.RESET if show else ''
    else:
        loadbar = text + sep[0] + (char_load * int(size_load * percentage)) + \
            (char_unload * int(size_load * (1-percentage))) + \
            sep[1] + Fore.RESET

        loadbar += ' ' + string_percentage if show else ''

    try:
        print(loadbar, end='\r')
        sleep(.1)  # to see it more slowly
    except KeyboardInterrupt:
        fprint('Exit by keyboard canceling!')
        exit(-1)


for x in range(0, 101):
    if x % 5 == 0:

        fprint('{} is a 5 divider!'.format(x))

    div_five = 'True' if x % 5 == 0 else 'False'

    string_loading = ''

    string_loading += 'Loading: '

    lprint(x/100, string_loading, True, True, ['[', ']'], '#', '.')


print()

# print a lone line at end for the '\r' in the code,
# so that new line doesn't get eaten

# try to resolve the '\r' problem with the carrier always at the start of line
# without the '\r' -> print line + spaces -> print load bar (causes blink effect)
