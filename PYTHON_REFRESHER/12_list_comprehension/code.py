numbers = [1, 3 ,5]
doubleds = [x * 2 for x in numbers]
print(doubleds)

friends = ["Rolf", "Sam", "Samantha","Sara","Jen"]
start_s= [x for x in friends if x.startswith("S")]
print(start_s)

print(id(friends))
print(id(start_s))