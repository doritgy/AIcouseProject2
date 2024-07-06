##start
firstInt:int = int(input("please type the first integer"))
secondInt:int = int(input("please type the second integer"))
if firstInt > secondInt:
    print(secondInt,firstInt)
elif secondInt > firstInt:
    print(firstInt, secondInt)
else: print("the nombers are the same", firstInt)
##end