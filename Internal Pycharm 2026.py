#Start 10/3/2026
#Xavier Gardner Internal
#-----------------------

#Library Imports:
#----------------
import time
import random


#Constants:
#----------

#possible locations player can travel depending on what is unlocked
SCHOOL_MAP = {
    "1":"Science Class",
    "2":"School Gym",
    "3":"Math Class",
    "4":"AGC"

}

#all the possible riddles that the player can be asked for the science location
riddles = [
    {"question": "I can be cracked, made, told, and played. What am I?",
     "answer": "joke"},
    {"question": "What has many keys but can not open any doors. What am I?",
     "answer": "piano"},
    {"question": "What has hands but can not clap?",
     "answer": "clock"}]

#all the possible moves for dodging for the gym function
actions = ["jump", "crouch", "dash left", "dash right"]

#all fragments required for the holy gate key
required_fragments = {"rusty_key_fragment", "weighted_key_fragment", "paper_key_fragment"}

#Variables:
#----------
name = ""
discovered_locations = {"1","2","3"}
inventory = []
searched_locations = []

player_time = 5 #expel time = 12
player_cortisol = 0


#Functions:
#---------

#Set up section of code
#-----------------------------
#function for printed text individually types a letter at a time. Speed will be set to 0.02 when finished
def slow_text(text: str, speed = 0.00004):
    for letter in text:
        print(letter, end = '', flush = True)
        time.sleep(speed)

#resets values to starting values
def reset_game():
    global inventory, player_cortisol, player_time, discovered_locations, searched_locations
    inventory = []
    player_cortisol = 0
    player_time = 5
    discovered_locations = {"1","2","3"}
    searched_locations = []

#checks if player has all key fragments, if so then location 4 unlocks
def key_fragment_check():
    if all (item in inventory for item in required_fragments):
        discovered_locations.add("4")

#easy way to print out lots of space
def space():
    print()
    print()
    print()


#shows the current available options the player can travel to
def show_map():
    key_fragment_check()
    while True:
        global name
        slow_text("====School Map====")
        print()
        print()

        for key, location in SCHOOL_MAP.items():
            if key in discovered_locations:
                print(f"{key}: {location}")
        space()

        map_teleport = input(f"{name}, where do you want to travel: ")

        if map_teleport not in discovered_locations:
            print()
            slow_text("That is not a discovered location")
            print()
            continue

        if map_teleport == "1":
            discovered_locations.remove("1")
            science_class()
            break

        elif map_teleport == "2":
            discovered_locations.remove("2")
            school_gym()
            break

        elif map_teleport == "3":
            discovered_locations.remove("3")
            math_class()
            break

        elif map_teleport == "4":
            discovered_locations.remove("4")
            AGC()
            break

        else:
            slow_text("You have to enter 1, 2 or 3.")
            print()

#shows the current status with cool dialogue
def class_laptop():
    global name
    space()
    slow_text("-----------------------")
    print()
    slow_text("-----------------------")
    print()
    slow_text("-----------------------")
    print()
    slow_text("-----------------------")
    print()
    slow_text("-----------------------")
    print()
    slow_text(f"Welcome {name}.")
    print()
    slow_text("After successfully logging into the laptop,")
    print()
    slow_text("you go into the Wellington College student portal to find your status...")
    print()
    status()
    space()

#gets all the options that player can visit
def get_available_options(all_options, searched_locations):
    return [option for option in all_options if option not in searched_locations]

#function for player to check there status
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

            slow_text("3. Current inventory (Enter 3) ")
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
                slow_text(f"Your inventory is {inventory}.")
                space()
                loop_control = False

            else:
                slow_text("Enter an integer, ever 1, 2 or 3.")
                print()

        except ValueError:
            slow_text("Enter an integer, ever 1, 2 or 3.")
            print()

#check if they have reached 100 cortisol and lost the game, if below 100 they are told there current cortisol level
def cortisol_check():
    global name

    print()
    if player_cortisol >= 100:
        slow_text(f"{name}, Your cortisol levels exceeded the limit and you pass out.")
        print()
        slow_text("You wake up in Mr Denham's office...")
        print()
        slow_text("I am not angry, I am just disappointed, you are expelled!!!")
        exit()
    else:
        print()
        slow_text(f"You now have a cortisol level of {player_cortisol}, be careful, do not get to a level of 100 cortisol...")
        space()

