import random
from time import sleep


# Check that users have entered a valid
# option based on a list
def integer_checker(question):
    """checks that the integer is more than 13"""


    while True:
        error = "Please enter an integer more than 1."
        #check for infinite mode
        to_check = input(question)

        if to_check == "":
            return "infinite"
        #round detector thingy
        try:

            response = int(to_check)

            #checks that the number is more than 1
            if response < 1:
                print(error)

            else:
                return response
        except ValueError:
            print(error)

def make_statement(statement, decoration):
    """adds emoji/decoration to headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")

    return ""

def string_checker(question, valid_ans=('yes', 'no')):
    error = f"please enter a valid option from the following list: {valid_ans}"
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            #check if the user response is a word in the list
            if item == user_response:
                return item

            #check if user response is the same as
            #the first letter of an item in the list
            elif user_response == item[0]:
                return item
        #print error if user does not enter something that is valid
        print(error)
        print()

def instructions():
    """prints instructions"""

    print("""
*** Instructions ***

pick either infinite mode or choose the number of rounds.

play against the computer (100% not rigged) you need to pick
rock (r), paper (p) or scissors (s)

you know how paper scissors rock works, right?
if you dont then FIGURE IT OUT!

(press <xxx> to exit the game at any time)
    """)

def rps_compare(user,bot):

    if user == bot:
        result = "tie"

    elif user == "rock" and bot == "scissors":
        result = "win"
    elif user == "paper" and bot == "rock":
        result = "win"
    elif user == "scissors" and bot == "paper":
        result = "win"

    else:
        result = "lose"



    return result

#main routine

#int game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0
yes_no_list = ["yes","no"]
rps_list = ["rock","paper","scissors","xxx"]
game_history = []

make_statement(f"ROCK, PAPER, SCISSORS"," _/¯\_")
print()

#instructions
#ask user if they want the instructions
want_instructions = string_checker("do you want the instructions: ")
print()

#display instructions if the user wants to see
if want_instructions == "yes":
    instructions()

#ask user for number of rounds / infinite mode
num_rounds = integer_checker("how many rounds do you want to play (press <enter> for infinite): ")
print()

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#game loop starts here
while rounds_played < num_rounds:

    #round headings (based on mode)

    if mode == "infinite":
        rounds_heading = make_statement(f"Round {rounds_played + 1} (infinite mode)","-")
    else:
        rounds_heading = make_statement(f"Round {rounds_played + 1} of {num_rounds}","-")

    bot_choice = random.choice(rps_list[:-1])

    #get user choice
    user_choice = string_checker("choose: ", rps_list)
    print()


    #exit code
    if user_choice == "xxx":
        break

    #print out user choice and bot choice
    print("you chose", user_choice)
    sleep(0.5)
    print()
    print(f"bot chose {bot_choice}")
    sleep(0.6)
    print()

    #randomly choose from the rps list (excluding the exit code)


    #compare user and bot choice
    result = rps_compare(user_choice, bot_choice)

    #adjust game lost / game tied counters and add results to game history
    if result == "lose":
        rounds_lost += 1
        feedback = "you lost"
    elif result == "tie":
        rounds_tied += 1
        feedback = "its a tie"
    else:
        feedback = "you won"

    round_feedback = f"{user_choice} vs {bot_choice}, {feedback}"
    history_item = f"round: {rounds_played + 1} - {round_feedback}"

    #print result
    sleep(0.2)
    print("ROCK")
    sleep(0.4)
    print("PAPER")
    sleep(0.4)
    print("SCISSORS")
    sleep(0.4)
    print()
    print(round_feedback)
    print()
    game_history.append(history_item)
    #makes the rounds progress
    rounds_played += 1

    #if users are in infinite mode increase number of rounds
    if mode == "infinite":
        num_rounds += 1

#game loop ends here

#fix crash
if rounds_played > 0:

    #game history / stats
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played *100
    percent_tied = 100 - percent_won - percent_lost


    #output game stats
    make_statement("game statistics", "[]")
    print(f"percent won:\t {percent_won:.2f}%\n"
          f"percent lost:\t {percent_lost:.2f}%\n"
          f"percent tied:\t {percent_tied:.2f}%\n")

    #ask if the user wants to see game history
    want_history = string_checker("do you want to see the game history? ",yes_no_list)
    print()
    if want_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("thanks for playing")

else:
    print("you chicken")
