#!/usr/bin/env python3
def collatz(number):
    if number % 2 == 0:
        evenNum = number // 2
        print(evenNum)
        return evenNum
    else:
        oddNum = 3*number+1
        print(oddNum)
        return oddNum

def userInput():
    while(True):
        print('Please enter an integer.')
        try:
            myInt = int(input())
            return myInt
        except ValueError:
            print('That\'s not an integer, Jerry!')
            continue


curVal = collatz(userInput())
while(curVal != 1):
    curVal = collatz(curVal)
