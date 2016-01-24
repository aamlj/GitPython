#Author: Mike Jones
# This program creates a neat multiplication table based on user input

x = input ("Enter your number: ")
i = 1

while i <= x:
    n = 1
    print " "  # put space between rows (extra)
    while n <= x:       #nested while loop
        print '\t',(i * n),#tab between columns to make it nice
        n += 1
    print " "
    i += 1

