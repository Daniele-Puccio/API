def hello():
    print("Hello!")
def users_age_in_seconds():
    age=int(input("Insert your age: "))
    age_in_seconds=age*365*24*60*60
    print(f"Your age in seconds: {age_in_seconds}s")

hello()
users_age_in_seconds()