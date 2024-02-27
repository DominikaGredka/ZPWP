# Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
# dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
# zwróci. Zadanie należy wykonać w 2 wersjach:
# i. Wykorzystując pętle for .
# ii. Wykorzystując listę składaną.


liczby = [1, 4, 7, 70, 123]
def funkcja1(lista):
    ret = []
    for liczba in lista:
       ret.append(liczba*2)
    return ret

def funkcja2(lista):
    ret = [liczba*2 for liczba in lista]
    return ret


nowaLista1 = funkcja1(liczby)
nowaLista2 = funkcja2(liczby)
print(nowaLista1)
print(nowaLista2)