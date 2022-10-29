friends = {"Bob","Rolf","Anne"}
abroad = {"Bob","Anne"}
local_friends = friends.difference(abroad)
print(local_friends)



local = {"Bob"}
abroad = {"Rolf","Anne"}
friends = local.union(abroad)
print(friends)


art = {"Bob","Jen","Rolf","Charlie"}
scienze = {"Bob","Jen","Adam","Anne"}

both = art.intersection(scienze)
print (both)

