#Corey Lundon  5/24/2013

"""Complete this program to find the greatest produdct of five consecutive
digits in the list"""

#read in the list and strip off the new line characters
in_file = open('array.txt')
series = in_file.read().replace('\n', '')

#stores the largest product of 5 consecutive digits in the list
answer = 0

#start at the first element and stop at the start of the last group of 5
for i in range(0, len(series)-4):    
    #slice off groups of 5 consecutive digits
    partial = series[i:i+5]

    #used to multiply the first element by 1
    element = 1

    #iterate through the groups of 5 
    for j in partial:
        #convert the string to int and multiply the consecutive digits together
        element *= int(j)

    #keep track of the largest product
    if(element > answer):
        answer = element

#print the answer to the screen
print("The largest product of 5 consecutive digits is %s" % (answer))
