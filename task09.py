def find_min_max(numbers: list) -> dict:
    result = {
        "max": max(numbers),
        "min": min(numbers)
    }
    
    return result


print(find_min_max([3, 7, 10, -5, -8, 15, 22])) 
print(find_min_max([100, 50, 200, -10])) 