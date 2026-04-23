def analyze_list(items: list) -> dict:
    total = len(items)
    
    report = {}
    for item in items:
        report[item] = items.count(item)
        
    unique = 0
    duplicates = []
    most_common = items[0]
    for item in report:
        if report[item] == 1:
            unique += 1
        else:
            duplicates.append(item)

        if report[item] > report[most_common]:
            most_common = item

    return {
        "total": total,
        "unique": unique,
        "duplicates": duplicates,
        "most_common": most_common
    }
    
print(analyze_list(["Ali", "Vali", "Ali", 1, 2, 1]))
# {
#   "total": 6,
#   "unique": 4,
#   "duplicates": ["Ali", 1],
#   "most_common": "Ali"
# }