friends = ["Rolf","Jen","Bob","Anne"]

for friend in friends:
    print(f"{friend} is my friend.")


grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade
print(f"The average is {total/amount}")