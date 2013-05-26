#!/usr/bin/python
#Corey Lundon  5/25/2013

"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""

#stores the largest palindrome and the 2 3-digit numbers
answer = 0
a = 0
b = 0

def palindrome_check(string):
    """Returns True if the string is the same forwards and backwards"""

    #reverse the string
    reverse_string = string[::-1]

    #return true if the two strings are equal, otherwise return false
    if (string == reverse_string):
        return True
    return False

#loop through the 3-digit numbers
#start high and go down since we are looking for the largest product
for x in range(999, 100, -1):
    for y in range(x, 100, -1):

        #convert the number to a string and check if it is a palindrome
        if (palindrome_check(str(x*y))):

            #check if the product is larger than the previous one
            if (answer < x*y):
                
                #store the product and the numbers used to compute it
                a, b = x, y
                answer = x*y

                #no need to stay in inner loop since we are going backwards
                break

print("The largest palindrome made from the product of two 3-digit numbers is %s made from %d * %d." % (answer, a, b))
