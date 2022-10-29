def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


students = [
    {"name":"BOB", "grades":(25,30,40)},
    {"name":"CHARLIE", "grades":()},
    {"name":"ROX", "grades":(25,30,40)}
]


print("Welcome to the average grade program.")

try:
    for student in students:
        average = divide(sum(student['grades']),len(student['grades']))
        print(f"{student} average of: {average}")
except ZeroDivisionError as e:
    print("There are no grades yet in your list!")
except TypeError as va:
    print("You have only 1 grade, for average you must have 2 or more grade.")
else:
    print(f"The average grade is {average}")
finally:
    print("Thanks you!")

