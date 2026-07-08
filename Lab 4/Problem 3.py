user_text = input("string: ")
cleaned = user_text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("palindrome.")
else:
    print("not a palindrome.")