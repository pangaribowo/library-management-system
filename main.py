from librarian import Librarian
from library import Library

def main():
    library = Library("City Library")
    librarian = Librarian("Alice")

    # Add books to the library
    librarian.add_book(library, "1984", "George Orwell", "1234567890")
    librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee", "2345678901")

    # Register members
    librarian.register_member(library, "John Doe", "M001")
    librarian.register_member(library, "Jane Smith", "M002")

    # Display available books
    print("Available books:")
    for book in library.list_available_books():
        print(book)

    # Members borrow books
    member_john = library.find_member_by_id("M001")
    member_jane = library.find_member_by_id("M002")
    book_1984 = library.find_book_by_isbn("1234567890")

    member_john.borrow_book(book_1984)

    # Display borrowed books
    print("\nBorrowed books:")
    for book in library.list_borrowed_books():
        print(book)

    # Member returns book
    member_john.return_book(book_1984)

    # Display available books after return
    print("\nAvailable books after return:")
    for book in library.list_available_books():
        print(book)

if __name__ == '__main__':
    main()
