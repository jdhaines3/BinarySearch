#need main computer guess function with while loop play again at end
#have computer guess your number, start halfway then divide by two depending on high/low
#---main---
def main():
#define low point as variable and high point as variable
#define turn variable = 0
    low = int(1)
    high = int(100)
    turn = int(0)
    keepGoing = True
    print("""Hey! Want to play a game?
Think of a number between 1 and 100.
I'll try to guess your number in the lowest amount of turns!
You tell me if I am too high, too low, or correct!
No cheating and switching the number halfway through...
""")
#run a binary search algorithm where low + high / 2 is guess(while loop)
    while (keepGoing):
    #turn = turn +1
        turn = turn + 1
        guess = int((low + high)/2)
    #input variable for h/l/c
        print("{}) I guess: {}".format(turn,guess))
        hlc = input("too (h)igh, too (l)ow, or (c)orrect?\n")
        #if h, new high point = guess; repeat
        if hlc == "h":
            high = guess
        #if l, new low point = guess + 1; repeat
        elif hlc == "l":
            low = guess + 1
        #if c, keepgoing = false; print correct
        elif hlc == "c":
            keepGoing = False
        else:
            print("I don't understand...try again")
    print("I finally got it! It only took {} turns!".format(turn))

#---run main---
main()

#while loop ask to play again, if yes repeat, if no, exit
repeat = True
while (repeat):
    answer = input("Would you like to play again? (y/n)\n")
    if answer == "y":
        main()
    elif answer == "n":
        print("Aw ok, thanks for playing!")
        repeat = False
    else:
        print("I don't understand, please try again")
print("See you soon!")
