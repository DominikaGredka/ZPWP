# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
# drugi element.

liczby = list(range(1, 11))

def funkcja(lista):
    for index in range(0, len(lista), 2):
        print(lista[index])

funkcja(liczby)