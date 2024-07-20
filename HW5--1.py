
positives:int = 0
negatives:int = 0
zeroes:int = 0
devideInSeven = 0
lastPositive = None
lastNegative = None
number:int = None

for i in range(1,5):
    number = int(input("please type an int"))
    if number == -9999:
        break
    if number >= 0:
        positives += 1
        lastPositive = number
    else:
        negatives += 1
        lastNegative = number
    zeroes += 1 if number == 0  else zeroes
    devideInSeven += 1 if number % 7 == 0 else devideInSeven
else:
    print(f"positives:{positives}, negatives:{negatives}, zeroes:{zeroes}, devideInSever:{devideInSeven},\
          lastNegative:{lastNegative}, lastPositive:{lastPositive}");
