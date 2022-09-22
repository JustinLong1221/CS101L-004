########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        play = input('Do you want to play again?\n')
        play = play.upper
        if (play == 'Y') or (play == 'YES'):
            return True
        elif (play == 'N') or (play =='NO'):
            return False
        print('You must enter Y/YES/N/NO to continue. Please try again')
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        wager = int(input('How many chips do you want to wager'))
        if wager > bank:
            print('The wager amount cannot be greater than how much you have.  {}'.format(bank))
        if wager < 1:
            print('The wager amount must be greater than 0. Please enter again.')
        else:
            return wager            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    numA = random.randint(1,10)
    numB = random.randint(1,10)
    numC = random.randint(1,10)
    return (numA, numB, numC)

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb) and (reela == reelc):
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        chips = int(input('How many chips do you want to start with?'))
        if (chips > 0 and chips < 101):
            return chips
        elif chips < 1:
            print('Too low a value, you can only choose 1 - 100 chips')
        else:
            print('Too high a value, you can only choose 1 - 100 chips')
    return 0

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager*10
    if matches == 2:
        return wager*3
    return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        initialbank = bank
        count = 0
        newbank = 0
        newhigh = bank

        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > newbank:
                newhigh = bank
            newbank = bank

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            count += 1
           
        print("You lost all {} in {} spins".format(initialbank,count))
        print("The most chips you had was {}".format(newhigh))
        playing = play_again()
