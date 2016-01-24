#Author: Mike Jones
# This program will print a random number of a given array

import random
def randomChoice(numberlist): #create my method 
   
    x=random.randint(0,len(numberlist))# this will return random integer
    return x


    
numberlist=[1,2,3,4,5]
numberlist2=[2,4,6,8,10]
numberlist3=[3,6,9,12,15]  #calling my function
numberlist4=[4,8,12,16,20]
numberlist5=[5,10,15,20,25]

print randomChoice(numberlist)
print randomChoice(numberlist2)
print randomChoice(numberlist3)  #print results
print randomChoice(numberlist4)
print randomChoice(numberlist5)






 
