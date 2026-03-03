
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