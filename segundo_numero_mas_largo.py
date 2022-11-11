"""
    Enunciado: 
    Dado un listado de números, encuentra el SEGUNDO más grande.
"""

# Metod 1
def second_highest(array_num: list):
    new_arr = array_num
    order_arr = []

    while len(order_arr) < 2:
        highest = None

        for i in new_arr:
            if highest == None or i > highest:
                highest = i

        new_arr.remove(highest)
        order_arr.append(highest)

    print(f"The second highest number is '{order_arr[-1]}'.")


# Metodo 2
def second_highest_two(array_num: list):
    print(f"The second highest number is '{sorted(array_num)[-2]}'.")


# Tests
second_highest([1, 2, 3, 4, 5, 6, 7])
second_highest_two([1, 2, 3, 4, 5, 2, 7])
second_highest([3, 63, 2456, 879, -294, -4, 0])
second_highest_two([3, 63, 2456, 879, -294, -4, 0])

#The second highest number is '6'.
#The second highest number is '6'.
#The second highest number is '879'.
#The second highest number is '879'."""