def find_longest_name(names: list) -> str:
    return max(names, key=len)



print(find_longest_name(['Ali', 'Diyor', 'Jasurbek', 'Muhammad']))
# "Jasurbek"

print(find_longest_name(['Bo', 'Ali', 'Zara']))
# "Zara"