def average (a,b,c): # create a function for average
    """ this function will take the average of three values by adding together

        and dividing by three"""

    return ((a+b+c)/3) #formula for computing averages
             
avg1 = average (9, 9, 9) #create varible avg1

x=int (input ("Enter first number: ")) #ask for input from user

y=int (input("Enter second number: ")) #ask for input from user

z=int (input("Enter third number: "))  #ask for input from user

avg2=average (x,y,z) #create varible avg2

avg3=average (x,9,z)  #create varible avg3

print avg1, avg2, avg3
