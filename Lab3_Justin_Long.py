#printing welcome message
print("Welcome to Flarsheim Guesser!")
#variable to store user choice
choice = 'y'
#a while loop to run until user choice is 'n' or 'N'
while(choice == 'Y' or choice == 'y'):
    #asking user to think of a number
    print("\nPlease think of a number between and including 1 and 100.")
    #variables for the remainders of 3,5,7
    Three_Remainder = 0
    Five_Remainder = 0
    Seven_Remainder = 0
    #reading remainder when number is divided by 3
    Three_Remainder = int(input("\nWhat is the remainder when your number is divided by 3? "))
    #a while loop to ask user input until they answer correctly
    while(Three_Remainder < 0 or Three_Remainder >=3):
        #checking for negative numbers
        if Three_Remainder < 0 :
            #printing error message
            print("The value entered must be 0 or greater")
        #checking if number is greater or equal to 3, which it can't be since it's the remainder of input/3
        elif Three_Remainder >=3:
            #printing error message
            print("The value entered must be less than 3")
        #asking remainder from user again
        Three_Remainder = int(input("What is the remainder when your number is divided by 3? "))
    #reading remainder when number is divided by 5
    Five_Remainder = int(input("\nWhat is the remainder when your number is divided by 5? "))
    #a while loop to ask user input until they answer correctly
    while(Five_Remainder < 0 or Five_Remainder >=5):
        #checking for negative numbers
        if Five_Remainder < 0 :
            #printing error message
            print("The value entered must be 0 or greater")
        #checking if number is greater or equal to 5, which it can't be since it's the remainder of input/5
        elif Five_Remainder >=3:
            #printing error message
            print("The value entered must be less than 5")
        #asking remainder from user again
        Five_Remainder = int(input("What is the remainder when your number is divided by 5? "))
    #reading remainder when number is divided by 7
    Seven_Remainder = int(input("\nWhat is the remainder when your number is divided by 7? "))
    #a while loop to ask user input until they answer correctly
    while(Seven_Remainder < 0 or Seven_Remainder >=7):
        #checking for negative numbers
        if Seven_Remainder < 0 :
            #printing error message
            print("The value entered must be 0 or greater")
        #checking if number is greater or equal to 7, which it can't be since it's the remainder of input/7
        elif Seven_Remainder >=7:
            #printing error message
            print("The value entered must be less than 7")
        #asking remainder from user again
        Seven_Remainder = int(input("What is the remainder when your number is divided by 7? "))

    for i in range(1,101):
        #checking each number to see if it matches the qualities
        if(i%3 == Three_Remainder and i%5 == Five_Remainder and i%7 == Seven_Remainder):
            #after correct number is found, printing what their number was
            print("Your number was",i)
            print("How amazing is that?\n")
    #asking user if they want to play again
    choice = input("Do you want to play again? Y to continue, N to quit ==> ")
    #repeat the question until they answer correctly, either y to play again or n to quit
    while(choice !='Y' and choice != 'N' and choice != 'y' and choice != 'n'):
        choice = input("Do you want to play again? Y to continue, N to quit ==> ")
    

    
      
