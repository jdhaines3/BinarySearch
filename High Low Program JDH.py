#want to create main high low function, with option to repeat the game after
#need to define main

#-----main-----#
def main():
    #generate random number between 1 and 100 with "random module"
    #import random and create variable for random.randit(1,100)

    import random
    i = random.randint(1,100)

    #turn = 0 variable for number of turns it takes
    turn = int(0)
    keepGoing = True
    print("""Let's play a game!
I'm thinking of a number between 1 and 100.
You try and guess in the minimal amount of tries.
I'll let you know if you are too high, too low, or spot on.
Let's do this!""")
    #while loop---keepgoing = true
    while (keepGoing):
    #input please enter number
        turn = turn + 1
        guess = int(input("{}) Please enter a number!\n".format(turn)))
    #if input too high, print too high, repeat and turn +1
        if guess > i:
            print("Too high! Try again!")
    #elif input too low, print too low, repeat and turn +1
        elif guess < i:
            print("Too low! Try again!")
    #elif input correct, print correct and keepgoing = false
        elif guess == i:
            print("DING DING DING! WE HAVE A WINNER!")
            keepGoing = False
    #else couldn't understand, please enter integer between 1 and 100
        else:
            print("I'm sorry, I didn't understand. Try entering a number next time.")
#it took {} turns.format(turn)
    print("It only took you {} turns! Congrats!".format(turn))

#run main
main()
#ask if want to repeat
#while loop for options from try again question
repeat = True
while (repeat):
    tryagain = input("Would you like to try again (y/n)?\n")
    #if y, repeat main
    if tryagain == "y":
        main()
    #if n, exit while loop
    elif tryagain == "n":
        print("Ok! Thanks for playing!")
        repeat = False
    #else say didn't understand and loop back to try again question
    else:
        print("I didn't understand...sorry.")
print("See you later!")
