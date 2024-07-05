class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.isbn}, {"Available" if self.is_available else "Checked Out"})'
