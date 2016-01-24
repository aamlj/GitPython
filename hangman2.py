import random
HangMan = ['''
 ________
|/    |
|    
|    
|     
|    
|      
|___''', '''



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
|    / \
|      
|___''' ]



#print HangMan[0]

f = open("wordlist.txt", 'r')
words= f.read()
#while (playAgain):
word = random.choice(words.split())
lives = 6
guess = ''
def play():
    #word = pick_a_word()
    while True:
        guess = getGuess(word)
        if processGuess(guess, word):
            print('You win! Well Done!')
            break
        if lives == 0:
            print('Game Over!')
            print('The word was: ' + word)
            break
def getGuess(word):
    blanks(word)
    #print('Lives Remaining: ' + str(lives_remaining))
    guess = raw_input(' Guess a letter or whole word?')
    return guess


def blanks(word):
    word = ''
    for letter in word:
        if guess.find(letter) > -1:
        # letter found
            word = word + letter
        else:
        # letter not found
            word = word + '-'
#print(word)


def processGuess(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        return wordGuess(guess, word)
    else:
        return letterGuess(guess, word)


def wordGuess(guess, word):
    #global lives
    if guess.lower() == word.lower():
        return True

    else:
        lives =- 1

        return False
def letterGuess(guess, word):
    #global guessed_letters
    #global lives
    if word.find(guess) == -1:
        lives = lives -1

        guess = guess + guess.lower()
        if allLetters(word):
            return True
    return False
def allLetters(word):
    for letter in word:
        if guess.find(letter.lower()) == -1:
            return False
    return True
play()
