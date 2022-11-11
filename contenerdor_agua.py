""" 
    Enunciado: 
Dado un array de números enteros positivos, donde cada uno
representa unidades de bloques apilados, debemos calcular cuantas unidades
de agua quedarán atrapadas entre ellos.

Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
           ⏹
           ⏹
    ⏹💧💧 ⏹
    ⏹💧⏹⏹💧⏹
    ⏹💧⏹⏹💧⏹
    ⏹💧⏹⏹⏹⏹

Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
de agua. Suponemos que existe un suelo impermeable en la parte inferior
que retiene el agua.
"""

import os

def water_counter(list):

    max_blocks = list[0]
    container = []
    container_list = []
    water = 0

    for i in list:

        if len(list) < 3 or i < 0 or isinstance(i, int) == False:
            print("\n[!] Deben haber más de dos números enteros y positivos\n")
            os._exit(1)
        elif list[-1] == 0:
            list.pop(-1)
        elif i == 0 and max_blocks == 0:
            continue
        elif max_blocks == 0 and i != 0:
            max_blocks = i

        if i <= max_blocks:
            container.append(i)
        else:
            max_blocks = i
            container.append(i)
            container.sort(reverse=True)
            container_list.append(container)
            container = []
            container.append(i)

    container.sort(reverse=True)
    container_list.append(container)

    for container in container_list:
        for i in container:
            if container[1] - i >= 0:
                water += container[1] - i

    print(f"\n[+] Hay {water} unidades de agua\n")


number_list1 = [4, 0, 3, 6, 1, 3]
number_list2 = [9, 0, 1, 12, 0, 8]
number_list3 = [10, 0, 0, 0, 0, 10]
number_list4 = [4, 0, 3, 6, 1, 3]
number_list5 = [4, 0, 3, 6, 1, 3]

water_counter(number_list1)
water_counter(number_list2)
water_counter(number_list3)

#result 7

