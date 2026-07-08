def count(d):
    freq = {}
    for value in d.values():
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1
    return freq

dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
frequency = count(dict)
print(frequency)