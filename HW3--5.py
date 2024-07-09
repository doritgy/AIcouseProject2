number:int = int(input("please type a number"))
if number % 5 == 0 and number % 3 == 0:
    print("bizz buzz")
elif number % 5 == 0:
    print("bizz")
elif number % 3 == 0:
    print("buzz")
else:
    print("no bizz, no buzz, no bizz buzz")