def analyze_grades(students: dict) -> dict:
    if not students:
        return {"average": 0.0, "above_average": []}
    
    grades = students.values()
    average = sum(grades) / len(grades)
    
    above_average = [name for name, grade in students.items() if grade > average]
    
    return {
        "average": average,
        "above_average": above_average
    }

print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))

print(analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 5}))