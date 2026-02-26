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
#main routine

#int game variables
mode = "regular"
rounds_played = 0

make_statement("ROCK, PAPER, SCISSORS"," _/¯\_")
print()

#instructions

#ask user for number of rounds / infinite mode
num_rounds = integer_checker("how many rounds do you want to play (press <enter> for infinite): ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#game loop starts here
while rounds_played < num_rounds:
    user_choice = input("choose: ").lower()

    #exit code
    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds played: ",rounds_played)

    #if users are in infinite mode increase number of rounds
    if mode == "infinite":
        num_rounds += 1

#game loop ends here

#game history / stats