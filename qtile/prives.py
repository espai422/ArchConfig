

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




# import subprocess
# sp = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE)

# output, _ = sp.communicate()
# output = output.split('')
# print (output)

import psutil
class Interfaces():

    def get_data(self):
        data = psutil.net_if_addrs()
        return data
    
    def get_interfaces(self):
        data = self.get_data()
        return [interface for interface in data]

    def get_interfaces_info(self):
        data = self.get_data()
        interfaces = self.get_interfaces()

        for interface in interfaces:
            
            iface_info = data[interface][0][1]

            if '.' in iface_info and iface_info != '127.0.0.1':

                return iface_info

x = Interfaces()

print(x.get_interfaces_info())