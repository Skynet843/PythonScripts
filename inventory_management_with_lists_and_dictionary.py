inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}#dictionary
newinv = ['gold coin', 'dagger', 'gold coin','rope', 'gold coin', 'ruby']#list

def displayInventory(intentory):
  print("Inventory:")
  totalitems = 0
  for k,v in inventory.items():
    print(v ," ",k)
    totalitems +=v
  print("\nTotal items is ",totalitems)

def addtoinventory(newinv,inventory):

	for i in range(len(newinv)):
		inventory.setdefault(newinv[i],0)
		inventory[newinv[i]] +=1


	'''for k,v in inventory.items():
		for new in newinv :
			if k == new:
				inventory[k] = inventory[k] + 1

	for new in newinv:
		if new not in inventory:
			inventory[new] = 1

	return inventory
	// This code also work.
	'''
displayInventory(inventory)

print("\nInventory updated")

displayInventory(addtoinventory(newinv,inventory))



