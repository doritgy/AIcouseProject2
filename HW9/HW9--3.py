import random
myList:list[int] = []
myList = [random.randint(-50, 50) for _ in range(20)]
print(myList)
#a
print("3 exponentiation", list(map(lambda a: a**3, myList)))
###############################
#b
print("only last digit", list(map(lambda a: a % 10, myList)))
##################################
#c
print("in farenheit", list(map(lambda a: a * 0.18 + 32, myList)))
################################
#d
print("positive/negative", list(map(lambda a: "positive" if a>=0 else "negative", myList)))
###############################
#e
print("max/min", list(map(lambda a: "max" if a == max(myList) else "min" if a == min(myList) else a, myList)))
###############################
#f
print("original     ", myList)
print("change digits", list(map(lambda a: a if 0 <= abs(a) <= 10 else  (a % 10) * 10 + a // 10 if a > 0  else (abs(a) // 10 + (abs(a) % 10) * 10) * (-1)  , myList)))
################################
#g
print("absolute", list(map(lambda a: abs(a) , myList)))
################################
#h
newList:list[int] = [[7000, 10500], [8000, 2000], [20200, 21000],[33000, 300]]
print(newList)
print("balance", list(map(lambda a: a[0] - a[1] , newList)))





