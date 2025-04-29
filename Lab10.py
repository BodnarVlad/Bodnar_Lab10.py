def factorial_recursive(n):
    if not isinstance(n, int):
        raise ValueError()
    if n < 0:
        raise ValueError()
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def fibonacci_recursive(n):
    if not isinstance(n, int):
        raise ValueError()
    if n < 0:
        raise ValueError()
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def sum_list_recursive(lst):
    if not isinstance(lst, list):
        raise ValueError()
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])

def is_palindrome_recursive(s):
    if not isinstance(s, str):
        raise ValueError()
    s = ''.join(c.lower() for c in s if c.isalnum())
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

# Перевірка функцій
def main():
    print("Перевірка factorial_recursive:")
    print(factorial_recursive(5))   # 120
    print(factorial_recursive(0))   # 1

    print("\nПеревірка fibonacci_recursive:")
    print(fibonacci_recursive(6))   # 8
    print(fibonacci_recursive(0))   # 0

    print("\nПеревірка sum_list_recursive:")
    print(sum_list_recursive([1, 2, 3, 4]))  # 10
    print(sum_list_recursive([]))           # 0

    print("\nПеревірка is_palindrome_recursive:")
    print(is_palindrome_recursive("А роза упала на лапу Азора"))  # True
    print(is_palindrome_recursive("Привіт"))                       # False

if __name__ == "__main__":
    main()
