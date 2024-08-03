
myList:list[str] = ["Mango","Orange","Banana","Apple","Strawberry", "Pineapple", "Grapes", "Watermelon"]
#a
print(list(map(lambda a: a[::-1] , myList)))
####################################
#b
print(list(map(lambda a: a[0] , myList)))
####################################
#c
print(list(map(lambda a: a.upper() , myList)))
####################################
#d
print("length", list(map(lambda a: len(a) , myList)))
##############################
#e
print("endswith", list(map(lambda a: a + "!" if a.endswith("s") else a, myList)))
######################
#f
newList:list[str] = ["Mango", 60],["Orange", 47],["Banana", 89],["Apple", 52],["Strawberry", 32], ["Pineapple", 50], ["Grapes", 69], ["Watermelon", 30]
print("calories", list(map(lambda a: a[1], newList)))
print("addition", list(map(lambda a: a[0] + str(a[1]), newList)))
print("over 50", list(map(lambda a: (a[0] + "!", a[1]) if a[1] > 50 else a, newList)))





