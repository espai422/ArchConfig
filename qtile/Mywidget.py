import json
from typing import Any, List, Tuple
from urllib.error import URLError
from urllib.request import Request, urlopen

from libqtile.log_utils import logger
from libqtile.widget import base
import random
from threading import Thread


def Color_generator():
    lista = [252,0,0]
    suma = True
    resta = False

    for index in '102102':
        index = int(index)

        if suma:
            for i in range(42):
                lista[index] = lista[index] + 6
                color = f'#{f"0{hex(lista[0])[2:]}"[-2:]}{f"0{hex(lista[1])[2:]}"[-2:]}{f"0{hex(lista[2])[2:]}"[-2:]}'
                yield [color,color]

        else:
            for i in range(42):
                lista[index] = lista[index] - 6
                color = f'#{f"0{hex(lista[0])[2:]}"[-2:]}{f"0{hex(lista[1])[2:]}"[-2:]}{f"0{hex(lista[2])[2:]}"[-2:]}'
                yield [color,color]

        suma , resta = resta , suma

def text_generator():
    lista = ['','']
   # lista = ['','',]
    while True:
        for i in lista:
            yield [i,i[::-1]]


try:
    import xmltodict

    def xmlparse(body):
        return xmltodict.parse(body)
except ImportError:
    # TODO: we could implement a similar parser by hand, but i'm lazy, so let's
    # punt for now
    def xmlparse(body):
        raise Exception("no xmltodict library")



class Hack(base.ThreadPoolText):
    """A generic text widget that polls using poll function to get the text"""
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('func', None, 'Poll Function'),
        ('background',["#1e2127","#1e2127"],'fondo'),
        ('foreground',['#D4E6DA','#D4E6DA'],'lletra')
    ]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(Hack.defaults)
        self.generator = Color_generator()
        self.txt = text_generator()

    def poll(self):

        fg = next(self.generator)
        if fg == ['#fc0000', '#fc0000']:
            self.generator = Color_generator()
        text = next(self.txt)
        self.foreground = fg
        return f' {text[0]} espai422 {text[1]} '
        

