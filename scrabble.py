#import urllib
#Text = urllib.urlopen(weblink)
word =raw_input("Enter your word: ") 
#import random
f = open("wordlist.txt", 'r')
x =f.read() 
x = (x.split())
    #firstWord = random.choice(word)
def scrabble(word):
    letter = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1,'f':6, 'g':2, 'h':4,
           'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3,#create my dictionary
           'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8,
           'y':4, 'z':10}
    value = 0 
    if(word in x):
        for i in word :
            if(i in letter):
                value = value + letter[i]#replaces letter with other letter in dictionary
        else:
            print "man, that word ain't in the list!"
    print "The total of your points for",word,"is ", value
scrabble(word)
