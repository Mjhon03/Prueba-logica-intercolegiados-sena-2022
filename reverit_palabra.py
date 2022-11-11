""" 
    Enunciado:
    Funcion que devuelva una cadena en sentido contrario, por ejemplo hello word quedaria drow olleh
"""

def reverse(string): 
    str = "" 
    for i in string: 
        str = i + str
    return str

entrada = input()

print(reverse(entrada))



#Test
#Hola mundo
#sontenp0rone0
#
#Results
#odnum aloH
#0enor0pnetnos