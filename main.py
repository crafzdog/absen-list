# a main() function acts as entry point executed when the script is starts
def main():
    name = prompt("Insert your name : ")
    print(name)


# a function that help us to ask a question to the end user
def prompt(question: str) -> str:
    answer = input(question)
    return answer


# ensures that the main() function is executed only when the script is run directly
if __name__ == "__main__":
    main()
