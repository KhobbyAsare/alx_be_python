class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # This should be an instance variable

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

    # Dunder Methods ..................

    # def __str__(self):
    #     return f"{self.title} {self.author} {self._is_checked_out}"
    #
    # def __repr__(self):
    #     return f"Title = {self.title}, Author = {self.author}, checked_out_state = {self._is_checked_out}"

class Library:
    def __init__(self):
        self._books = []  # This should be an instance variable

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"Title: {book.title}, Author: {book.author}")



# Example usage:
# library = Library()
# library.add_book(Book("1984", "George Orwell"))
# library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
#
# print(library)

#
# print("Available Books:")
# library.list_available_books()
#
# library.check_out_book("1984")
# print("\nAvailable Books after checking out '1984':")
# library.list_available_books()
#
# library.return_book("1984")
# print("\nAvailable Books after returning '1984':")
# library.list_available_books()
