##start
listOfNo = []
result1: int = 0
result2: int = 1
print(listOfNo)
for i in range(1,4):
    listOfNo.append(int(input("please type an integer")))
    print(i)
    result1 += listOfNo[i-1]
    result2 *= listOfNo[i-1]
    print(result1,result2)
print("the sum of the integers is",result1)
print("the multiplication of the integers is",result2)

##end