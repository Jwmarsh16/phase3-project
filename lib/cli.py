class Cli:
    def start(self):
        print("Welcome to the Book Library Management System!")
        print("")
        self.menu()

    def menu(self):
        print("Choose an option:")
        print("1. Add a new author")
        print("2. Add a new book")
        print("3. Display all authors")
        print("4. Display all books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.add_author()
        elif choice == "2":
            self.add_book()
        elif choice == "3":
            self.display_authors()
        elif choice == "4":
            self.display_books()
        elif choice == "5":
            print("Thank you for using the Book Library Management System!")
            CONN.close()
        else:
            print("Invalid choice. Please try again.")
            self.menu()