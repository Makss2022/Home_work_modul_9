from contacts import contacts
from typing import Dict, List, Callable


def input_error(func: Callable):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except TypeError:
            return "Сommand entered incorrectly!"
        except ValueError:
            return "Give me name and phone please!"
        except KeyError:
            return "Contact  does not exist in the contact book!"
    return inner


@input_error
def hello_hendler(*args: str) -> str:
    return "How can I help you?"


@input_error
def exit_hendler(*args: str) -> str:
    return "Good bye!"


@input_error
def add_handler(name_phone: list[str]) -> str:
    name, phone = name_phone
    if name in contacts.keys():
        return f"The contact '{name}' already exists in the contact-book!"
    contacts[name] = phone
    return "New contact saved!"


@input_error
def phone_hendler(name_list: list[str]) -> str:
    name = name_list[0]
    return f"Phone {name} is {contacts[name]}"


@input_error
def change_hendler(name_phone: list[str]) -> str:
    name, new_phone = name_phone
    contacts[name] = new_phone
    return f"{name}'s phone has been replaced with a new phone {new_phone}"


@input_error
def show_all_handler(*args: str) -> str:
    header = "Contacts book:\n"
    contacts_format = "\n".join(f"{name} number is {phone}" for name,
                                phone in contacts.items())
    contacts_format = "Phone numbers do not exist yet!" if contacts == {} else contacts_format
    return header + contacts_format


handlers: dict[str, Callable] = {
    "hello": hello_hendler,
    "good bye": exit_hendler,
    "close": exit_hendler,
    "exit": exit_hendler,
    "add": add_handler,
    "change": change_hendler,
    "phone": phone_hendler,
    "show all": show_all_handler,
}