#shows the current time for player or ends game if player's time reaches 12
def time_check():
    print()
    if player_time >= 12:
        slow_text("Tick, tock")
        print()
        time.sleep(3)
        slow_text("tick tock.")
        print()
        time.sleep(1)
        slow_text(f"{name}, it is too late to escape...")
        print()
        time.sleep(3)
        slow_text("Mr Denham storms out of his office and expels you!!!")
        exit()
    else:
        print()
        slow_text(f"The current time is {player_time}PM, spend your time wisely as midnight is near...")
        space()


#Start/introduction functions

#fetches name
def name_start():
    global name

    slow_text("====WELLINGTON COLLEGE ESCAPE=====")
    space()

    slow_text("Before you play the best game of your life I need to know 1 thing from you...")
    print()
    name = input("what is your name: ")
    print()
    slow_text(f"Very well then {name}.")
    print()
    print()

#gives player 3 options, ever starting straight away, getting an introduction then starting or just quit
def start_menu():
    loop_control = True

    while loop_control:
        try:
            slow_text("1. Start (Enter 1)")
            space()

            slow_text("2. Introduction (Enter 2)")
            space()

            slow_text("3. Quit (Enter 3) ")
            space()

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

#breifs the player on the objective and situation player is in
def introduction():
    global name
    slow_text("First of all you will need to understand the situation you are placed in...")
    print()
    slow_text("The current time is 5:30PM.")
    print()
    slow_text("You slept through last period and the teacher left you behind...")
    print()
    slow_text("The gates are closed, you are trapped inside the school...")
    print()
    slow_text("Be careful as every move costs you time and can increase your cortisol...")
    print()
    slow_text("Solve riddles and avoid danger, collect all 3 key fragments (Rusty key fragment, Heavy weighted key fragment, Paper key fragment) to forge the holy gate key,")
    print()
    slow_text("so you can unlock the school gate before it clocks midnight...")
    print()
    print(f"Good luck {name}.")
    space()


#levels
#------
#tower block
#-----------
def tower_block_search():
    global searched_locations
    all_options = [1,2,3]

    slow_text("You wake up in first floor of tower block.")
    print()
    slow_text("you are inside a tech classroom, quickly search the class for a school map before you are found...")
    space()

    while True:
        available_options = get_available_options(all_options, searched_locations)

        if not available_options:
            #if all locations searched exit loop
            break

        options_text = ",".join(str(option) for option in available_options)
        slow_text(f"Available options: {options_text}:")
        space()

        if 1 not in searched_locations:
            slow_text("1. Search the rubbish bin (Enter 1)")
            space()

        if 2 not in searched_locations:
            slow_text("2. Search the teacher's drawers (Enter 2)")
            space()
        if 3 not in searched_locations:
            slow_text("3. Search the electronics storage system (Enter 3) ")
            space()
        try:
            find_map = int(input("Enter your choice on where you want to search for the school map: "))
        except ValueError:
            slow_text(f"Enter an integer from {available_options}")
            space()
            continue

        if find_map not in available_options:
            slow_text(f"Enter an integer from {available_options}")
            space()
            continue

        searched_locations.append(find_map)
        space()

        if find_map ==1:
            space()
            find_map_choice_1()


        elif find_map == 2:
            space()
            find_map_choice_2()


        elif find_map == 3:
            space()
            find_map_choice_3()


#sub-functions for towerblock with all 3 options where they can search for the map
#----------------------------
def find_map_choice_1():
    global player_cortisol, name

    slow_text("You walk over to the rubbish bin...")
    print()
    slow_text("but once you arrive there is a strange, rotten smell coming from it...")
    print()
    print()
    loop_control = True
    while loop_control:
        try:
            search_bin = int(input("Enter (1) if you still want to search bin, or enter (2) if you want to search somewhere else: "))
        except ValueError:
            slow_text(f"Invalid choice, enter an integer.")
            continue
        if search_bin == 1:
            print()
            print()
            slow_text("You start removing trash from the rubbish bin...")
            print()
            slow_text("Out of no where a rat jumps out of the bin and tries to attack you!!!")
            print()
            slow_text("You dodge just in time but your cortisol spikes!!!")
            print()
            print()
            player_cortisol +=20
            cortisol_check()
            space()

            slow_text("You go back to the bin, but find no map.")
            print()
            slow_text("It is your lucky day though as you found a lab note.")
            inventory.append("lab_note")
            print()
            slow_text("Your luck does not run out when searching as you discover a protein shake for the gym.")
            space()
            inventory.append("protein_shake")
            space()
            loop_control = False
            space()
            tower_block_search()


        elif search_bin == 2:
            print()
            print()
            slow_text(f"Smart decision {name}.")
            loop_control = False
            space()
            tower_block_search()

        else:
            print()
            print()
            slow_text("You have to enter 1 or 2")
            loop_control = True
            #fix this
