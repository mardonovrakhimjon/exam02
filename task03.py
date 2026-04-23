def calculate_tax(salary: int) -> dict:
    result = {"gross": None, "tax": None, "net": None, "rate": None}

    rate = None
    if salary <= 5000000:
        rate = 0
    elif salary <= 10000000:
        rate = 12
    if salary <= 20000000:
        rate = 18

    gross = salary
    tax = salary * rate / 100
    net = salary - tax

    result['gross'] = gross
    result['tax'] = tax
    result['net'] = net
    result['rate'] = rate

    return result

print(calculate_tax(8_000_000))
print(calculate_tax(3_000_000))
