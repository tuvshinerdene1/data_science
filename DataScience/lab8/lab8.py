def factorial(n):
    """
    n тооны факториал олох
    параметр n тоо нь эерэг бүхэл тоо өгөгдөнө
    буруу параметр орж ирвэл ValueError алдаа үүсгэнэ
    n тооны факториалыг буцаана
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return n * factorial(n-1)


# print(factorial(3))  # 6
# print(factorial(9))  # 362880
# print(factorial(-1))  # ValueError
# print(factorial(3.0))  # ValueError

test_values = [3, 9, -1, 3.0]

for val in test_values:
    try:
        result = factorial(val)
        print(f"Factorial of {val} is {result}")
    except ValueError:
        print(f"Error: {val} is not a valid input ")


def fibonacci(n):
    """
    Фибоначчийн n-р элементийг олох функц
    n параметрийн утга нь дарааллын хэд дэх элементийг
    олохыг илтгэх бөгөөд 0-с эхэлсэн эерэг бүхэл тоо байна
    Дарааллын n-р утгыг буцаана
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))  # 8
# print(fibonacci(19))  # 4181
# print(fibonacci(0))  # 0
# print(fibonacci(-4))  # ValueError
# print(fibonacci(3.14))  # ValueError
test_values1 = [6,19,0,-4,3.14]
for val in test_values1:
    try:
        print(fibonacci(val))
    except ValueError:
        print(f"Error {val} is not valid input")