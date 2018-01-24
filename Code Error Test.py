import time
import os
def enterName():
    print("Welcome to KDGaming DarkRP server #1. Please read the rules.\n\t1)No Random Death Match\n\t2)Do not break NLR\n\t3)Do not FailRP\n\t4)Use common sense.")
    RPname = input(str("Please enter an RP name: "))
    agreeornot = input("Do you agree to these rules? y/n".lower)
    yeslist = ["y","yes","yeah","yep"]
    nolist = ["n","no","nah","nope"]
    if agreeornot in yeslist:
        print("{0}(OOC): I have read and agree to follow the rules.".format(RPname))
    elif agreeornot in nolist:
        print("{0}(OOC): I do not agree with the rules. So I must leave.".format(RPName))
        time.sleep(3)
        os.cls()
        enterName()
    else:
        print("Incorrect answer. Try again.")
    os.cls()
    enterName()

def menu():
    inventory = []
    answer=''
    print("RP Menu\n\tPress O to open inventory\n\tPress A to add an item to inventory\n\tPress E to use an item from the inventory\n\tPress Q to quit game.")
    while answer != q:
        answer = input("Please enter choice: >>>").lower()
    if answer == 'o':
        print(inventory)
    elif answer == 'e':
        item = input("Which item do you want to use?")


def main():
    enterName()

main()
