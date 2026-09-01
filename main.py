from math_operations import add, divide, multiply, subtract
from utils import print_title

print_title("Модульный калькулятор")


while True:
    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: введите число. Попробуйте ещё раз.")


print()
print("Выберите операцию:")
print("1 — Сложение")
print("2 — Вычитание")
print("3 — Умножение")
print("4 — Деление")

choice = input("Ваш выбор: ")


if choice == "1":
    result = add(first_number, second_number)
elif choice == "2":
    result = subtract(first_number, second_number)
elif choice == "3":
    result = multiply(first_number, second_number)
elif choice == "4":
    try:
        result = divide(first_number, second_number)
    except ValueError as error:
        print(f"Ошибка: {error}")
        result = None
else:
    print("Неизвестная операция.")
    result = None


if result is not None:
    print(f"Результат: {result}")
