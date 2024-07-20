
while True:
    num:int = int(input("let me have an even integer"))
    if num % 2:
        break
    else:
        print("please type an even integer")

for i in range(1, num + 1):
    numOfSp:int = num + 1 - i
    print(f" " * numOfSp, end="")
    mull:int = "*" * (i * 2 - 1)
    print(mull)



