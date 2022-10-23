# -- fstring --
name ="Bob"
print(f"Hello, {name}")

name="Rolf"
print(f"Hello, {name}")

# -- Template --
name ="Paolo"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

longer_phrase ="Hello, {}. Today is {}."
formatted = longer_phrase.format("Luigi","Monday")
print(formatted)