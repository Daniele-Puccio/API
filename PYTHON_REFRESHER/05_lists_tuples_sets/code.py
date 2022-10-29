l = ["Bob","Rolf","Anne"]
t = ("Bob","Rolf","Anne")
s = {"Bob","Rolf","Anne"}

print(l[0])
print(t[0])

l[0]="Daniele"

print(l[0])

l.append("Lorenzo")
print(l)

l.remove("Rolf")
print(l)

s.add("Smith")
print(s)