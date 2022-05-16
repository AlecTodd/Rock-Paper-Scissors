import random

player_count = 0
bot_count = 0

def lost():
    print("Bot won the round!")
    global bot_count
    bot_count+=1

def win():
    print("Player has won the round!")
    global player_count
    player_count+=1

def tie():
    print("Tie! No one wins!")

def score():
    global bot_count
    global player_count
    print("Player has " + str(player_count) + " wins so far")
    print("Bot has " + str(bot_count) + " wins so far")




options = ["rock", "paper", "scissors"]



game = input("Would you like to play?\n")
if game == ["no", "No"]:
    exit()
else:
    while player_count < 6 or bot_count < 6:
        choice = input("Choose rock, paper, scissors\n")
        # if choice != "rock" or "paper" or "scissors":
        #     exit()
        bot = random.choice(options)
        print("Bot has thrown " + bot)

        if choice == "rock":
            if bot == "paper":
                lost()
            if bot == "scissors":
                win()
            if bot == "rock":
                tie()

        if choice == "paper":
            if bot == "scissors":
                lost()
            if bot == "rock":
                win()
            if bot == "paper":
                tie()

        if choice == "scissors":
            if bot == "rocks":
                lost()
            if bot == "paper":
                win()
            if bot == "scissors":
                tie()

        score()
        if player_count == 5:
            print("Congratulations! You have won the game!")
            exit()
        if bot_count == 5:
            print("Sorry! You lost!")
            exit()
        continue




