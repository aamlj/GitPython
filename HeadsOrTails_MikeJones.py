#author:Mike Jones

# Program that will flip a coin a million times and display how many times it
#will be on heads or tails using the random function

#dont forget to import random
import random

# i have to make three varibles heads, tails and the counter to increment  
heads=0
tails=0
i=1

#gonna need a while statement so it will loop 1000000 times. 
while (i<=1000000):
    #this will pick a number between 0 and 1
    number=( random.random())
    # increment my number to prevent an infinite loop
    i+=1
    #create a conditional to determine what is labeled as heads or tails
    if number<.5:
        #add 1 to heads if this is true
        heads+=1
    # otherwise and 1 to tails     
    else:
        tails+=1
       
       
                                #total of heads              #total of tails
print "The coin landed on heads", heads, "times and on tails",tails ,"times."

