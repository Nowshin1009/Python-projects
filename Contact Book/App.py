 
contact_Book= [

 {
    "name":"Taki",
    "phone":"01728437694",
    "email":"taki@diu.edu.bd"
},

 {
    "name":"Taifa",
    "phone":"01728437694",
    "email":"taifa@diu.edu.bd"
},
 {
    "name":"Tara",
    "phone":"01728437694",
    "email":"tara@diu.edu.bd"
},
 {
    "name":"Tufa",
    "phone":"01728437694",
    "email":"tufa@diu.edu.bd"
},

 {
    "name":"Afsana",
    "phone":"01728437694",
    "email":"afsana@diu.edu.bd"
}
]


def create_contact():
    name = input("Enter name : ")
    phone =  input ("Enter phone no. :")
    email = input("Enter email : ")

    contact = {
        "name":name,
        "phone" : phone,
        "email":email
    }

    contact_Book.append(contact)

    print("Contact created successfully!")

def view_all_contacts():
    for index, contact in enumerate(contact_Book):
        print(f"{index+1}. {contact['name']} || {contact['phone']} || {contact['email']} ")


def search_contact():
    search_term = input("Enter what you want to search : ")
    for contact in contact_Book:
        if  search_term.lower() in contact["name"].lower():
            print(f"Found : {contact["name"]} - {contact["phone"]} - {contact["email"]}")



def remove_contact():
        #search --> select  --> delete
        search_term = input("Enter text to search to remove : ")
        for index, contact in enumerate(contact_Book):
            if search_term.lower() in contact["name"].lower():
                print(f"{index+1}. {contact['name']} - {contact['phone']}")
        selected_index = input("Enter an contact to remove: ")
        selected_index= int(selected_index)

        contact_Book.pop(selected_index-1)
        print("Contact removed successfully!")


def update_contact():
    #select contact --> get new values --> replace with old value
    found_search_result=False
    search_term = input("Enter text to search to update : ")
    for index, contact in enumerate(contact_Book):
        if search_term.lower() in contact["name"].lower():
            found_search_result=True
            print(f"{index+1}. {contact['name']} - {contact['phone']}")

        if not found_search_result:
            print("No such contact")
            return
    selected_index = input("Enter an contact to update: ")
    selected_index= int(selected_index)
    
    new_name=input("Enter new name: ")
    new_phone=input("Enter new phone number: ")
    new_email=input("Enter new email: ")

    # sequentially -->
    # contact_Book[selected_index - 1]["name"]=new_name
    # contact_Book[selected_index - 1]["phone"]=new_phone
    # contact_Book[selected_index - 1]["email"]=new_email


    # with mathod -->
    contact_Book[selected_index-1].update(
        {
            "name":new_name,
            "phone":new_phone,
            "email":new_email
        }
    )
    print("Contact updated successfully!!!")


    


print("=======WELCOME=========")
menu_text= """
Your options:
1. Create contact
2. View All contacts
3. Search a contact
4. Remove a contact
5. Update a contact
0. Exit
"""

while True:


    print(menu_text)
    print("Enter your choice : ")
    choice = input()

    if choice == "1":
        create_contact()
    elif choice == "2":
        view_all_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        remove_contact()
    elif choice == "5":
        update_contact()
    elif choice == "0":
        break
    else:
        print("Wrong choice!! Try again")

