from termcolor import colored


def print_success(text):
    print(colored(text, 'green', 'on_black'), end='')


def print_warning(text):
    print(colored(text, 'yellow', 'on_black'), end='')


def print_error(text):
    print(colored(text, 'red', 'on_black'), end='')


def print_grey(text):
    print(colored(text, 'light_grey', 'on_black'), end='')
