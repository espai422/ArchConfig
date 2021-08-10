

contador = 0
def Color_generator():
    lista = [252,0,0]
    suma = True
    resta = False
    global contador
    for index in '102102':
        index = int(index)

        if suma:
            for i in range(42):
                lista[index] = lista[index] + 6
                color = f'#{f"0{hex(lista[0])[2:]}"[-2:]}{f"0{hex(lista[1])[2:]}"[-2:]}{f"0{hex(lista[2])[2:]}"[-2:]}'
                contador += 1
                yield [color,color]

        else:
            for i in range(42):
                lista[index] = lista[index] - 6
                color = f'#{f"0{hex(lista[0])[2:]}"[-2:]}{f"0{hex(lista[1])[2:]}"[-2:]}{f"0{hex(lista[2])[2:]}"[-2:]}'
                contador += 1
                yield [color,color]

        suma , resta = resta , suma


def text_generator():
    lista = [
    '----雷',
    '---雷',
    '--雷--',
    '-雷---',
    '雷----',]
    while True:
        for i in lista:
            yield [i,i[::-1]]




y = text_generator()
x = Color_generator()
from time import sleep
for i in y:
    print(i)
    sleep(0.01)
# x = 6
# y = f'0{hex(x)[2:]}'[-2:]
# print(y)
print(contador)