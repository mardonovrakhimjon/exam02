def calculate_stats(numbers: list) -> dict:
    if not numbers:
        return {"sum": 0, "average": 0.0}
    
    total_sum = sum(numbers)
    
    average = round(total_sum / len(numbers), 2)
    
    return {"sum": total_sum, "average": average}

print(calculate_stats([3, 7, 10, -5, -8, 15, 22])) 

print(calculate_stats([10, 20, 30]))