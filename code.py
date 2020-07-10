import time
import random

random = random.choice(["Cyclops", " Hydra", " Fire Dragoon", "Vampire",
                        "pirate"])


def print_message(message):
    print(message)
    time.sleep(2)


def restart():
    replaying = input("Would you like to play again? (y/n)").lower()
    if "y" in replaying:
        print_message("Excellent! Restarting the game ...")
        play()
    elif "n" in replaying:
        print_message("Thanks for playing! See you next time")
        exit()


def house():
    print_message("You approach the door of the house.")
    print_message("You are about to knock when the door opens "
                  "and out steps " + random + ".")
    print_message("Eep! This is the " + random + "'s house!")
    print_message("" + random + " attacks you!")


def lose():
    print_message("You feel a bit under-prepared for this, "
                  "what with only having a tiny dagger.")
    fight_or_run = input("Would you like to (1) fight or (2) run away?")
    if fight_or_run == "1":
        print_message("You do your best...")
        print_message("but your dagger is no match for " + random + ".")
        print_message("You have been defeated!")
        restart()
    elif fight_or_run == "2":
        print_message("You run back into the field. Luckily, you don't"
                      " seem to have been followed.")
        main()


def cave():
    print_message("You peer cautiously into the cave.")
    print_message("It turns out to be only a very small cave.")
    print_message("Your eye catches a glint of metal behind a rock.")
    print_message("You have found the magical Sword of Ogoroth!")
    print_message("You discard your silly old dagger and take "
                  "the sword with you.")
    print_message("You walk back out to the field.")


def field():
    print_message("Enter 1 to knock on the door of the house.")
    print_message("Enter 2 to peer into the cave.")
    print_message("What would you like to do?")


def win():
    fight_or_run2 = input("Would you like to (1) fight or (2) run away?")
    if fight_or_run2 == "1":
        print_message("As the " + random + " moves to attack, "
                      "you unsheath your new sword.")
        print_message("The Sword of Ogoroth shines brightly in your "
                      "hand as you brace yourself for the attack.")
        print_message("But " + random + " takes one look at"
                      "your shiny new toy and runs away!")
        print_message("You have rid the town of " + random + ". "
                      "You are victorious!")
        restart()
    elif fight_or_run2 == "2":
        print_message("You run back into the field. Luckily, you don't"
                      " seem to have been followed.")
        main()


def been_there():
    print_message("You peer cautiously into the cave.")
    print_message("You've been here before, and gotten all the"
                  " good stuff. It's just an empty cave now.")
    print_message("You walk back out to the field.")
    field()


def play():
    print_message("You find yourself standing in an open field,"
                  "filled with grass and yellow wildflowers.")
    print_message("Rumor has it that a " + random + " is somewhere around "
                  "here, and has been terrifying the nearby village.")
    print_message("In front of you is a house.")
    print_message("To your right is a dark cave.")
    print_message("In your hand you hold your trusty (but not very effective) "
                  "dagger.")
    main()


def main():
    field()
    while True:
        choice = input("(Please enter 1 or 2.)\n")
        if choice == "1":
            house()
            lose()

            break
        elif choice == "2":
            cave()
            field()
            while True:
                choice = input("(Please enter 1 or 2.)\n")
                if choice == "1":
                    house()
                    win()
                elif choice == "2":
                    been_there()
                    while True:
                        choice2 = input("(Please enter 1 or 2.)\n")
                        if choice2 == "1":
                            house()
                            win()
                        elif choice2 == "2":
                            been_there()
            break


play()
