import random, statistics
myList:list[int] = [random.randint(1,100) for _ in range(50)]
print(myList)
print("over 50", list(filter(lambda x:  x > 50 , myList)))
######################
print("divisionl by 7", list(filter(lambda x:  x % 7 == 0 , myList)))
######################
print("two digits", list(filter(lambda x:  10 <= x < 100 , myList)))
######################
print("first digit same as second digit", list(filter(lambda x:  10 <= x < 100 and x % 10 == x // 10, myList)))
######################

##                 answer 1: when we don't know the number of digits'
def sumDigits(x:int) -> int:
    y:int = 0
    while x != 0:
        y += x % 10
        x = x // 10
    return y
print(myList)
##with map
print("mapping1" , list(map(lambda x: sumDigits(x) , myList)))
## with filter and map but we get the sum not the original number
print("mapping2" , list(filter(lambda x: x == 9 ,map(lambda x: sumDigits(x) , myList))))
##with an external function
print("mapping3" , list(filter(lambda x: sumDigits(x) == 9, myList)))

##                     answer number 2: if we know that we have numbers with maximum 2 digits
print("sum of digits = 9", list(filter(lambda x: x % 10 + x // 10 == 9, myList)))

########################################
print("avg", statistics.mean(myList), "greater than the average", list(filter(lambda x: x > statistics.mean(myList), myList)))
#######################################
print("max", max(myList), "greater than half the max", list(filter(lambda x: x > max(myList) / 2, myList)))
#######################################
numbers2:list[int] = [8, 5, 3, 9, 10, 12]

print("list greater than mediant" ,list(filter(lambda x: x > (sorted(numbers2)[int((len(numbers2)+1) / 2) - 1] if len(numbers2) % 2 else (sorted(numbers2)[int(len(numbers2) / 2) - 1] + sorted(numbers2)[int((len(numbers2) + 2) / 2) - 1]) / 2 ) , sorted(numbers2))))
#########################################
try:
    myList2 = [int(input("please enter an integer")) for _ in range(5)]
except Exeption as e:
    Print("something went wrong, try from the beginning")
print(myList2)
print("not in", list(filter(lambda x: x not in myList2, range(100))))
#########################################
def primeNo(x:int) -> bool:
    for i in range(2,x):
        if x % i:
            continue
        else:
            return False
    else: return True

print("prime only", list(filter(lambda x: primeNo(x) , range(3,100))))





