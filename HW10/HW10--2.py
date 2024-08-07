
#a
myDict:dict = {"add": "adding item", "delete": "deleting item", "update": "updating item"}
def getAction(action:str) ->str:
    return(myDict.get(action))

print(getAction("add"))
print(getAction("delete"))
print(getAction("update"))
###
operDict:dict ={"add": "adding item", "delete": "deleting item", "update": "updateing item"}
print("add", operDict["add"])
print("delete", operDict["delete"])
print("update", operDict["update"])
#################################


