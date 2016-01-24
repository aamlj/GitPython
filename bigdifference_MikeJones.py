#Author: Mike Jones
# This program will find and print the difference in the largest and smallest
# number in an array.



a=0;

def big_diff(array):        #method to find difference in max and min
    return max(array) - min(array)

a = big_diff([10, 3, 5, 6])
print a

a = big_diff([7, 2, 10, 9])#call the method and print results
print a

a = big_diff([2, 10, 7, 2])
print a
