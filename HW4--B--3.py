stringg:str = ""
lastString:str = ""
bigString:str = ""
while True:
    stringg = input("please enter a string")
    if stringg == lastString:
        break
    else:
        bigString = bigString + stringg
        print(f"{bigString}")
    lastString = stringg
print(f"{bigString}")

