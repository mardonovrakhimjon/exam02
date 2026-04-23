def find_pattern(items: list, pattern: str, match_type: str) -> list:
    lower_pattern = pattern.lower()
    result = []
    
    for item in items:
        item_lower = item.lower()
        if match_type == "starts" and item_lower.startswith(lower_pattern):
            result.append(item)
        elif match_type == "ends" and item_lower.endswith(lower_pattern):
                result.append(item)
        elif match_type == "contains" and pattern in item_lower:
                result.append(item)
            
    return result
                

print(find_pattern(["Ali", "Alisher", "Vali", "Aziz"], "A", "starts")) 
# ["Ali", "Alisher", "Aziz"]

print(find_pattern(["Alisher", "Bobur", "Jasur"], "ur", "ends")) 
# ["Bobur", "Jasur"]

print(find_pattern(["Python", "Java", "JavaScript"], "java", "contains"))
# ["Java", "JavaScript"]