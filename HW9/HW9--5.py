
myList:list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
#a
print("sorted by length", sorted(myList, key = lambda a: len(a)))
#######################
#b
print("sorted by last letter", sorted(myList, key = lambda a: a[len(a) - 1]))
#############################
#c
print("sorted by reverse of letters", sorted(myList, key = lambda a: a[::-1]))
##############################
#d
newList:list[str] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print("sorted by distance", list(sorted(newList, key = lambda a: a[1])))
print("sorted by distance, with reverse", list(sorted(newList, reverse = True, key = lambda a: a[1])))
print("sorted by continent and then distance", list(sorted(newList, key = lambda a: (a[2], a[1]))))


