# Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
# metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
# ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
# stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
# zwracała true , a dla drugiego false .

from statistics import mean


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return mean(self.marks) > 50


student1 = Student("Jan", [50, 51, 52])
student2 = Student("Tomasz", [29, 45, 60])

print(student2.is_passed())
print(student1.is_passed())
