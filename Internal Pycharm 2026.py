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
KEY_ESCAPE_GATE = 1
tower_block_level_1_pass = 1
tower_block_level_6_gate_key = 1

#Variables:
#----------
inventory = []
searched_locations = []
available_options = []
all_options = []

player_time = 5 #expel time = 12
player_cortisol = 0
player_key = 0 # later on if player_key = 1 then KEY_ESCAPE_GATE = True
name = ""
display_updated_status = ""

#Decision variables
find_map = ""
start_menu_choice = ""
search_bin = ""

#Functions:
#---------

# Start/set up section of code
#-----------------------------
def space():
    print()
    print()
    print()
    print()
def sleep_1_and_space():
    print()
    print()
    time.sleep(1)

def sleep_3_and_space():
    print()
    print()
    time.sleep(3)

def get_available_options(all_options, searched_locations):
    global available_options
    return [option for option in all_options if option not in searched_locations]


def name_start():
    slow_text("====WELLINGTON COLLEGE ESCAPE=====")
    print()
    print()
    #time.sleep(1)

    slow_text("Before you play the best game of your life I need to know 1 thing from you...")
    print()
    #time.sleep(1)
    name = input("what is your name: ")
    #time.sleep(1)
    print()
    #time.sleep(1)
    slow_text(f"Very well then {name}.")
    #time.sleep(3)
    print()
    print()
def start_menu():
    loop_control = True

    while loop_control:
        try:
            slow_text("1. Start (Enter 1)")
            print()
            print()

            slow_text("2. Introduction (Enter 2)")
            print()
            print()

            slow_text("3. Quit (Enter 3) ")
            print()
            print()
            #time.sleep(1)

            start_menu_choice = int(input("Enter your choice: "))

            if start_menu_choice == 1:
                loop_control = False

            elif start_menu_choice == 2:
                introduction()
                start_menu()
                loop_control = False

            elif start_menu_choice == 3:
                exit()
            else:
                slow_text("You have to enter 1, 2 or 3")
                print()

        except ValueError:
            slow_text("Enter an integer, ever 1, 2 or 3")
            print()

def status():
    loop_control = True
    while loop_control:
        try:
            slow_text("1. Cortisol level (Enter 1)")
            print()
            print()

            slow_text("2. Current time (Enter 2)")
            print()
            print()

            slow_text("3. Map (Enter 3) ")
            print()
            print()
            #time.sleep(1)
            slow_text("3. Current inventory (Enter 4) ")
            print()
            print()

            display_updated_status = int(input("Enter your choice: "))

            if display_updated_status == 1:
                cortisol_check()
                print()
                print()
                loop_control = False

            elif display_updated_status == 2:
                slow_text(f"The current time is {player_time}PM.")
                print()
                print()
                loop_control = False

            elif display_updated_status == 3:
                exit()

            elif display_updated_status == 4:
                exit()
            else:
                slow_text("You have to enter 1, 2, 3 or 4")
                print()

        except ValueError:
            slow_text("Enter an integer, ever 1, 2, 3 or 4")
            print()




def introduction():
    #time.sleep(2)
    slow_text("First of all you will need to understand the situation you are placed in...")
    print()
    #time.sleep(1)
    slow_text("The current time is 5:30PM.")
    print()
    slow_text("You slept through last period and the teacher left you behind...")
    print()
    slow_text("The gates are closed, you are trapped inside the school...")
    print()
    slow_text("Be careful as every move costs you time and can increase your cortisol...")
    print()
    slow_text("Solve riddles and avoid danger to find the almighty key so you can unlock the school gate before it clocks midnight...")
    print()
    #time.sleep(1)
    print(f"Good luck {name}.")
    print()
    print()
    print()
    #time.sleep(3)

def cortisol_check():
    print()
    if player_cortisol >= 100:
        slow_text(f"{name}, Your cortisol levels exceeded the limit and you pass out.")
        print()
        #time.sleep(2)
        slow_text("You wake up in Mr Denham's office...")
        print()
        slow_text("I am not angry, I am just dissapointed, you are expelled!!!")
        exit()
    else:
        print()
        slow_text(f"You now have a cortisol level of {player_cortisol}, be careful, do not get to a level of 100 cortisol...")
        print()

def map():
    print("")


#levels
#------
#tower block
#-----------
def tower_block():
    slow_text("You wake up in first floor of tower block.")
    print()
    slow_text("you are inside a tech classroom, quickly search the class for a school map before you are found...")
    print()
    print()
    tower_block_search()
def tower_block_search():
    loop_control = True
    all_options = [1,2,3]
    while loop_control:
        try:
            available_options = get_available_options(all_options, searched_locations)
            options_text = ",".join(str(option) for option in available_options)

            if 1 not in searched_locations:
                slow_text("1. Search the rubbish bin (Enter 1)")
                print()
                print()

            if 2 not in searched_locations:
                slow_text("2. Search the teacher's draws (Enter 2)")
                print()
                print()

            if 3 not in searched_locations:
                slow_text("3. Search the electronics storage system (Enter 3) ")
                print()
                print()

            find_map = int(input("Enter your choice on where you want to go: "))

            if find_map == 1 and 1 not in searched_locations:
                searched_locations.append(1)
                print()
                print()
                find_map_choice_1()
                loop_control = False

            elif find_map == 2 and 2 not in searched_locations:
                searched_locations.append(2)
                print()
                print()
                find_map_choice_2()
                loop_control = False

            elif find_map == 3 and 3 not in searched_locations:
                searched_locations.append(3)
                print()
                print()
                find_map_choice_3()
                loop_control = False
            elif len(searched_locations) == 3:
                loop_control = False

            else:
                slow_text(f"You have to enter {available_options}")
                print()
        except ValueError:
            slow_text(f"Enter an integer, ever {available_options}")
            print()

#sub-functions for towerblock
#----------------------------

def find_map_choice_1():
    print()
    slow_text("You walk over to the rubbish bin...")
    print()
    slow_text("but once you arrive there is a strange, rotten smell coming from it...")
    print()
    print()
    loop_control = True
    while loop_control == True:
        search_bin = int(input("Enter (1) if you still want to search bin, or enter (2) if you want to search somewhere else: "))
        if search_bin == 1:
            print()
            print()
            slow_text("You start removing trash from the rubbish bin...")
            print()
            slow_text("Out of no where a rat jumps out of the bin and trys to attack you!!!")
            print()
            slow_text("You dodge just in time but your cortisol spikes!!!")
            print()
            print()
            global player_cortisol
            player_cortisol =+20
            cortisol_check()
            space()
            slow_text("You go back to the bin, but find no map.")
            print()
            slow_text("It is your lucky day though as you found a lab note.")
            inventory.append("lab note")
            space()
            loop_control = False
            tower_block_search()


        elif search_bin == 2:
            print()
            print()
            slow_text(f"Smart decision {name}.")
            loop_control = False
            #make player chose again


        else:
            print()
            print()
            slow_text("You have to enter 1 or 2")
            loop_control = True




def find_map_choice_2():
    print()

def find_map_choice_3():
    print()

#function for printed text individually types a letter at a time. Speed will be set to 0.02 when finished
def slow_text(text: str, speed = 0.00003):
    for letter in text:
        print(letter, end = '')
        time.sleep(speed)

#Main Loop:
#----------
map()
name_start()
start_menu()
tower_block()
status()

