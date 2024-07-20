import random
noOfGames:int = 0
while True:
    myNumber = random.randint(1,100)
    while True:
        yourNumber = int(input("please guess what the number is"))
        print(f"too big" if myNumber < yourNumber else "too little" if myNumber > yourNumber else "")
        noOfGames += 1
        if yourNumber == myNumber:
            print("bingo")
            break
    print(f"you succeeded after {noOfGames} games")
    ans = input("do you want to continue?")
    if ans == "no":
        break