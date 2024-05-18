#can only record result of last game
#If there is no history of game data, the program will create a new file to save the current game data on once it ends
#MUST RUN PROGRAM TWICE to get BOTH results!!!!!
#Duplicate numbers in your guesses still count against your guesses left

import random

def checkguess(guess, count, number, maxguess):
    """Checks the guessed number to be the random number, and makes sure it does not exceed the maximum number of guesses"""
    remainder = maxguess - count
    if int(guess) == number:
        print("Congratulations! You Win The Game!")
        print("You guessed {0} and won the game with {1} guesses to spare!".format(guess, remainder))
        return "You Won"
    else:
        # check number to be lower or higher than number
        if remainder == 0:
            print("You guessed {0} on your last guess and lost the game.".format(guess))
            print("The number you were trying to guess was {0}.".format(number))
            return "You Lost"
        else:
            if int(guess) > number:
                print("You guessed {0}, which is greater than the correct number.".format(guess))
            elif int(guess) < number:
                print("You guessed {0}, which is smaller than the correct number.".format(guess))
                
            print("You have {0} guesses remaining".format(remainder))

def oknums(mode):
    """Finds the range of numbers in difficulty"""
    xs = [0]
    count = 0
    if mode.lower() == "easy":
        t = 10
    elif mode.lower()== "normal":
        t = 100
    elif mode.lower() == "hard":
        t = 1000
    elif mode.lower() == "unrealistic":
        t = 10000
    for num in range(t):
        count += 1
        xs.append(count)
    return xs

def guesscheck(difficulty, maxnum):
    """Checks to see if guess is within range of maxnum in difficulty"""
    xs = oknums(difficulty)
    n = input("Guess a whole number between 0 and {0} \n".format(maxnum))
    try:
        if int(n) in xs:
            return n
    except:
        print("{0} is not a valid guess. Please guess again.".format(n))
        return guesscheck(difficulty, maxnum)

def Easy():
    """Game mode with a number between 0-10"""
    rng = random.Random()
    t = rng.randrange(0, 11)
    print("You chose the difficulty EASY. \nYou get 3 guesses.")
    count = 0
    maxguess = 3
    for guess in range(maxguess):
        n = guesscheck("easy", 10)
        count += 1
        v = checkguess(n, count, t, 3)
        if int(n) == t:
            break
    return v
    

def Normal():
    """Game mode with a number between 0-100"""
    rng = random.Random()
    t = rng.randrange(0, 101)
    print("You chose the difficulty NORMAL. \nYou get 10 guesses.")
    count = 0
    maxguess = 10
    for guess in range(maxguess):
        n = guesscheck("normal", 100)
        count += 1
        v = checkguess(n, count, t, 10)
        if int(n) == t:
            break
    return v

def Hard():
    """Game mode with a number between 0-1000"""
    rng = random.Random()
    t = rng.randrange(0, 1001)
    print("You chose the difficulty HARD. \nYou get 15 guesses.")
    count = 0
    maxguess = 20
    for guess in range(maxguess):
        n = guesscheck("hard", 1000)
        count += 1
        v = checkguess(n, count, t, 15)
        if int(n) == t:
            break
    return v

def Unrealistic():
    """Game mode with a number between 0-10000"""
    rng = random.Random()
    t = rng.randrange(0, 10001)
    print("You chose the difficulty UNREALISTIC. \n You get 20 guesses")
    count = 0
    maxguess = 30
    for guess in range(maxguess):
        n = guesscheck("unrealistic", 10000)
        count += 1
        v = checkguess(n, count, t, 20)
        if int(n) == t:
            break
    return v

def ChooseDifficulty():
    """Menu of Difficulty options"""
    print("What Difficulty Would You Like To Play?")
    print(" (0-10) EASY              Press 'E' \n (0-100) NORMAL           Press 'N' \n (0-1000) HARD            Press 'H' \n (0-10000) UNREALISTIC    Press 'U' \n")
    print(" Then Press Enter")
    difficulty = input(" ")
    t = difficulty.lower()
    if t == "e":
        return str(Easy())
    elif t == "n":
        return str(Normal())
    elif t == "h":
        return str(Hard())
    elif t == "u":
        return str(Unrealistic())
    else:
        print("You did not choose a difficulty. \nPlease pick a difficulty or exit the game.")
        ChooseDifficulty()

    

def EndStart():
    restart = input("Would you like to start a new game? \n    Press Y to play again \n    Press N to quit \n")
    if restart.lower() == "y":
        PlayGame()
    elif restart.lower() == "n":
        exit()      
    else:
        print("Please pick one of the options listed.\n")
        EndStart()

def PlayGame():
    """Starts, saves, and ends game"""
    result = ChooseDifficulty()
    savedata = open("Saved Game Data.txt", "w")
    savedata.write(result)
    savedata.close()
    EndStart()
    

def StartNewGame():
    try:
        savedata = open("Saved Game Data.txt", "r")
        content = savedata.readlines()
        savedata.close()
        print("{0} your last game, would you like to start a new game? \nAll previous game data will be ERASED if you start a new game.".format(str(content)))
        c = input("    Press Y to start \n    Press N to quit \n ")      
        if c.lower() == "y":
            PlayGame()
        else:
            exit()

    except:
        savedata = open("Saved Game Data.txt", "w")
        t = input("Would you like to start a new Game? \n    Press Y to play again \n    Press N to quit \n    Then Press Enter \n")
        if t.lower() == "y":
            PlayGame()
        else:
            exit()


StartNewGame()

