#Author: Mike Jones

#Program Description: Tells user if it is a good or dull party based on is it the week

#end and how many cigars there are

cigars = raw_input("How many cigars?")  # prompt user to enter number of cigars

weekend = raw_input("Is it the weekend?")  # prompt user to enter yes or no 

if weekend == "yes" and cigars<="40":  # if both are true then print line as output

    print  ("That ain't no party")
    
elif cigars<='60' or cigars>='40':  # if both are true then print line as output

    print ("Now that's a  party!")

elif  cigars<='40' and weekend == "no": #if both are true then print line as input

   print ("That ain't no party!")
