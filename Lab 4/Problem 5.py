def print_elem(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1

    result = ", ".join(f"{k} => {v}" for k, v in counts.items())
    print(result)


sample = [10, 20, 30, 30, 30, 30, 20, 40]
print_elem(sample)