from books import (
    add_book,
    view_all_books,
    search_book,
    search_books_by_author,
    remove_book,
    lend_book,
    return_book,
    view_lent_books,
    load_books
)

def main_menu():
    load_books()  # Load books at the start

    menu_text = """
    ----HELLO !!!-----
    ----WELCOME To our Library Management System------

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
