def sort_names(students: list) -> list:
    return sorted(students, key=str.lower)


print(sort_names(["Ali", "Vali", "Hasan", "Husan", "Aziza"]))
# ["Ali", "Aziza", "Hasan", "Husan", "Vali"]

print(sort_names(["Zara", "Bobur", "Anvar"]))
# ["Anvar", "Bobur", "Zara"]