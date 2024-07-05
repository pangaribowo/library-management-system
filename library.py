class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def list_available_books(self):
        return [book for book in self.books if book.is_available]

    def list_borrowed_books(self):
        return [book for book in self.books if not book.is_available]

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def __repr__(self):
        return f'Library({self.name}, Books: {len(self.books)}, Members: {len(self.members)})'
