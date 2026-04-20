def sort_names(students: list) -> list:
    return sorted(students, key=str.lower)

print(sort_names(["Ali", "Vali", "Hasan", "Husan", "Aziza"]))

print(sort_names(["Zara", "Bobur", "Anvar"]))