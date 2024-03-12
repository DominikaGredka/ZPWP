# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.


def funkcja(lista1, lista2):
    nowaLista = list(set(lista1 + lista2))
    wynik = [x**3 for x in nowaLista]
    return wynik


pl = [1, 2, 4]
dl = [2, 5, 10]

print(funkcja(pl, dl))
