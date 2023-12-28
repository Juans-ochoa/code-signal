'''You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.'''

'''Se le proporciona una serie de números enteros que representan las coordenadas de obstáculos situados en línea recta.

Suponga que está saltando desde el punto con la coordenada 0 hacia la derecha. Sólo se permite realizar saltos de la misma longitud representados por algún número entero.

Encuentra la longitud mínima del salto suficiente para evitar todos los obstáculos.'''


def solution(inputArray):
    step = 1

    while True:
        res = any([x % step == 0 for x in inputArray])
        if res:
            step += 1
        else:
            break

    return step


# solution([5, 3, 6, 7, 9])
solution([1000, 999])
