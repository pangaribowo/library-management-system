# Library Management System

This is a simple Library Management System implemented in Python using Object-Oriented Programming (OOP) principles. The application manages book inventory, member registrations, book lending, and returns.

## Project Structure

```
library_management_system/
├── book.py
├── member.py
├── librarian.py
├── library.py
├── main.py
└── README.md
```

## Classes

1. **Book**
   - Represents a book in the library.
   - Attributes: `title`, `author`, `isbn`, `is_available`

2. **Member**
   - Represents a member of the library.
   - Attributes: `name`, `member_id`, `borrowed_books`
   - Methods: `borrow_book(book)`, `return_book(book)`

3. **Librarian**
   - Represents a librarian managing the library.
   - Attributes: `name`
   - Methods: `add_book(library, title, author, isbn)`, `register_member(library, name, member_id)`

4. **Library**
   - Represents the library containing books and members.
   - Attributes: `name`, `books`, `members`
   - Methods: `list_available_books()`, `list_borrowed_books()`, `find_book_by_isbn(isbn)`, `find_member_by_id(member_id)`

## Usage

1. Clone the repository.

```sh
git clone https://github.com/yourusername/library_management_system.git
cd library_management_system
```

2. Run the `main.py` script.

```
python main.py
```

This will simulate the management of a library, including adding books, registering members, borrowing and returning books, and displaying available and borrowed books.

##Output

```
Available books:
Book(1984, George Orwell, 1234567890, Available)
Book(To Kill a Mockingbird, Harper Lee, 2345678901, Available)

Borrowed books:
Book(1984, George Orwell, 1234567890, Checked Out)

Available books after return:
Book(1984, George Orwell, 1234567890, Available)
Book(To Kill a Mockingbird, Harper Lee, 2345678901, Available)
```

## Future Improvements

- Implement a graphical user interface (GUI) for better user interaction.
- Add persistent storage (e.g., database) for books and members.
- Enhance the system with additional features like search functionality, book reservations, and overdue notifications.