inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
newinv  = {'rope': 5, 'torch': 6, 'gold coin': 4}

def displayInventory(intentory):
  print("Inventory:")
  totalitems = 0
  for k,v in inventory.items():
    print(v ," ",k)
    totalitems +=v
  print("\nTotal items is ",totalitems)

def addtoinventory(newinv,inventory):

    for k,v in inventory.items():
        inventory[k] = inventory[k] + newinv.get(k,0)

    return inventory


displayInventory(inventory)

inventory = addtoinventory(newinv,inventory)
print("\nInventory updated")
displayInventory(inventory)

