## Text menu in Python
import GTFS

def print_menu():  ## Your menu design here
    gtfs = GTFS.GTFS()
    print (30 * "-", "MENU", 30 * "-")
    print ("1. Display line ")
    print ("2. Show Station ")
    print ("3. A* intinerary")
    print ("4. Menu Option 4")
    print ("5. Exit")
    print (67 * "-")


loop = True

while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = input("Enter your choice [1-5]: ")

    if choice == 1:
        print
        "Menu 1 has been selected"
        ## You can add your code or functions here
    elif choice == 2:
        print
        "Menu 2 has been selected"
        ## You can add your code or functions here
    elif choice == 3:
        print
        "Menu 3 has been selected"
        ## You can add your code or functions here
    elif choice == 4:
        print
        "Menu 4 has been selected"
        ## You can add your code or functions here
    elif choice == 5:
        print
        "Menu 5 has been selected"
        ## You can add your code or functions here
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")