book_list = []

def add_book():
    title = input("Enter book title: ")
    authors = input("Enter authors name: ").split(',')
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
        lent_to = book["lent_to"] if book["lent_to"] else "Available"
        print(f"{index + 1}. Title: {book['title']}, Authors: {authors}, ISBN: {book['isbn']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}, Lent to: {lent_to}")

def print_book(book):
    authors = ", ".join(book["authors"])
    lent_to = book["lent_to"] if book["lent_to"] else "Available"
    print(f"Title: {book['title']}, Authors: {authors}, ISBN: {book['isbn']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}, Lent to: {lent_to}")

def search_book():
    search_term = input("Enter title or ISBN to search: ").lower()
    found = False
    for book in book_list:
        if search_term in book["title"].lower() or search_term in book["isbn"].lower():
            print_book(book)
            found = True
    if not found:
        print("No matching books found.")

def search_books_by_author():
    search_term = input("Enter author name to search: ").lower()
    found = False
    for book in book_list:
        if any(search_term in author.lower() for author in book["authors"]):
            print_book(book)
            found = True
    if not found:
        print("No matching books found.")

def remove_book():
    search_term = input("Enter title or ISBN to search for removal: ").lower()
    found = False
    for index, book in enumerate(book_list):
        if search_term in book["title"].lower() or search_term in book["isbn"].lower():
            print(f"{index + 1}. {book['title']}")
            found = True
    if not found:
        print("No matching books found.")
        return

    selected_index = int(input("Enter the number of the book to remove: ")) - 1
    if 0 <= selected_index < len(book_list):
        removed_book = book_list.pop(selected_index)
        save_books(book_list)
        print(f"Removed book: {removed_book['title']}")
    else:
        print("Invalid selection.")

def lend_book(): 
    search_term = input("Enter title or ISBN to search for lending: ").lower()
    found = False
    for index, book in enumerate(book_list):
        if search_term in book["title"].lower() or search_term in book["isbn"].lower():
            print(f"{index + 1}. {book['title']}")
            found = True
    if not found:
        print("No matching books found.")
        return

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
    found = False
    for index, book in enumerate(book_list):
        if search_term in book["title"].lower() or search_term in book["isbn"].lower():
            print(f"{index + 1}. {book['title']}")
            found = True
    if not found:
        print("No matching books found.")
        return

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
    print("Books saved successfully.")

def load_books():
    try:
        with open('books.csv', 'r') as fp:
            for line in fp.readlines():
                title, authors, isbn, quantity, year, lent_to = line.strip().split(',')
                book = {
                    "title": title,
                    "authors": authors.split(','),
                    "isbn": isbn,
                    "year": year,
                    "price": float('0.0'), 
                    "quantity": int(quantity),
                    "lent_to": lent_to if lent_to != 'None' else None
                }
                book_list.append(book)
    
    except FileNotFoundError:
        print("No existing book records found. Starting fresh.")
