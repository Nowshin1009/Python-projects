 
contact_Book= [

 {
    "name":"Taki",
    "phone":"01728437694",
    "email":"takiul47-375@diu.edu.bd"
},

 {
    "name":"Taifa",
    "phone":"01728437694",
    "email":"takiul47-375@diu.edu.bd"
},
 {
    "name":"Tara",
    "phone":"01728437694",
    "email":"takiul47-375@diu.edu.bd"
},
 {
    "name":"Tufa",
    "phone":"01728437694",
    "email":"takiul47-375@diu.edu.bd"
},

 {
    "name":"Afsana",
    "phone":"01728437694",
    "email":"takiul47-375@diu.edu.bd"
}
]

contact_Book = []

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
        print(f"{index+1}. {contact['name']} || {contact['phone']} || {contact["email"]} ")


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

print("=======WELCOME=========")
menu_text= """
Your options:
1. Create contact
2. View All contacts
3. Search a contact
4. Remove a contact
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
    else:
        print("Wrong choice!! Try again")

