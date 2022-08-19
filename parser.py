from typing import Callable, List
from handlers import input_error


@input_error
def hello_show_exit_parser(list_input_user: list[str]) -> str:
    return ["", ""]


@input_error
def add_change_parser(list_input_user: list[str]) -> str:
    if list_input_user[1] == "" or ''.join(list_input_user[2:]) == "" or list_input_user[1].isdigit():
        return [""]
    return [list_input_user[1], ''.join(list_input_user[2:])]


@input_error
def phone_parser(list_input_user: list[str]) -> str:
    return [list_input_user[1], ""]


@input_error
def unknown_command(list_input_user: list[str]) -> str:
    return [""]


parser_handler: dict[str, Callable] = {
    "hello": hello_show_exit_parser,
    "good bye": hello_show_exit_parser,
    "close": hello_show_exit_parser,
    "exit": hello_show_exit_parser,
    "add": add_change_parser,
    "change": add_change_parser,
    "phone": phone_parser,
    "show all": hello_show_exit_parser
}


def parser_user_input(imput_user: str) -> tuple[str, list]:
    input_user_split = imput_user.split()
    command = input_user_split[0].lower()
    input_user_split.extend([""])

    if input_user_split[0].lower() == "show" and input_user_split[1].lower() == "all" or input_user_split[0].lower() == "good" and input_user_split[1].lower() == "bye":
        command = " ".join(input_user_split[0:2]).lower()

    arguments = parser_handler.get(
        command, unknown_command)(input_user_split)

    return command, arguments
