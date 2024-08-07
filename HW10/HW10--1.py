
myDict:dict = {"name": "Israel", "birth": 1948, "population_millions": 9.3,\
               "capital": "Jerusalem", "language": "Hebrew", "cities": ["Jerusalem", "Tel Aviv", "Heifa","Rishon LeZion", "Petah Tikva", "Ashdod"],\
               "currency": "ILS" , "area_Kilometer": (22, 145), "gdp_billion": 450}

#a
print("city Jerusalem", myDict.get( "capital"))
##############################
#b
print("keys", myDict.keys())
############################
#c
myList:list = [item[0].upper() for item in myDict.items()]
myList:list = [key.upper() for key in myDict.keys()]
print("myList", myList)
##############################
#d
print("my values", myDict.values())
############################
#e
myList:list = [(len(str(value))) for value in myDict.values()]
print("my list now", myList)
############################
#f
print("all items", list(item for item in myDict.items()))
#######################
#g
myDict2:dict = myDict.copy()
print("myDict2", myDict2)
################################
#h
myDict2.clear()
print(myDict2)
##################################
#i
newDict:dict = myDict.fromkeys(myDict.keys(), None)
print("newDict", newDict)
################################
#j
del myDict["currency"]
print(myDict)
#########################################
#k
print("area_kilometer", myDict.pop("area_Kilometer"))
#########################################
#l
myDict.update({"national_sport": "soccer", 'population_millions': 9.4})
print(myDict)
#############################




