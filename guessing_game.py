# Francesca Ramunno
# December 15 2016

######################################################################
## Guess my number game ##
#
# The computer will randomly generate a number between 1 and 100
# and the player will try to guess it.
# The computer will either respond with 'Lower' or 'Higher' based
# on the guess and will count the number of tries it takes
# the player to guess correctly.
######################################################################


import random;


#####################################################################
# This function asks the user if they would like to continue the game
# and returns true or false based on the users response
#####################################################################


def continueGame():
    sValToCheck = raw_input("Would you like to continue? Press 'Y' to continue or any other key to exit ");
    if (sValToCheck == "Y" or sValToCheck == "y"):
        return True;
    else:
        return False;


#######################################################################
#
# Start the game
#
#######################################################################

# print out game instructions only once

print("~~Welcome to the 'Guess My Number' game!~~");
print("\n~~I'm thinking of a number between 1 and 100...~~");
print("\n~~Try to guess it in as few attempts as possible~~")
print("\n\t\tBest of luck!\t\n\n");

keepPlaying = True; # this is a flag to continue the game

while keepPlaying:
    
    iNumToGuess = random.randint(1,100); # this is the random number between 1 and 100 to guess

    iGuess = int(input("\nTake a guess: "));
    iNumTries = 1; # variable to track the number of tries

    # keep asking until the guess is correct
    if iGuess == iNumToGuess:
        print "You guessed it! And it was on the first try -- good job!";
        keepPlaying = continueGame();
        
    else:
        
        while iGuess != iNumToGuess:
            
            if iGuess > iNumToGuess:
                print("Lower...\n");
                
            else:
                print("Higher...\n");
                
            iGuess = int(input("Take a guess: "));
            iNumTries += 1;
                
        print "You guessed it! It took you", iNumTries, "tries\n";
        keepPlaying = continueGame();
        


        
    