def find_map_choice_2():
    slow_text("You walk over to the teacher's draws...")
    print()
    slow_text("The draws for some reason is unlocked so you pull it out.")
    print()
    slow_text("After searching for a good few seconds a piece of paper catches your attention...")
    print()
    slow_text("You unravel the paper to find that it is in fact the school map!!!")
    print()
    show_map()

def find_map_choice_3():
    global player_time, name
    slow_text("You walk over to the electronics storage system...")
    print()
    slow_text("It is overflowing with random electronic parts...")
    print()
    loop_control = True
    while loop_control:
        try:
            search_electronics = int(input("Enter (1) if you still want to search the electronics storage system, or enter (2) if you want to search somewhere else: "))

        except ValueError:
            slow_text(f"Invalid choice, enter 1 or 2.")
            continue

        if search_electronics == 1:
            print()
            print()
            slow_text("You start moving electronics around in hope for the school map...")
            print()
            print()
            slow_text("You instead find a calculator.")
            inventory.append("calculator")
            space()

            slow_text("You keep searching for the map, with a little hope left...")
            print()
            slow_text("Your hope is destroyed after searching the whole storage system.")
            print()
            slow_text("You leave the area in hopes to find the map somewhere else feeling pitiful.")
            print()
            print()
            player_time +=1
            time_check()
            loop_control = False
            space()
            tower_block_search()

        elif search_electronics == 2:
            print()
            print()
            slow_text(f"You will see if that move pays off {name}...")
            loop_control = False
            space()
            tower_block_search()

        else:
            print()
            print()
            slow_text("You have to enter 1 or 2")
            loop_control = True

#Locations:

#Science class
def science_class():
    global player_cortisol, player_time, name

    space()
    slow_text("With the help of your map, you navigate your way through the school into the science block.")
    print()
    slow_text("You walk through the corridor, the atmosphere is eerie...")
    print()
    slow_text("Out of no where a teacher starts yelling at you!!!")
    slow_text(f"{name}, what are you still doing here?!?!")
    print()
    player_cortisol += 20
    cortisol_check()
    space()

    slow_text("You dash into the nearest class and luckily escape danger.")
    print()
    slow_text("You murmur to yourself,")
    print()
    slow_text("'Hold on a minute I need a rusty key fragment, I could maybe find it in this science lab...' ")
    print()
    slow_text("You see a chest in the corner of the room so you make your way over..")
    space()
    slow_text("'What brings you here?', the chest asks.")
    print()
    slow_text("'W-w-well I am looking for a rusty key fragment.'")
    print()
    slow_text("The chest replies 'Very well then, I have access to this key, but I am bored so you have to solve a riddle...'.")
    print()
    slow_text("'Every mistake costs you time...'")
    space()

    #lab note is a hint for jokes found in the towerblock
    if "lab_note" in inventory:
        print()
        slow_text("You unravel the note from your pocket, the reading follows: ")
        space()
        slow_text("The objective is simple solve 1 of the riddles to receive the key...")
        print()
        slow_text("The chest was taught only knows 3 jokes so it will keep repeating them until you answer 1 of them correctly.")
        print()
        slow_text("Question: I can be cracked, made, told, and played.First letter will be j.")
        print()
        slow_text("Question:What has many keys but can not open any doors. First letter will be p.")
        print()
        slow_text("Question: What has hands but can not clap? First letter will be c.")
        space()

    random.shuffle(riddles)

    #loop until the player gets 1 right
    correct = False
    while not correct:
        riddle = random.choice(riddles)
        print("Riddle: ", riddle["question"])
        print()
        player_answer = input("Enter your answer: ").lower()

        if player_answer == riddle["answer"]:
            print("Correct!!!")
            print()
            print(f"Very well then {name}, here is the rusty key fragment.")
            inventory.append("rusty_key_fragment")
            print(inventory)
            key_fragment_check()
            space()
            correct = True
        else:
            print("Wrong answer!!!")
            print()
            print("Time is ticking!!!")
            player_time +=1
            time_check()

    space()
    slow_text("You walk over to a laptop...")
    print()
    class_laptop()
    space()
    show_map()


