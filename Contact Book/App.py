 
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

contact_book = []

def create_contact():
    name = input("Enter name : ")
    phone =  input ("Enter phone no. :")
    email = input("Enter email : ")

    contact = {
        "name":name,
        "phone" : phone,
        "email":email
    }

    contact_book.append(contact)

    print("Contact created successfully!")

# create_contact()
# create_contact()

# print(contact_book)

def view_all_contacts():
    for contact in contact_Book:
        print(contact["name"],contact["phone"],contact["email"], sep=" | ",)
#view_all_contacts()

def search_contact():
    search_term = input("Enter what you want to search : ")
    for contact in contact_Book:
        if  search_term.lower() in contact["name"].lower():
            print(f"Found : {contact["name"]} - {contact["phone"]} - {contact["email"]}")

#search_contact()

def remove_contact():
        #search --> select  --> delete
        search_term = input("Enter text to search to remove : ")
        for index, contact in enumerate(contact_Book):
            if search_term.lower() in contact["name"].lower():
                print(f"{index+1}. {contact['name']} - {contact['phone']}")
        selected_index = input("Enter an contact to remove: ")
        selected_index= int(selected_index)

        contact_Book.pop(selected_index-1)
remove_contact()
view_all_contacts()
