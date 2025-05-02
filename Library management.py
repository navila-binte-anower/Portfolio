class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' borrowed successfully.")
        else:
            print(f"Book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' returned successfully.")
        else:
            print(f"Book '{self.__title}' is not borrowed.")

    def view_book_info(self):
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {'Available' if self.__availability else 'Borrowed'}")

    def get_book_id(self):
        return self.__book_id

    def get_availability(self):
        return self.__availability

book1 = Book(101, "Python Programming", "John Doe")
book2 = Book(102, "Data Science Essentials", "Jane Smith")
book3 = Book(103, "Machine Learning", "Alan Turing")
book4 = Book(104, "Artificial Intelligence", "Marvin Minsky")
book5 = Book(105, "Deep Learning", "Yann LeCun")
book6 = Book(106, "Natural Language Processing", "Christopher Manning")
book7 = Book(107, "Statistics for Data Science", "David C. Hsu")
book8 = Book(108, "Python for Data Analysis", "Wes McKinney")

def view_all_books():
    print("Library Books:")
    for book in Library.book_list:
        book.view_book_info()

def borrow_book():
    try:
        book_id = int(input("Enter book ID to borrow: "))
        found_book = None
        for book in Library.book_list:
            if book.get_book_id() == book_id:
                found_book = book
                break

        if found_book:
            if found_book.get_availability():
                found_book.borrow_book()
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid book ID.")
    except:
        print("Invalid input. Please enter a number.")

def return_book():
    try:
        book_id = int(input("Enter book ID to return: "))
        found_book = None
        for book in Library.book_list:
            if book.get_book_id() == book_id:
                found_book = book
                break
        if found_book:
            if not found_book.get_availability():
                found_book.return_book()
            else:
                print("Book is not borrowed.")
        else:
            print("Invalid book ID.")
    except:
        print("Invalid input. Please enter a number.")

print("-----Welcome to the Library-----")
while True:
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all_books()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")