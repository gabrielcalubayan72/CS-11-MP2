#CALUBAYAN, Gabriel Aldrich S., 2021-06299, CS 11 H1
#ODHUNO, Shane I., 2021-06336, CS 11 H1

winmsg = """⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡟⠉⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⡀⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⡀⠄⠄⠄⢹⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣧⠄⠄⠄⠈⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡄⠄⠄⢸⣠⣶⡷⠄⢰⣿⡿⠄⠈⠙⢿⡇⠄⠄⢠⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⠄⠄⣿⣟⣁⣀⡀⢸⣿⡇⠘⠻⢿⡌⡇⠄⠄⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⠄⢰⣿⣿⣿⣍⣵⣿⣿⣷⡰⢤⣄⢻⡇⠄⠄⣼⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣄⢸⣿⣿⡿⢿⣿⣿⣿⣿⢿⣿⣿⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⠿⢾⣿⠋⠄⣼⠛⠻⠿⠿⡇⢻⣿⣿⡇⠄⣰⣿⣿⣿⣿⣿⣿
⣾⣿⣿⣿⣿⣿⡄⢸⣧⠄⠄⣿⣄⡀⠄⢠⠃⠄⠙⢿⡇⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡃⠈⣿⡇⠄⢈⣉⡉⠉⠛⠃⠄⠄⢸⠁⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣄⣿⣿⣾⣦⡙⠛⠟⠃⣀⣰⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⣷⣿⣿⣿⡏⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿
⢹⣿⣿⣿⣿⣿⣿⣿⠄⠈⣿⣿⣧⣄⣤⣿⣿⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⠸⣿⣿⣿⣿⣿⠇⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠉⠙⠛⠉⠁⠄⠄⠄⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿"""

welcome = """
==============================================
            Welcome to Mastermind
==============================================
"""

print(welcome)

import random as rd
import sys

#main function that executes the game itself
def mainCode(theuserinp):
    #stores patterns you've guessed already
    history = []

    #stores the revealed positions in the lifelines to prevent repeating clues
    life_history = []
    
    #number of guesses and lifelines
    guesses = 10
    life1 = 1
    life2 = 1
    
    #generates random pattern with user-inputted lengths between 4, 6, or 8 digits
    length = int(theuserinp)
    pattern = []
    for i in range(length):
        n = rd.randint(0,9)
        pattern.append(n)

    print('\n' + "Hidden code is of length " + str(length) + ".")
    print("Total number of Guesses: 10")

    while guesses > 0:
        print("\n" + "Guess #" + str(11 - guesses))
        guess = input("Enter guess: ")
        
        #lifeline#1
        if guess == "Lifeline#1":
            if guesses > 1:
                if life1 > 0:
                    guesses -= 1
                    life1 -= 1
                    digit = rd.choice(pattern)
                    pos = pattern.index(digit) + 1
                    while pos in life_history:
                        digit = rd.choice(pattern)
                        pos = pattern.index(digit) + 1
                    life_history.append(pos)
                    print("Hidden code contains digit " + str(digit))
                    print("Note: Total number of guesses is reduced by 1.")
                else:
                    print("You have already used Lifeline#1.")
            else:
                print("You don't have enough guesses for Lifeline#1.")
        
        #lifeline#2 
        elif guess == "Lifeline#2":
            if guesses > 2:
                if life2 > 0:
                    guesses -= 2
                    life2 -= 1
                    digit = rd.choice(pattern)
                    pos = pattern.index(digit) + 1
                    while pos in life_history:
                        digit = rd.choice(pattern)
                        pos = pattern.index(digit) + 1
                    life_history.append(pos)
                    print("Hidden code contains digit " + str(digit) + " at position " + str(pos))
                    print("Note: Total number of guesses is reduced by 2.")
                else:
                    print("You have already used Lifeline#2.")
            else:
                print("You don't have enough guesses for Lifeline#2.")
        
        elif guess == "Reveal":
            print("GAME OVER!")
            print("Code: " + str(pattern))
            user_retry()
        
        #checks if input is all numbers
        elif not guess.isnumeric():
            print ("Invalid guess." + "\n" + "Code only uses symbols 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9")
            print("Do not put letters, spaces, or any other symbols.")
        
        else:
            #converts input into list with integer elements
            guess = [int(x) for x in str(guess)]
            
            #when user guesses correctly
            if guess == pattern:
                print("YOU WIN!!!")
                print(winmsg)
                guesses == 0
                user_retry()
            
            #checks if input is of valid length or if it has been guessed already
            if len(guess) != length:
                print ("Invalid guess." + "\n" + "Code is of length " + str(length))
            elif guess in history:
                print ("Invalid guess." + "\n" + "You guessed that already.")
            
            #when user guesses wrong
            else:
                guesses -= 1
                
                #right color and position
                red = 0
                
                #right color, wrong position
                white = 0
                
                #creates a separate list copy of the pattern and user guess
                dummy_pattern = pattern[:]
                dummy_guess = [int(x) for x in guess] 
    
                #loop to set up clues for the player move
                for index1, input1 in enumerate(dummy_guess):
                    if input1 == dummy_pattern[index1]:
                        red += 1
                        dummy_pattern[index1] = "checked solution"
                        dummy_guess[index1] = "checked user"

                for index1, input1 in enumerate(dummy_guess):
                    for i, p in enumerate(dummy_pattern):
                        if p == input1:
                            white += 1
                            dummy_pattern[i] = "checked solution"
                            break
                    
                print(str(red) + "R" + " - " + str(white) + "W")
                print("You have " + str(guesses) + " guesses left.")
                
                #if there are no guesses left
                if guesses == 0:
                    print("GAME OVER! Try again.")
                    print("Code: " + str(pattern))
                    #asks user if they want to try again.
                    #if yes, game starts over with a new pattern
                    guesses = 10
                    user_retry()
                    
        history.append(guess)

