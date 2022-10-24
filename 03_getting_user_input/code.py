# -- fstring --
 
name = input("Inserisci il tuo nome: ")
print(name.capitalize())

# -- Mathematics user inputs --
size_input =input("Inserire le misure della casa (in piedi): ")
square_feet = int(size_input)
square_metres= square_feet / 10.8
print(f"{square_feet} piedi sono {square_metres:.2f} metri")
