user_input = input("Enter number: ")
n = int(user_input)

a = 0
b = 1

while a < n:
    print(a)
    next_number = a + b
    a = b
    b = next_number
    b = next_number