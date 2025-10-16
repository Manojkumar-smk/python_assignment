library = []

def show_menu():
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

def Add_book():
    book_title = input("Enter Book Name: ")
    author_name = input("Enter Author Name: ")
    library.append({"Book": book_title, "Author": author_name})
    print("Book added successfully!")

def View_Books():
    print("\nBooks in Library:")
    print("-" * 30)
    if not library:
        print("No books available.")
    else:
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book['Book']} by {book['Author']}")

def Search_book():
    title = input("Enter book title to search: ")
    found = False
    for book in library:
        if book["Book"].lower() == title.lower():
            print(f"Found: {book['Book']} by {book['Author']}")
            found = True
            break
    if not found:
        print("Book not found in library.")

# Main loop
while True:
    show_menu()
    try:
        Op_num = int(input("Enter your choice: "))
        if Op_num == 1:
            Add_book()
        elif Op_num == 2:
            View_Books()
        elif Op_num == 3:
            Search_book()
        elif Op_num == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Please enter a valid number.")