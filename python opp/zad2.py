import Zad1 as zad1


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka informacje: "
            f"miasto {self.city}, "
            f"ul.{self.street}, "
            f"kod pocztowy {self.zip_code}, "
            f"godziny otwarcia {self.open_hours}, "
            f"telfon {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik: {self.first_name} {self.last_name}, "
            f"data urodzenia{self.birth_date}, "
            f"adres: ul.{self.street}, {self.zip_code} {self.city},"
            f"telefon {self.phone}"
        )


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
        return (
            f"Książka: "
            f"biblioteka: {self.library.city}, ul.{self.library.street},"
            f"autor: {self.author_name} {self.author_surname},"
            f"liczba stron: {self.number_of_pages},"
            f"data publikacji: {self.publication_date}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f" - {book}" for book in self.books])
        return (
            f"Pracownik: {self.employee.first_name}, "
            f"student: {self.student.name}, "
            f"lista książek: {book_list}, "
            f"data zamówienia: {self.order_date}"
        )


library1 = Library("Katowice", "Dębowa 5", "40-230", "9:00 - 20:00", "32 257 73 48")
library2 = Library(
    "Warszawa", "Piotrkowska 30", "73-948", "10:00 - 22:00", "22 158 15 18"
)

book1 = Book(library1, "13.02.1999", "Jan", "Nowak", 359)
book2 = Book(library2, "29.02.2000", "Janusz", "Polak", 2137)
book3 = Book(library1, "28.10.2006", "Anna", "Wącław", 246)
book4 = Book(library2, "18.11.2015", "Klaudia", "Olszówka", 124)
book5 = Book(library1, "16.08.2023", "Roman", "Polański", 187)

employee1 = Employee(
    "Jan",
    "Wolny",
    "15.03.2020",
    "18,06,2003",
    "Katowice",
    "Graniczna 5",
    "40-562",
    "521789318",
)
employee2 = Employee(
    "Jane",
    "Smith",
    "2022-02-01",
    "1985-08-20",
    "Wrocław",
    "Pocztowa 66",
    "56-655",
    "532168439",
)
employee3 = Employee(
    "Bob",
    "Johnson",
    "2022-03-01",
    "1995-11-10",
    "Warszawa",
    "Leśna 33",
    "61-854",
    "596172943",
)

student1 = zad1.Student("Jan", [50, 51, 52])
student2 = zad1.Student("Tomasz", [78])
student3 = zad1.Student("Ania", [50, 95])

order1 = Order(employee1, student2, [book2, book1, book4], "05.03.2024")
order2 = Order(employee3, student1, [book2, book3], "13.02.2024")

print(order1)
print(order2)
