while True:
    a = float(input("Birinchi son: "))
    b = float(input("Ikkinchi son: "))
    c = input("Amallar (+, - ,* , /): ")

    if c == "+":
        result = a + b
    elif c == "-":
         result = a - b
    elif c == "*":
        result = a * b
    elif c == "/":
        if b != 0:
            result = a / b
        else:
            result = "Xato! Nolga bo'lish mumkin emas."
    else:
        result = "Noma'lum amal!"

    print(f"Natija: {result}")
    break
