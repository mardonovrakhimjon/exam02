def calculate_tax(salary: int) -> dict:
    if salary <= 5000000:
        rate_str = "0%"
        tax = 0
    elif salary <= 10000000:
        rate_str = "12%"
        tax = (salary - 5000000) * 0.12
    elif salary <= 20000000:
        rate_str = "18%"
        tax = (5000000 * 0.12) + (salary - 10000000) * 0.18
    else:
        rate_str = "25%"
        tax = (5000000 * 0.12) + (10000000 * 0.18) + (salary - 20000000) * 0.25

    tax = int(tax)
    return {
        "gross": salary,
        "tax": tax,
        "net": salary - tax,
        "rate": rate_str
    }

print(calculate_tax(8_000_000))
print(calculate_tax(3_000_000))
