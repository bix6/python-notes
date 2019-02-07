def displayInventory(myInv):
    print('Inventory:')
    totalItems = 0
    for k, v in myInv.items():
        print(str(v) + ' ' + str(k))
        totalItems += v
    print('Total number of items: ' + str(totalItems))

# invA = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# displayInventory(invA)


def addToInventory(myInv, newItems):
    for i in newItems:
        myInv.setdefault(i,0)
        myInv[i] += 1
    return myInv


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
