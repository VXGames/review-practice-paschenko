
def calculate_positive_average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("List must contain only numbers")
    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
            count += 1
    if count > 0:
        average = total / count
    else:
        average = 0
    return average

data = [1, -2, 3, 4]
print(calculate_positive_average(data))
