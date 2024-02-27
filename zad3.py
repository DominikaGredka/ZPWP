# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
# jedynie parzyste elementy.

liczby = [1, 5, 16, 81, 966, 120, 152, 52, 634, 9]

def funkcja(lista):
    for liczba in lista:
        if liczba%2 == 0:
            print(liczba)

funkcja(liczby)