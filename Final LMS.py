class Books:
    def __init__(self, title, author, subject):
        self.title = title
        self.author = author
        self.subject = subject


class Library:
    def __init__(self):
        self.books = []  # Use the instance variable 'books' instead of 'book'

    def add_book(self, title, author, subject):
        book = Books(title, author, subject)  # Create an instance of 'Books'
        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self, book):
        for b in self.books:
            if b:
                if b.title == book:
                    self.books.remove(b)
                    print("Book removed successfully!")
                    print(f"Title: {b.title} \n Author: {b.author} \n Subject: {b.subject}")
            else:
                print("Book not found in the library.")

    def search_book(self,tit):
        for b in self.books:
            if b:
                if b.title == tit:
                    print("Book found in the library.")
                    print(f"Title: {b.title}")  
                    print(f"author: {b.author}")
                    print(f"subject: {b.subject}")
            else:
                print("Book not found in the library.")

    def modify_book(self, old_book, new_book):
        for b in self.books:
            if b:
                if b.title == old_book:
                    b.title = new_book
                    print("Book modified successfully!")
            else:
                print("Book not found in the library.")

    def display_books(self):
        if self.books:
            print("Books available in the library:")
            for b in self.books:
                print("")
                print(f"Title: {b.title}")  
                print(f"author: {b.author}")
                print(f"subject: {b.subject}")
                print("*"*10)
        else:
            print("No books in the library.")


def display_menu():
    print("Library Management System")
    print("1:- Add Book")
    print("2:- Remove Book")
    print("3:- Search Book")
    print("4:- Modify Book")
    print("5:- Display Books")
    print("6:- Exit")


def save_library(library):
    with open("library.csv", "w") as file:  # Use 'w' mode to overwrite the file
        for book in library.books:
            file.write(f"{book.title},{book.author},{book.subject}\n")  # Save book title, author, and subject


def load_library():
    library = Library()
    try:
        with open("library.csv", "r") as file:
            for line in file:
                book_info = line.strip().split(",")  # Split the line into title, author, and subject
                if len(book_info) == 3:
                    title, author, subject = book_info
                    library.add_book(title, author, subject)  # Use 'add_book' to add the loaded book properly
    except FileNotFoundError:
        pass
    return library
librarian_USERNAME= "namal"
librarian_PASSWORD = "123"



def get_user_type():
    print("Login as:")
    print("1:- Librarain")
    print("2:- Student")
    print("3:- Close Program")
    choice = input("Enter your choice (1 to 3): ")

    if choice == '1':
        return "librarian"
    elif choice == '2':
        return "Student"
    elif choice == '3':
        return "exit"
    else:
        print("Invalid choice! Please enter 1 to 3.")
        return None

def librarian_login():
    print("librarian Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == librarian_USERNAME and password ==librarian_PASSWORD:
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

def Student_login():
    print("Student Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "guest" and password=="123":
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False



def main():
    library = load_library()
    print("*"*80)
    print("             Welcome to Namal Library Management System")
    print("*"*80)
    
    while True:
        user_type = get_user_type()

        if user_type == "exit":
            print("Exiting the program... ")
            print("Thank You for visiting Namal Library! ")
            break

        elif user_type == "librarian":
            if librarian_login():
                while True:
                    display_menu()
                    choice = input("Enter your choice (1-6): ")

                    if choice == '1':
                        book = input("Enter the book name: ")
                        book2 = input("Enter the book author: ")
                        book3 = input("Enter the book subject: ")
                        library.add_book(book, book2, book3)
                        save_library(library)

                    elif choice == '2':
                        book = input("Enter the book name: ")
                        library.remove_book(book)
                        save_library(library)

                    elif choice == '3':
                        tit = input("Enter the book name: ")
                        library.search_book(tit)
                        save_library(library)

                    elif choice == '4':
                        book = input("Enter the book name to be modified: ")
                        new_book = input("Enter the new book name: ")
                        library.modify_book(book, new_book)
                        save_library(library)

                    elif choice == '5':
                        library.display_books()

                    elif choice == '6':
                        print("Logging out as Librarian")
                        break

                    else:
                        print("Invalid choice! Please enter a number from 1 to 6.")

        elif user_type == "Student":
            while True:
                print("1. Search Book")
                print("2. Display Book")
                print("3. Exit")
                choice = input("Enter your choice (1-3): ")

                if choice == '1':
                    book = input("Enter the book name: ")
                    library.search_book(book)
                    save_library(library)

                elif choice == '2':
                    library.display_books()

                elif choice == '3':
                    print("Logging out as Student")
                    break

                else:
                    print("Invalid choice! Please enter a number from 1 to 3.")

        else:
            print("Invalid user type. Please try again.")

if __name__ == "__main__":
    main()
