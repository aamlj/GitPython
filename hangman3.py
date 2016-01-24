#Author: Mike Jones
# The classic game of hangman#


import random
def playGame():
    #get wordlist from file
    f = open("wordlist.txt", 'r')
    playAgain = True
    #set boolean to loop at end
    while (playAgain):
        #ascii characters for art set into a list
        hangMan = ['''
         ________
        |/    |
        |
        |
        |
        |
        |
        |___ ''','''



         ________
        |/    |
        |    (_)
        |
        |
        |
        |
        |___''', '''


         ________
        |/    |
        |    (_)
        |     |
        |     |
        |
        |
        |___''', '''


         ________
        |/    |
        |    (_)
        |    \|
        |     |
        |
        |
        |___''', '''

         ________
        |/    |
        |    (_)
        |    \|/
        |     |
        |
        |
        |___''', '''


         ________
        |/    |
        |    (_)
        |    \|/
        |     |
        |    /
        |
        |___''', '''


         ________
        |/    |
        |    (_)
        |    \|/
        |     |
        |    / \\
        |
        |___''' ]



        #read the file
        word= f.read()

        #divide txt. file into individual words
        word = (word.split())

        #use choice() to pick random word from list
        newWord = random.choice(word)

        #set the blanks for placeholders of word
        blanks = '_' * len(newWord)

        #set empty list for letters that have been used
        alreadyGuessed = []

        #since player can only guess wrong letter 6 times(including 0)
        chance = 6

        #set boolean to determine if all blanks are filled or not
        correct = False
        #print newWord
        #run through all 7 chances so it will display right graphics
        #this works but need some kind of loop here
        while not correct and chance > 0:
            if chance == 6:
                print hangMan[0]
            elif chance == 5:
                print hangMan[1]
            elif chance == 4:
                print hangMan [2]
            elif chance == 3:
                print hangMan [3]
            elif chance == 2:
                print hangMan [4]
            elif chance ==1:
                print hangMan[5]
            elif chance == 0:
                print hangMan [6]
            print ""

            #print the placeholders together and create whitespace around it
            print (" ".join(blanks))
            print ""
            print ""

            # keep a tally of what has been quessed
            print "You have guessed the letter:", alreadyGuessed

            #get user input
            guess = raw_input("Enter your letter: ")

            #set all input to lower case
            guess = guess.lower()

            # make sure user enters valid input
            while not guess.isalpha() or guess in list(alreadyGuessed):
                if not guess.isalpha():
                    print "Man, you know to enter a letter!"
                    guess = raw_input ("Enter your letter: ")
                if guess in list(alreadyGuessed):
                    print "You already used that letter"
                    guess = raw_input("Enter your letter: ")

            #add the input to the list of used letters
            alreadyGuessed.append(guess)

            #replace placeholders with input if guess is correct
            if guess in newWord:
                blanks = "".join([char if char in alreadyGuessed else '_' for char in newWord])
            else:
                chance -=1
            print ""
            print (" ".join(blanks))
            # handles if the player gets the word right
            if blanks == newWord:
                    correct == True
                    print "You win!"
                    anotherRound = raw_input("Play again? y/n")
                    anotherRound = anotherRound.lower()
                    if anotherRound =='y':
                        playGame()
                    else:
                        print ("GoodBye!")

            #otherwise subtract 1 from chance and print the updated blanks
            #else:
                #chance -= 1
           # print ""
            #print (" ".join(blanks))

        #print the art with no more guesses
        print hangMan[6]
        print "Your man is dead! The word was", newWord

        #prompt user to play again
        anotherRound = raw_input ("Would you like to play again:  y/n ")

        #set input to lower case to check for validity
        anotherRound = anotherRound.lower()
        if anotherRound == 'y':
           playGame()

        #if user types anything other then y game over
        else:
            print ("Goodbye!")
            break
        #close file
        #newWord = f.close()
playGame()
