def named(**kwargs):
    print(kwargs)

named(name="BOB", age=25)

# ---
def named(name,age):
    print(name,age)

details ={"name":"Bob","age": 25}
named(**details)

# ---

def named(**kwargs):
    print(kwargs)

details = {"name":"Bob","age" : 25}
named(**details)

def print_nicely(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="bob", age=25)