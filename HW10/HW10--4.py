
operDict:dict = {"upper": lambda a: a.upper(), "lower": lambda a: a.lower(),\
    "length": lambda a: len(a), "reverse": lambda a: a.reversed}
myString:str = input("please type a string")
myAction:str = input("plese type an action")
print("resault of action", operDict.get(myAction)(myString))
