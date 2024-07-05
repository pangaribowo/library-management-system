class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
        else:
            print(f'The book "{book.title}" is currently unavailable.')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
        else:
            print(f'The book "{book.title}" is not borrowed by {self.name}.')

    def __repr__(self):
        return f'Member({self.name}, {self.member_id}, Borrowed Books: {[book.title for book in self.borrowed_books]})'
