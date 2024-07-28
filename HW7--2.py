myStr:str = " fun-day "
myStr = myStr.strip()
print(myStr)
#############################
print("hello".isalpha())
#############################
print("777".isdigit())
#############################
print("   ".isspace())
#############################
print("".join(['A','J','N','I','N']))
##########################
print("*".join(['A','J','N','I','N']))
##########################
print("true" if "e" in "hEllo".lower() else "false")
########################################
myStr = input("please enter some text")
myList:list[str] = []
myList = [myStr[i].upper() for i in range(len(myStr)) if myStr[i].isalpha()]
print("myList", myList)



