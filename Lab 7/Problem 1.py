try:
    num = 10
    result = num / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")