# entry point for the program


def main():
    name = prompt("Insert your name : ")
    print(name)


def prompt(question: str):
    answer = input(question)
    return answer


if __name__ == "__main__":
    main()
