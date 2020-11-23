from time import sleep

commandhelp = ["help: display this message", "login: log in to hasaki!", "register: create an account at hasaki!",
               "exit: exit slice 'n' dice"]
commands = ["help", "login", "register", "exit"]

def programinitialization():
    print("slice 'n' dice alpha - for hasaki!")
    print("from nooney with passion\n")
    sleep(3)


def printcommands():
    print("Commands available:", *commandhelp, sep='\n- ')


def console():
    print("Redirecting to console...")
    sleep(1)
    print("Successfully redirected to console!")
    print("Type 'help' to list possible commands!")
    while True:
        print("Console: ")
        command = input()
        if command in commands:
            if command == "help":
                printcommands()
            if command == "login":
                print("WIP")
            if command == "register":
                print("WIP")
            if command == "exit":
                exit()
        else:
            print("Unknown command. \n"), sleep(1)