#function that asks the user to retry if so desired
def user_retry():
    retry = input('\n' + "Retry? (Y/N): ")
    if retry == "Y":  
        diff_option = (input("Do you want to set the difficulty? (Y/N): "))
        if diff_option == "Y":
            difficulty = input('\n' + """Please choose among "Easy", "Medium", and "Hard" to determine the length of the pattern: """)    
            if difficulty == "Easy": 
                mainCode(4)
            elif difficulty == "Medium":
                mainCode(6)
            elif difficulty == "Hard":
                mainCode(8)
            else:
                print('\n' + """Kindly only choose among "Easy", "Medium", and "Hard" difficulties. Please restart and try again.""")     
        elif diff_option == "N":
            difficulties = [4, 6, 8]
            mainCode(rd.choice(difficulties)) 
        else: 
            print('\n' + """Kindly only choose among "Y" or "N". Please restart and try again.""")
    else:
        print()
        print("Thank you for playing!")
        print("By Calubayan and Odhuno")
        sys.exit()

#asks the user for the desired length of the pattern
print("Before playing, please refer to the User Manual for the Instructions. ")
diff_option = (input("Do you want to set the difficulty? (Y/N): "))

if diff_option == "Y":
    difficulty = input("""Now, please choose among "Easy", "Medium", and "Hard" to determine the length of the pattern: """)
    if difficulty == "Easy": 
        mainCode(4)
    elif difficulty == "Medium":
        mainCode(6)
    elif difficulty == "Hard":
        mainCode(8)
    else:
        print('\n' + """Kindly only choose among "Easy", "Medium", and "Hard" difficulties. Please restart and try again.""")
elif diff_option == "N":
    difficulties = [4, 6, 8]
    mainCode(rd.choice(difficulties))
else: 
    print('\n' + """Kindly only choose among "Y" or "N". Please restart and try again.""")