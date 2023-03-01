import sys, time


#Need to implement loading existing list into list - Possible methods CSV? 

#list to hold items
shopping_list = []

#list holding special food items
special_list = ['Hershey bar', 'Muffin', 'Cupcake', 'Croissant', 'Pudding', 'Toblerone', 'Snickers', 'Caramel Apple', 'Popcorn', 'Cookies']

#Instructions
inp = input("\nWelcome to the shopping list application!\nWhile using this app you can either add items to a list or view your current shopping list. When adding items type 'END' to stop adding items.\nWould you like to add items to the list? (y/n): ")


if inp == 'y':
    while True:
        new_item = input("- ")
        if new_item == 'END':
            print("Thank you for using the shopping list application! Here are the items you added to your shopping list:\n")
            for item in shopping_list:
                print(item)
            ans1 = input("\nWould you like to roll for a random sweet to add to your shopping list? (y/n): ")
            if ans1 == 'y':
                f = open("treat.txt", 'w')
                f.write(1)
                f.close()
            else:
                ans = input("\nWould you like to view the current list? (y/n): ")
                 if ans == 'y':
                    for item in shopping_list:
                        print(item)
            break
        shopping_list.append(new_item)

elif inp == 'n':
    ans = input("Would you like to view the current list? (y/n): ")
    if ans == 'y':
        for item in shopping_list:
            print(item)
    else:
        print("Thank you for using the shopping list app!\n")
        
