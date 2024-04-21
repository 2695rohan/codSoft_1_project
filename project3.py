'''contact book:
1. Add new contact
2. Search contact
3. Display contact
4. Edit contact
5. Delete contact
6. Exit
Enter your choice '''

contact = {}

def display_contact():
    print("Name \t\t Contact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice = (input(" 1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete contact \n 6. Exit \n Enter your choice: "))

    if choice == "1":
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
    elif choice == "2":  
        search_name = input("Enter the contact name: ") 
        if search_name in contact:
            print(search_name, "'s contact number is", contact[search_name])
        else:
            print("Name is not found in contact book!")
    elif choice == "3":
        if not contact:
            print("Empty contact book")
        else:
            display_contact()    
    elif choice == "4":
        edit_contact = input("Enter the contact to be edited: ")
        if edit_contact in contact:
            phone = input("Enter mobile number: ")
            contact[edit_contact] = phone
            print("***Contact Sucessfully Updated***")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choice == "5":
        del_contact = input("Enter the contact name to be deleted: ") 
        if del_contact in contact:
            confirm = input("Do you want to deleted this contact y/n? :")
            if confirm == 'y' or confirm =='Y':
                contact.pop(del_contact)    
                print("***Contact Deleted Sucessfully***")
            display_contact()
        else:
            print("Name is not found in contact book!")
    else:
        break
    
