#creating a empty dictonary to store contacts detail , where contact name will be key

from pickle import TRUE


contacts={}
print(" Menu\n 1. Add contact \n 2. update contact \n 3. Delete contact \n 4. Give contact \n 5. Show contacts \n")
while TRUE:
    
    user_choice=int(input("Enter the respective values from menu \n"))
    if user_choice==1:
        name=input("Enter contact name\n")
        number=input("Enter respective contact number\n")
        contacts[name]=number
    elif user_choice==2:
        update_contact=input("Enter contact name to be updated \n")
        if update_contact in contacts:
            update_value=input("Enter  number\n")
            contacts[update_contact]=update_value
        else:
            print("No data found")
    elif user_choice==3:
        delete_contact=input("Enter contact name to be deleted\n")
        if delete_contact in contacts:
            confirm=input(f"To confirm deleting {delete_contact}`s contact press y \n")
            if confirm=='Y' or confirm =='y':
                contacts.pop(delete_contact)
            else:
                print("Action reverted")
        else:
            print("No data found")
    elif user_choice==4:
        contactTodisplay=input("Enter name to display contact\n")
        if contactTodisplay in contacts:
            print(contactTodisplay + " "+contacts[contactTodisplay])
        else:
            print("No data found")
    elif user_choice==5:
        if len(contacts)==0:
            print("No contacts found")
        else:

            for item in contacts:
                items=item
                print(item +"  =  "+ contacts[items])
    else:
        exit=input("if you want to perform more operation press y\n else press any key")
        if exit != 'y' or exit !='Y':
            break
        else:
            continue;
    

