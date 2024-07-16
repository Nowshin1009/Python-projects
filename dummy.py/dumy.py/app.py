book_list = []

def add_book():
    title = input("Enter book title: ")
    authors = input("Enter authors name : ").split(',')
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    book = {
    "title": title,
    "authors": authors,
    "isbn": isbn,
    "year": year,
    "price": price,
    "quantity": quantity,
    "lent_to": None
    } 

    book_list.append(book)
    save_books(book_list)
    print("Book added successfully!!!") 

def view_all_books():
    for index, book in enumerate(book_list):
        authors = ", ".join(book["authors"])
        if book["lent_to"]:
            lent_to = book["lent_to"]
        else:
            lent_to = "Available"
        
        print(f"{index + 1}. Title: {book['title']}, Authors: {authors}, ISBN: {book['isbn']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}, Lent to: {lent_to}")

def print_book(book):
    authors = ", ".join(book["authors"])
    lent_to = book["lent_to"] if book["lent_to"] else "Available"
    print(f"Title: {book['title']}, Authors: {authors}, ISBN: {book['isbn']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}, Lent to: {lent_to}")

def search_book():
    search_term = input("Enter title or ISBN to search : ").lower()
    for book in book_list:
        if search_term in book["title"].lower() or search_term in book["isbn"].lower():
            print_book(book)

def search_books_by_author():
    search_term = input("Enter author name to search: ").lower()
    for book in book_list:
        if any(search_term in author.lower() for author in book["authors"]):
            print_book(book)

def remove_book():
    search_term = input("Enter title or ISBN to search for removal: ").lower()
    for index, book in enumerate(book_list):
        if search_term in book["title"].lower() or search_term in book["isbn"].lower():
            print(f"{index + 1}. {book['title']}")
    selected_index = int(input("Enter the number of the book to remove: ")) - 1

    if 0 <= selected_index < len(book_list):
        removed_book = book_list.pop(selected_index)
        save_books(book_list)
        print(f"Removed book: {removed_book['title']}")
    else:
        print("Invalid selection.")

def lend_book(): 
    search_term = input("Enter title or ISBN to search for lending: ").lower()
    for index, book in enumerate(book_list):
        if search_term in book["title"].lower() or search_term in book["isbn"].lower():
            print(f"{index + 1}. {book['title']}")
    selected_index = int(input("Enter the number of the book to lend: ")) - 1

    if 0 <= selected_index < len(book_list):
        if book_list[selected_index]["quantity"] > 0:
            borrower = input("Enter the name of the borrower: ")
            book_list[selected_index]["quantity"] -= 1
            book_list[selected_index]["lent_to"] = borrower
            save_books(book_list)
            print(f"Book lent to {borrower}.")
        else:
            print("Not enough books available to lend.")
    else:
        print("Invalid selection.")

def return_book():
    search_term = input("Enter title or ISBN to search for return: ").lower()
    for index, book in enumerate(book_list):
        if search_term in book["title"].lower() or search_term in book["isbn"].lower():
            print(f"{index + 1}. {book['title']}")
    selected_index = int(input("Enter the number of the book to return: ")) - 1

    if 0 <= selected_index < len(book_list):
        book_list[selected_index]["quantity"] += 1
        book_list[selected_index]["lent_to"] = None
        save_books(book_list)
        print("Book returned successfully.")
    else:
        print("Invalid selection.")

def view_lent_books():
    for book in book_list:
        if book["lent_to"]:
            print_book(book)


def save_books(book_list):
    with open('books.csv', 'wt') as fp:
        for book in book_list:
            line = f"{book['title']},{book['authors']},{book['isbn']},{book['quantity']},{book['year']},{book['lent_to']}\n"
            fp.write(line)

def load_books():
    if os.path.exists('books.csv'):
        with open('books.csv', 'rt') as fp:
            for line in fp:
                title, authors, isbn, quantity, year, lent_to = line.strip().split(',')
                book = {
                    "title": title,
                    "authors": authors.split(','),
                    "isbn": isbn,
                    "year": year,
                    "price": float('0.0'), # Assuming price is not saved, you can modify this as needed
                    "quantity": int(quantity),
                    "lent_to": lent_to if lent_to != 'None' else None
                }
                book_list.append(book)     

def main_menu():
    menu_text = """
    ----HELLO !!!-----
    ----WELCOME To our Library management system------

    Your options:
    1. Add a book
    2. View all books
    3. Search for books by title or ISBN
    4. Search for books by authors
    5. Remove a book
    6. Lend a book
    7. Return a book
    8. View all lent books
    0. Exit
    """
    
    while True:
        print(menu_text)
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            search_books_by_author()
        elif choice == "5":
            remove_book()
        elif choice == "6":
            lend_book()
        elif choice == "7":
            return_book()
        elif choice == "8":
            view_lent_books()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()