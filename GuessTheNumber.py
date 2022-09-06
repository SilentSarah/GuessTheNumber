# Project Name: Guess The Number (With multiple modes: player guessing the number / computer guessing the number)
# Difficulty Level: Low
# Developer: Sarah Hicham Meftah
# Date: 06/09/2022

import random
import time

tries = 3
cookies = 0
diffci = 0
modei = 0
guesses = [0,0,0,0,0]

global easyR
global medR
global hardR

def DifficultyChooser():
    global diffci
    print("Choose Your Difficulty.")
    diffc = input("1) Easy (5 Numbers range)\n2) Mediocre (7 Numbers range)\n3) Hard (10 Numbers Range)\n")
    diffci = int(diffc)
    OnGameProccess(modei, diffci)

def ModeChooser():
    global modei
    global guesses
    print("GUESS THE NUMBER: THE GAME")
    mode = input("\n1) Player Guesses the number\n2) Computer Guesses the number\n")
    modei = int(mode)

    DifficultyChooser()

def RestartGame():
    
    global tries
    global cookies
    print("GAME OVER")
    print("You have lost")
    restart = input("Type 'restart' if you want to restart the game or 'exit' to quit\n")
    if restart == "restart":
        tries = 3
        cookies = 0
        ModeChooser()
    elif restart == "exit":
        exit()
    else:
        return RestartGame()

def CheckAnswer(answer, dif):
    global tries
    global cookies
    global diffci
    tries -= 1
    if int(answer) != dif:
        return Prompt(dif)
    elif int(answer) == dif:
        print("Congratulations You guessed it correctly and you have won one cookie!")
        cookies += 1
        tries += 1
        return OnGameProccess(modei, diffci)
    
def Prompt(dif):
    match diffci:
        case 1:
            if tries > 0:
                choice = input("A number has been chosen, please type a number between 1 and 5, you have " + str(tries) + " tries left\n")
                CheckAnswer(choice, dif)
            else:
                RestartGame()
        case 2:
            if tries > 0:
                choice = input("A number has been chosen, please type a number between 1 and 8, you have " + str(tries) + " tries left\n")
                CheckAnswer(choice, dif)
            else:
                RestartGame()
        case 3:
            if tries > 0:
                choice = input("A number has been chosen, please type a number between 1 and 10, you have " + str(tries) + " tries left\n")
                CheckAnswer(choice, dif)
            else:
                RestartGame()

def BotCalc():
    global diffci
    global tries
    global guesses

    match diffci:
        case 1:
            if tries > 0: 
                tries -= 1
                
                print("Guessing...")
                time.sleep(3)
                brand = random.randint(1, 5)
                i = 0
                for i in range(len(guesses)):
                    if guesses[i] == 0:
                        guesses[i] = brand
                        print(guesses[i])
                        break
                    elif guesses[i] == brand:
                        brand = random.randint(1, 5)
                answer = input("Computer has guessed the number: " + str(brand) + " ,is it the correct answer? (y/n)(" + str(tries) + " tries left)\n")
                match answer:
                    case 'y':
                        print("The Computer has guessed the number correctly. You lose!")
                        print("Returning back...")
                        time.sleep(3)
                        ModeChooser()
                    case 'n': BotCalc()
            else:
                print("The Computer couldn't guess the number. You win!")
                print("Returning back...")
                time.sleep(3)
                ModeChooser()
        case 2:
            if tries > 0: 
                tries -= 1
                print("Guessing...")
                time.sleep(3)
                brand = random.randint(1, 5)
                i = 0
                for i in range(len(guesses)):
                    if guesses[i] == 0:
                        guesses[i] = brand
                        print(guesses[i])
                        break
                    elif guesses[i] == brand:
                        brand = random.randint(1, 7)
                answer = input("Computer has guessed the number: " + str(brand) + " ,is it the correct answer? (y/n)(" + str(tries) + " tries left)\n")
                match answer:
                    case 'y':
                        print("The Computer has guessed the number correctly. You lose!")
                        print("Returning back...")
                        time.sleep(3)
                        ModeChooser()
                    case 'n': BotCalc()
            else:
                print("The Computer couldn't guess the number. You win!")
                print("Returning back...")
                time.sleep(3)
                ModeChooser()
        case 3:
            if tries > 0: 
                tries -= 1
                print("Guessing...")
                time.sleep(3)
                brand = random.randint(1, 10)
                i = 0
                for i in range(len(guesses)):
                    if guesses[i] == 0:
                        guesses[i] = brand
                        print(guesses[i])
                        break
                    elif guesses[i] == brand:
                        brand = random.randint(1, 10)
                answer = input("Computer has guessed the number: " + str(brand) + " ,is it the correct answer? (y/n) (" + str(tries) + " tries left)\n")
                match answer:
                    case 'y':
                        print("The Computer has guessed the number correctly. You lose!")
                        print("Returning back...")
                        time.sleep(3)
                        ModeChooser()
                    case 'n': BotCalc()
            else:
                print("The Computer couldn't guess the number. You win!")
                print("Returning back...")
                time.sleep(3)
                ModeChooser()


def OnGameProccess(mode, diff):

    global tries
    global guesses
    if modei < 1 or modei > 2 or diff < 1 or diff > 3:
        print(modei, diff)
        return ModeChooser()
    if modei == 1: # This will make the computer choose a number based on the difficulty chosen
        
        match diffci:
            case 1:                            
                tries = 3
                easyR = random.randint(1, 5)
                print("Selecting a random number")
                time.sleep(2)
                Prompt(easyR)                          
            case 2:
                tries = 4
                medR = random.randint(1, 7)
                print("Selecting a random number")
                time.sleep(2)
                Prompt(medR)   
            case 3:
                tries = 5
                hardR = random.randint(1, 9)
                print("Selecting a random number")
                time.sleep(2)
                Prompt(hardR)

    if modei == 2: # Computer will try to guess the number
        guesses = [0,0,0,0,0]
        match diffci:
            case 1:
                tries = 3
                print("Difficulty chosen: Easy")
                time.sleep(1)
                print("You have 3 seconds to think of a number between 1 and 5")
                time.sleep(1)
                BotCalc()
            case 2:
                tries = 4
                print("Difficulty chosen: Mediocre")
                time.sleep(1)
                print("You have 3 seconds to think of a number between 1 and 7")
                time.sleep(1)
                BotCalc()
            case 3:
                tries = 5
                print("Difficulty chosen: Hard")
                time.sleep(1)
                print("You have 3 seconds to think of a number between 1 and 10")
                time.sleep(1)
                BotCalc()
       
ModeChooser()


