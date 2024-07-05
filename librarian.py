from book import Book
from member import Member

class Librarian:
    def __init__(self, name):
        self.name = name

    def add_book(self, library, title, author, isbn):
        new_book = Book(title, author, isbn)
        library.books.append(new_book)

    def register_member(self, library, name, member_id):
        new_member = Member(name, member_id)
        library.members.append(new_member)

    def __repr__(self):
        return f'Librarian({self.name})'
