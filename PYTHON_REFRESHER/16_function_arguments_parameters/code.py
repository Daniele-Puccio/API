def say_hello(name, surname):
    print(f"Hello {name} {surname}!")

say_hello("Bob", "Smith")

# ---

def say_hello(name, surname):
    print(f"Hello {name} {surname}!")

say_hello(surname="Bob", name="Smith")

# ---
def divide(dividend, divisor):
    if divisor != 0:
        print(int(dividend / divisor))
    else:
        print("you fool!")


divide(15,0)