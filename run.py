#!/usr/bin/python
# -*- coding: utf8 -*-
from matrix import Matrix
import os


def main():
    m = Matrix()
    menu = {'I': m.new, 'C': m.clear, 'L': m.pixel_color,
            'V': m.column_color, 'H': m.row_color, 'K': m.retangle,
            'F': m.region_color, 'S': m.save}
    os.system("clear")
    print "Editor gráfico"
    while True:
        option = raw_input("Comando: ")
        c = option.replace(' ', '')
        if c[0].upper() in menu.keys():
            menu[c[0].upper()](c[1::])
        elif c[0].upper() == 'X':
            print c[0].upper()
            exit()
        else:
            print "Opção inválida!"

if __name__ == "__main__":
    main()
