# Coursera Assignment for:
# An Introduction to Interactive Programming in Python (Part 1)
# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name.upper() == "ROCK":
        return 0
    elif name.upper() == "SPOCK":
        return 1
    elif name.upper() == "PAPER":
        return 2
    elif name.upper() == "LIZARD":
        return 3
    elif name.upper() == "SCISSORS":
        return 4
    else:
        print "The input: %s is not defined!" % (name)
    

    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "The input: %d is not in defined!" % (number)
        
    # We could also use a dictionary
    # names = {"rock":0, "Spock":1,"paper":2, "lizard":3,"scissors":4 }
    # number = names["rock"]
    # which returns number = 0
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print "\n"

    # print out the message for the player's choice
    print "Player chooses %s" %(player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses %s" %(comp_choice)

    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if (difference == 1) or (difference == 2):
        print "Computer wins!"
    elif (difference == 4) or (difference == 3):
        print "Player wins!"
    elif (difference == 0):
        print "Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


