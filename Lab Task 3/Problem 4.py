prime_sum = 0

for current_number in range(2, 1000):
    is_prime = True

    for i in range(2, current_number):
        if current_number % i == 0:
            is_prime = False
            break

    if is_prime == True:
        prime_sum = prime_sum + current_number

print(prime_sum)