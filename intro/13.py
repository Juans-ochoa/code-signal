'''Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.'''


def solution(inputString: str) -> str:
    start, end = -1, -1

    for i in range(len(inputString)):
        if inputString[i] == '(':
            start = i
        if inputString[i] == ')':
            end = i

            return solution(inputString[:start]+inputString[start+1:end]
                            [::-1]+inputString[end+1:])

    return inputString


# res = solution('hola(bar(tol(hi)))techo(love(one))(tomo)late(tomo(tato))')
res = solution('foo(bar(baz))blim')
print(res)
