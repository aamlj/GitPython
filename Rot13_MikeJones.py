#Author: Mike Jones
#converts text pulled of the internet using the Rot13 method.


import urllib
Text = urllib.urlopen('http://gaweda.herokuapp.com/hw/rot13')#pull statement from internet

line = Text.readline().lower()#convert to all lowercase
   

#print line#test that the statement is right

letter = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r','f':'s', 'g':'t', 'h':'u',
           'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',#create my dictionary
           'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
           'y':'l', 'z':'m'}
answer = ""#create a string
for i in line:#go through each letter in the phrase
    if (i in letter):
        answer = answer + letter[i]#replaces letter with other letter in dictionary
    else:
        answer = answer +  i#makes space and punctuation

print answer
             












    
