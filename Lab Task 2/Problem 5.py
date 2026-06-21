print("Enter marks to check: ")
x = int(input())
if x >= 90 and x <= 100:
    print("A+")
if x >= 85 and x < 90:
    print("A")
if x >= 80 and x < 85:
    print("B+")
if x >= 75 and x < 80:
    print("B")
if x >= 70 and x < 75:
    print("C+")
if x >= 65 and x < 70:
    print("C")
if x >= 60 and x < 65:
    print("D+")
if x >= 50 and x < 60:
    print("D")
if x < 50:
    print("F")
if x > 100:
    print("Invalid number")