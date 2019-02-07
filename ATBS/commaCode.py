def comma(listy):
    myStr = ''
    for i in range(len(listy)):
        if i == len(listy) - 1:
            myStr = myStr[:-2]
            myStr += ' and ' + str(listy[i])
            return myStr
        myStr += str(listy[i]) + ', '

aList = ['apples', 'bananas', 'tofu', 'cats']
bList = [23,554,38.4]
cList = ['bobby', 24, 'aardvark', 'knight', 28390.4, 20000]
print(comma(cList))
        
