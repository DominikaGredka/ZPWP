# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
# typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.

def funkcja(lista, a):
    return lista[0] == a
lista = [2, 4, 6, 8 ]
print(funkcja(lista, 3))