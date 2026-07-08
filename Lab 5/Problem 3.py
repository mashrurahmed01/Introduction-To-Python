def find_max_min(numbers):
    if not numbers:
        return None, None

    max_val = numbers[0]
    min_val = numbers[0]

    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


num_list = [45, 12, 89, 5, 23]
maximum, minimum = find_max_min(num_list)
print("Max:", maximum, "Min:", minimum)