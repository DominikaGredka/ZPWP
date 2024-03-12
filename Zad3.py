# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"


def funkcja(liczba):
    return liczba % 2 == 0


czyParzysta = funkcja(4)

if czyParzysta:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
