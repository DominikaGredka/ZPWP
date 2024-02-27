# Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie
# go wyświetlić ( print
#


def funkcja(name, surmane):
    msg = f"Ceść, {name} {surmane}!"
    return msg

wiadomosc = funkcja("Jan", "Nowak")
print(wiadomosc)