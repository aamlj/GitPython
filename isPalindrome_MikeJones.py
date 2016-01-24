def isPalindrome(x):
    if str(x) == str(x)[::-1]:               # use slicing we learned in class   
        print True
    else:
        print False


isPalindrome('dad')
isPalindrome('Go hang a salami; I’m a lasagna hog')
isPalindrome('daddy')
isPalindrome('booby')