#School gym
def school_gym():
    global player_cortisol
    dodge_streak = 0

    space()
    slow_text("Using your school map, you walk over to the school gym to hopefully find a key fragment...")
    print()
    slow_text("As you attempt to enter the gym a powerlifter interrupts you suddenly at the door way.")
    print()
    slow_text("He demands 'Hey, how much do you bench?!?'")
    print()
    slow_text("You reply 'No clue.'")
    print()
    slow_text("He yells 'Get out of here then!!!'")
    print()
    slow_text("You think to yourself 'a key fragment must be in here, I must get past him'.")
    space()

    #makes challenge easier, item can be found in the towerblock
    if "protein_shake" in inventory:
        slow_text("You chug the protein shake from earlier to improve your physical ability.")
        reaction_time = 7
        required_dodge_streak = 2
    else:
        reaction_time = 5
        required_dodge_streak = 3
    print()
    slow_text(f"You have to dodge {required_dodge_streak} attacks from the powerlifter to get past.")
    print()

    while dodge_streak < required_dodge_streak:
        action = random.choice(actions)
        slow_text(f"Quick! Enter '{action}' within {reaction_time} to dodge!!!")

        start_time = time.time()
        player_input = input(">>>").lower()
        end_time = time.time()

        if player_input == action and end_time - start_time <= reaction_time:
            dodge_streak += 1
            slow_text(f"Good job, you dodged in time! ({dodge_streak}/{required_dodge_streak})")
            print()
        else:
            slow_text("The power lifter successfully attacks!!!")
            print()
            player_cortisol +=10
            cortisol_check()
            dodge_streak = 0
    slow_text("The powerlifter clearly did not do enough cardio, so you slip right past him.")
    print()
    slow_text("You enter the gym and the weighted key fragment is right there on the dumbbell rack.")
    print()
    inventory.append("weighted_key_fragment")
    print(inventory)
    key_fragment_check()
    space()
    show_map()




#Math class
def math_class():
    global player_cortisol,name

    space()
    slow_text("With the help of your trusty map, you walk over to the math department...")
    print()
    slow_text("The head of the math department walks out of his class and spots you lurking")
    print()
    slow_text(f"{name}, look I have had a long day, if you get these math questions right you will not have a detention.")
    space()

    slow_text("You walk into the class and see other kids sitting around as they all have a detention")
    print()
    slow_text("You sit down whilst the kids stare at you...")
    print()
    slow_text("'Here is your work sheet, it is simple get 3 in a row right and you can walk out of here.'")
    print()
    slow_text("'You will keep repeating worksheets until you complete the objective.'")
    print()
    #calc
    correct_math_streak = 0
    while correct_math_streak < 3:
        #create math question and answer for it
        number_1 = random.randint(1, 12)
        number_2 = random.randint(1, 12)
        correct_math_answer = number_1 * number_2

        try:
            player_answer = int(input(f"What is the answer for {number_1} x {number_2}: "))

        except ValueError:
            slow_text("You did not enter a number!!!")
            continue

        if player_answer == correct_math_answer:
            print()
            correct_math_streak += 1
            slow_text(f"Correct!!! ({correct_math_streak}/3 in a row.)")
            space()
        else:
            slow_text("Incorrect!!! your streak plummets down to 0!!!")
            correct_math_streak = 0
            player_cortisol += 10
            cortisol_check()

    space()
    slow_text("Very well then,")
    print()
    slow_text("'here is the paper key that you will need for leaving.'")

    inventory.append("paper_key_fragment")
    print(inventory)
    key_fragment_check()
    space()
    show_map()



#final location
def AGC():
    global name
    space()
    slow_text("With all the the key fragments found you make your way over to your final destination.")
    space()
    slow_text("You enter the AGC, you walk on to the stage where you find the holy key forge...")
    print()
    slow_text("You place all three key fragments ontop of the key forge...")
    print()
    slow_text("Your ears start ringing and your vision goes blurry...")
    space()
    slow_text("You wake up after passing out with a throbbing a headache...")
    print()
    slow_text("The key forge had done its magic, the holy gate key floats in the air...")
    space()
    slow_text("After arriving at the school gate you slot the holy gate key into it.")
    print()
    slow_text(f"You step foot outside of the school, you are now free {name}")
    space()



#Main Loop:
#----------
def main_loop():
    name_start()
    start_menu()
    tower_block_search()

#running game
while True:
    print("===GAME OVER===")
    space()
    reset_game()
    main_loop()
    restart = input("Do you want to restart? (enter y or n): ").lower()
    if restart != "y":
        break

