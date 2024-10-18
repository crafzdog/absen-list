from enum import Enum


# menu enum for submission
class Menu(Enum):
    Register = ("1", "register")
    Login = ("2", "login")
    EXIT = ("0", "exit")
