# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Saylor Sherrodd
#                   Spencer Jones
#                   Ricardo Mejia
#                   Andrew Spears
#                   Anderson Loan
# Section:         574
# Assignment:   Lab 8.10
# Date:         12 10 2022
#

zero = ['000','0 0', '0 0', '0 0', '000']#define each symbol
one = [' 1 ', '11 ', ' 1 ', ' 1 ', '111']
two = ['222', '  2', '222', '2  ', '222']
three = ['333', '  3', '333', '  3', '333']
four = ['4 4', '4 4', '444', '  4', '  4']
five = ['555', '5  ', '555', '  5', '555']
six = ['666', '6  ', '666', '6 6', '666']
seven = ['777'] + ['  7' for i in range(4)]
eight = ['888', '8 8', '888', '8 8', '888']
nine = ['999', '9 9', '999', '  9', '999']
colon = [' ', ':', ' ', ':', ' ']

symbols = {'0' : zero, #put all symbols in dict for easy access
           '1' : one,
           '2' : two,
           '3' : three,
           '4' : four,
           '5' : five,
           '6' : six,
           '7' : seven,
           '8' : eight,
           '9' : nine,
           ':' : colon} 

time = input('Enter the time: \n') #get input, and add spaces 

for k in range(5): #loop through each line, and print parts of each number
    for i in time:
        print(symbols[i][k], end = ' ') #print the corresponding line of each number, and do not add newline
    print() #move to next line