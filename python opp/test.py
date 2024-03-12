class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\nOpen Hours: {self.open_hours}\nPhone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nHire Date: {self.hire_date}\nBirth Date: {self.birth_date}\nLocation: {self.city}, {self.street}"


class Book:
    def __init__(
        self, library, publication_date, author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublished: {self.publication_date}\nPages: {self.number_of_pages}\n{self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f" - {book}" for book in self.books])
        return f"Order by {self.employee.first_name} {self.employee.last_name} for {self.student}\nOrder Date: {self.order_date}\nBooks:\n{book_list}"


# Tworzenie instancji klas
library1 = Library("City1", "Street1", "12345", "9 AM - 5 PM", "123-456-7890")
library2 = Library("City2", "Street2", "54321", "10 AM - 6 PM", "987-654-3210")

employee1 = Employee("John", "Doe", "2022-01-01", "1990-05-15", "City1", "Street1")
employee2 = Employee("Jane", "Smith", "2022-02-01", "1985-08-20", "City2", "Street2")
employee3 = Employee("Bob", "Johnson", "2022-03-01", "1995-11-10", "City1", "Street1")

book1 = Book(library1, "2021-05-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2020-10-15", "Author2", "Surname2", 300)
book3 = Book(library2, "2019-07-20", "Author3", "Surname3", 150)
book4 = Book(library2, "2022-02-28", "Author4", "Surname4", 250)
book5 = Book(library1, "2023-01-10", "Author5", "Surname5", 180)

order1 = Order(employee1, "Student1", [book1, book2, book3], "2024-03-05")
order2 = Order(employee2, "Student2", [book4, book5], "2024-03-06")

# Wyświetlanie zamówień
print(order1)
print("\n==============================\n")
print(order2)
