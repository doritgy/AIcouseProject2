
for i in range(1,21):
    print(f"{i}", end=' ')
print(f"\n")
for i in range(1,21,2):
    print(f"{i}", end=' ')
print(f"\n")
jump:int = int(input("please type what jump you want between numbers"))
for i in range(1,21,jump):
    print(f"{i}", end=' ')
print(f"\n")
firstN:int = int(input("please type the start number"))
lastN:int = int(input("please type the last number"))
jump:int = int(input("please type the jump between the numbers"))
for i in range(firstN,lastN+1,jump):
    print(f"{i}", end=' ')
