#Who's_your_Daddy.py
#Joe Carty
#11/12/14

import pickle
choice = ()
names = {"Charlie":"Timmy","Dennis":"Will","Mac":"Billy","Frank":"Danny"}

while choice != '0':
    print(
        '''
    Who's Your Daddy?
		=================
 
		0 - Quit
		1 - Find out who's your dad
		2 - Add a daddy
		3 - Delete a dad

		=================

		''')


if choice == '0':
    print("Goodbye.")

elif choice == '1':
    print("\nHere are all of the kids.\n")
    for key in names:
        print(key)
        
