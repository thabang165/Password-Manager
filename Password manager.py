
import json
print("Welcome to Password Manager!")
def password_manager():
    library = []
    while True:             
        print("1. Add a new password ")
        print("2. Retrieve a password ")
        print("3. Delete a password ")
        print("4. Exit")
        try:
            option = int(input("Choose an option: "))

            if option == 1:
                website = input("Enter the name of the website or app: ").lower()
                password = input("Enter the password: ")
                libr_input = {
                    website : password
                }
                library.append(libr_input)
                
                jsonfile = open("passwords.json" , "w")
                json.dump(library, jsonfile)
                jsonfile.close()
            elif option == 2:
                passwords_json = open("passwords.json")
                library_of_passwords = json.load(passwords_json)
                passwords_json.close()
                for keys in library_of_passwords:
                    print(keys)
            elif option == 3:  
                passwords_to_delete = open("passwords.json")
                library_of_passwords_to_delete = json.load(passwords_to_delete)
                user_password_to_remove = input("Write the name of the website or app which it's password you want to remove: ").lower()
                for key in library_of_passwords_to_delete: 
                    if user_password_to_remove in key:
                        del key[user_password_to_remove]
                        print("Password for", user_password_to_remove , "has been successfully removed")
                    else:
                        print("Invalid entry. The name of the website or app entered is not saved in passwords directory")
                json.dump(library_of_passwords_to_delete, open("passwords.json", "w"))
                
            elif option == 4:
                print("Thank you for using Password Manager. Goodbye")
                break
            else:
                print("Please enter a number between 1 to 4")
        except:
            print("Please enter a number corresponding with an action you want to take")
        
password_manager()