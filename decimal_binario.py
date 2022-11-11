"""
    Enunciado:
    Crea un programa que se encargue de transformar un numero binario a decimal sin utilizar funciones propias del lenguaje.
"""

def binToDec(bin):
    i = len(bin) - 1
    dec = 0

    for p in bin:
        dec += int(p) * 2 ** i
        i = i - 1

    return dec

print( binToDec(input("Numero para convertir: ")))

#Test
# 101000
# 101010101
# 0010101101010101
# 1111111111111111111
#Result 
#341
#40
#11093
#524287

