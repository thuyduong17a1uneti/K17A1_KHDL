def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def calculate_expressions(n):
    #A
    sum_odd = sum(i for i in range(1, n + 1) if i % 2 != 0)
    #B
    sum_even = sum(i for i in range(1, n + 1) if i % 2 == 0)
    #C
    product = 1
    for i in range(1, n + 1):
        product *= i
    #D
    product_divisible_by_3 = 1
    for i in range(1, n + 1):
        if i % 3 == 0:
            product_divisible_by_3 *= i
    #E
    sum_prime = sum(i for i in range(2, n + 1) if is_prime(i))
    #F
    sum_series = 0
    sign = 1
    for i in range(1, n + 1):
        sum_series += sign * (1 / i)
        sign *= -1
    return sum_odd, sum_even, product, product_divisible_by_3, sum_prime, sum_series
n = int(input("Nhập giá trị n: "))
A, B, C, D, E, F = calculate_expressions(n)
print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)
print("E =", E)
print("F =", F)