#Start 10/3/2026
#Xavier Gardner Internal
#-----------------------

#Library Imports:
#----------------
import time
import random

#loop for while loops ect
loop = True

#Constants:
#----------
EXPEL_TIME = 12
KEY_ESCAPE_GATE = 1
tower_block_level_1_pass = 1
tower_block_level_6_gate_key = 1

#Variables:
#----------
player_time = 5.5
player_cortisol = 0
player_key = 0 # later on if player_key = 1 then KEY_ESCAPE_GATE = True
name = ""
level_1_pass_desicion = ""

#Functions:
#----------
def start_menu():
    loop_control = True

    while loop_control:
        try:
            slow_text("====WELLINGTON COLLEGE ESCAPE=====")
            print()
            print()
            print()
            time.sleep(1)

            slow_text("1. Start (Enter 1)")
            print()
            print()

            slow_text("2. Introduction (Enter 2)")
            print()
            print()

            slow_text("3. Quit (Enter 3) ")
            print()
            print()

            start_menu_choice = int(input("Enter your choice: "))

            if start_menu_choice == 1:
                loop_control = False

            elif start_menu_choice == 2:
                introduction()
                loop_control = False

            elif start_menu_choice == 3:
                exit()
            else:
                slow_text("You have to enter 1, 2 or 3")
                print()

        except ValueError:
            slow_text("Enter an integer, ever 1, 2 or 3")
            print()



def introduction():
    slow_text("Before you play the best game of your life I need to know 1 thing from you...")
    print()
    #time.sleep(1)
    name = input("what is your name: ")
    print()
    #time.sleep(1)
    slow_text(f"Very well then {name}.")
    print()
    time.sleep(2)
    slow_text("First of all you will need to understand the situation you are placed in...")
    print()
    time.sleep(1)
    slow_text("The current time is 5:30PM.")
    print()
    slow_text("You slept through last period and the teacher left you behind...")
    print()
    slow_text("The gates are closed, you are trapped inside the school...")
    print()
    slow_text("Be careful as every move costs you time and can increase your cortisol...")
    print()
    slow_text("Make your way to the very top of the tower block where the almighty key is stored so you can unlock the school gate before it clocks midnight...")
    print()
    time.sleep(1)
    slow_text(f"Good luck {name}.")
    print()
    print()
    print()
    time.sleep(3)

def cortisol_check():
    print()
    if player_cortisol >= 100:
        slow_text(f"{name}, Your cortisol levels exceeded the limit and you pass out.")
        print()
        time.sleep(2)
        slow_text("You wake up in Mr Denham's office...")
        print()
        slow_text("I am not angry, I am just dissapointed, you are expelled!!!")
        exit()
    else:
        print()
        slow_text(f"You have a cortisol level of {player_cortisol}, be careful, do not get to a level of 100 cortisol...")
        print()


#levels
def tower_block():
    slow_text("You wake up in first floor of tower block.")
    print()
    slow_text("You must find a elevator pass to the second floor,")

def tower_block_level_1():
    print()
    time.sleep(1)
    slow_text("you are inside a tech classroom, quickly search the class for a pass before you are found...")

#function for printed text individually types a letter at a time. Speed will be set to 0.02 when finished
def slow_text(text: str, speed = 10000.02):
    for letter in text:
        print(letter, end = '')
        time.sleep(0.001/speed)

#Main Loop:
#----------
start_menu()
introduction()
tower_block()

