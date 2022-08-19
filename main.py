from parser import parser_user_input
from handlers import handlers


def main():
    while True:
        try:
            user_input = input("Command: ")
            command, arguments = parser_user_input(user_input)
            command_handler = handlers.get(command)
            command_response = command_handler(arguments)
            print(command_response)
            if command_response == "Good bye!":
                break
        except TypeError:
            print("Сommand entered incorrectly!")


if __name__ == "__main__":
    main()
