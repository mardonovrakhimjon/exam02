def analyze_list(items):
    total = len(items)

    unique_elements = set(items)
    unique_count = len(unique_elements)
    
    duplicates = []
    most_common = None
    max_count = 0
    
    for item in unique_elements:
        count = items.count(item)
        if count > 1:
            duplicates.append(item)
        
        if count > max_count:
            max_count = count
            most_common = item
            
    return {
        "total": total,
        "unique": unique_count,
        "duplicates": duplicates,
        "most_common": most_common
    }
    
print(analyze_list(["Ali", "Vali", "Ali", 1, 2, 1]))
