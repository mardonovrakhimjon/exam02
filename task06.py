def analyze_grades(students: dict) -> dict:
    average = sum(students.values()) / len(students)
    above_average = [name for name, ball in students.items() if ball > average]
    # for name, ball in students.items():
    #     if ball > average:
    #         above_average.append(name)
    return {'average': average, 'above_average': above_average}
    
print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))

print(analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 5}))