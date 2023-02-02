import sys, time


#Need to implement loading existing list into list - Possible methods CSV? 

#list to hold items
shopping_list = []

#Instructions
inp = input("\nWelcome to the shopping list application!\nWhile using this app you can either add items to a list or view your current shopping list. When adding items type 'END' to stop adding items.\nWould you like to add items to the list? (y/n): ")


if inp == 'y':
    while True:
        new_item = input("- ")
        if new_item == 'END':
            print("Thank you for using the shopping list application! Here are the items you added to your shopping list:\n")
            print(shopping_list)
            break
        shopping_list.append(new_item)

elif inp == 'n':
    ans = input("Would you like to view the current list? (y/n): ")
    if ans == 'y':
        print(shopping_list)
    else:
        print("Thank you for using the shopping list app!\n")
        
