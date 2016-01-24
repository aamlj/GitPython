#Author: Mike Jones
# This program will display the factorial value of a number
n = input("Enter your number: ")

def factorial (n):#method to calculate factoral value
    i=1
    while n >=1:
        i = i * n
        n = n-1
    return i
answer = factorial(n)#call my method
print answer
