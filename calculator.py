def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b  # ← НОВАЯ ФУНКЦИЯ

# Главная функция
if __name__ == "__main__":
    print("Калькулятор")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"3 * 4 = {multiply(3, 4)}")  # ← НОВЫЙ ВЫВОД
