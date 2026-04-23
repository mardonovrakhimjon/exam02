def count_by_grade(grades: dict, target_grade: int) -> dict:
    result = {"count": 0, "students": []}
    for name, grade in grades.items():
        if grade == target_grade:
            result["students"].append(name)
            result["count"] += 1

    return result

print(count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5))
# {"count": 2, "students": ["Ali", "Husan"]}

print(count_by_grade({"Aziz": 4, "Bobur": 4, "Diyor": 3}, 4))
# {"count": 2, "students": ["Aziz", "Bobur"]}
