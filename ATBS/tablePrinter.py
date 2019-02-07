#! python3
# tablePrinter.py - right justifies columns of strings from a list

def printTable(myStrs):
    newStr = ''
    colWidths = [0] * len(myStrs)

    for a in range(len(myStrs)):
        for b in range(len(myStrs[0])):
            strLen = len(myStrs[a][b])
            if strLen > colWidths[a]:
                colWidths[a] = strLen
                
    for a in range(len(myStrs[0])):
        for b in range(len(myStrs)):
            newStr += myStrs[b][a].rjust(colWidths[b]) + ' '
        newStr += '\n'

    print(newStr)
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)            
