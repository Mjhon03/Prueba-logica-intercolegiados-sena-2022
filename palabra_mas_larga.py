"""
    Enunciado:
    Determinar cual es la plabra con mayor caracteres de un parrafo.
"""

def LongestWord(sen): 
    word_list = sen.split(' ')
    longest = ''
    for word in word_list:
        if len(longest) < len(word):
            longest = word
    return longest
    
parrafo= input()

print(LongestWord(parrafo))

#Test
# El hotel del centro es el más antiguo del pueblo y también es aquel que tiene más comodidades. Este hotel fue construido en 1911, pero primero se utilizó como casa de familia. En 1975 un inversionista compró esta propiedad y la reformó para transformarla en el hotel que hoy conocemos. Es un hotel pequeño, pero cuenta con servicio a la habitación, con pileta climatizada, con un restaurante de categoría, entre otras cosas.
# Muchas personas creen que los osos polares están en peligro de extinción, pero la denominación correcta sobre la situación de esta especie es que están en situación de conservación vulnerable. De todas formas, es necesario que se actúe rápidamente para evitar que esta especie desaparezca.
# La actividad del sector turístico ha aumentado considerablemente en la ciudad y esto ha generado muy buenos ingresos para las personas que trabajan en este sector. Esta mejora es una consecuencia de que el gobierno haya organizado mejor el circuito turístico y de que haya hecho campañas de difusión de los lugares que se pueden visitar.
# Los especialistas recomiendan que se mejore el tratamiento de la basura lo antes posible, ya que un buen tratamiento de la basura es fundamental para que se reduzca la contaminación. Por eso, es indispensable que se pueda organizar un sistema para recuperar los desechos reciclables.
#Result 
# inversionista
# denominación
# considerablemente
# contaminación