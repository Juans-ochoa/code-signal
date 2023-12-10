def solution(numbers:list[int]):
    product_numbers = []
    for i in range(0, len(numbers) - 1):
        product_numbers.append(numbers[i] * numbers[i+1])
    return max(product_numbers)

print(solution([1, 2, 3]))