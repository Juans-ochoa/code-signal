'''Dada una secuencia de enteros como una matriz, determine si es posible obtener una secuencia estrictamente creciente eliminando no más de un elemento de la matriz.

Nota: secuencia , , ..., se considera que es un aumento estricto si . La secuencia que contiene solo un elemento también se considera estrictamente creciente.a0a1ana0 < a1 < ... < an'''
def solution(sequence:list[int]):
    sec1 = 0
    sec2 = 0
    for i in range (len(sequence) -1 ):
        if(sequence[i] >= sequence[i+1]):
            sec1 += 1
    
    if sec1 > 1: return False

    for i in range (len(sequence) -2 ):
        if(sequence[i] >= sequence[i+2]):
            sec2 += 1
    
    if sec2 > 1: return False
    
    return True
    

print(solution([1, 2, 1, 2]))
# print(solution([1, 1, 2, 3, 4, 4]))
# print(solution([1, 1, 1, 2, 3]))
# print(solution([1, 2, 3, 4, 5, 3, 5, 6]))