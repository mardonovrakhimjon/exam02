def calculate(num1: float, num2: float, operator: str) -> float:
    if operator == "+":
        return round(num1 + num2, 2)
    elif operator == "-":
        return round(num1 - num2, 2)
    elif operator == "*":
        return round(num1 * num2, 2)
    elif operator == "/":
        if num2 != 0:
            return round(num1 / num2, 2)
        else:
            return "Xato! Nolga bo'lish mumkin emas."
    else:
        return "Noma'lum amal!"
print(calculate(15, 3, "/"))    # 5.0
print(calculate(8, 5, "*"))   # 40.0
print(calculate(10, 0, "/"))    # Error: Nolga bo'lish mumkin emas
print(calculate(7, 4, "^"))     # Error: Noto'g'ri operator