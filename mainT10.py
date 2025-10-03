
shoppingListTitle = ""
shoppingList_items = ""

menu_hline = "-"*20

while len(shoppingListTitle) < 1:
    shoppingListTitle = input("Enter the title: ")
    if len(shoppingListTitle) < 1:
        print("ERROR: Empty titles not allowed. Please, try again.")
    


def main():
    menu_choice = "0"

    while menu_choice != "3":

        menu_choice = input("\n1. Add an item\n2. Print currently added items\n3. Finished\n\nEnter your choice: ")
        if menu_choice == "1":
            added_item = input("Enter an item: ")
            items(added_item)
        elif menu_choice == "2":
            print(f'Currently added items:\n{shoppingList_items}')
        elif menu_choice == "3":
            shoppingList()
            exit()
        else:
            print("Error: Invalid choice, please try again.")

def shoppingList():
    print(f'\n{menu_hline}\n{shoppingListTitle:^20}\n{menu_hline}\n{shoppingList_items}')

def items(list_item):
    global shoppingList_items
    shoppingList_items +=  list_item + "\n"
    
main()
