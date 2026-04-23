def filter_positive(numbers: list) -> list:
    return [n for n in numbers if n['value'] > 0]


print(filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}]))
# [{'value': 10}, {'value': 7}]

print(filter_positive([{'value': 0}, {'value': 5}, {'value': -3}]))
# [{'value': 5}]