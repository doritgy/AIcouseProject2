myStr:str = ""
myList:list[str] = []
myNewStr:str = ""
myStr = "Dorit Guy Hod-Hasharon"
print("the length of the string is:", len(myStr))
#####################
print(myStr.upper())
#####################
print(myStr.lower())
#####################
print(myStr.startswith("Dorit Guy"))
####################
print(myStr.endswith("Hod-Hasharon"))
####################
myList = myStr.split()
print(myList)
#######################
print(myStr.replace(" ", "*"))
#########################
myList = myStr.split("*")
print(myList)
##########################
print(myStr.center(50, "="))
#########################
print(myStr[4:])
####################
print(myStr[:4])
####################
print(myStr[::2])
####################
myNewStr = myStr.lower()
print("my new string:", myNewStr.title())
#############################






