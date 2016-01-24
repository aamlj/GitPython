#Author: Mike Jones
#HiLo is a game where user sets upper and lower bounds and then guesses the number

import random

#get the users lower number
def getLowerBound():

        low = input ("Enter your lower number:")

        return low

#force user to enter a number greater than low
def getUpperBound(low):

        upper=input("Enter your upper number:")
        
        while low>=upper:

                print ("I told you lower number first!")

                upper=input("Enter your upper number:")

        return upper

#generate a number in the "bounds" the user set
def getNumber(upper,low):

        number=random.randint(low,upper)

        return number

#compare users guess to the random number and let them know if too high or too low
def HiLo(g, a):

        while g!=a:

           g = input("Your guess:")

           if g < a:

                print ("Too Low!")

           elif g>a:

                print ("Too high!")

           else:

                print ("correct")        

#prompt user if they want to play again
def playAgain():

        x=raw_input ("Do you want to play again? yes or no")

        while (not(x == 'yes' or x == 'no')):

                print("Invalid selection!!!") #force user to enter 'yes' or 'no'

                x=raw_input ("Please enter yes or no")
                   
        if x=="yes":

                return True
        else:
                return False


again  = True

while again:

        low=getLowerBound()

        upper=getUpperBound(low)

        number=0                        #call my methods

        number=getNumber(upper,low)

        a=getNumber(upper,low)

        g=0

        HiLo(g,a)                

                
        again = playAgain()

print "Thanks for playing, Goodbye"








