

myList:list[str] = ["grand theft auto V","Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
#a
print("only more than 8 letters" ,list(filter(lambda a: a if len(a) > 8 else "", myList)))
##########################
#b
print("only starting with f", list(filter(lambda a: a.lower().startswith("f"), myList)))
#########################
#c
print("only games with two words" ,list(filter(lambda a: a if len(a.split()) == 2 else "", myList)))
################################
#d
print("only games with V inside the name" ,list(filter(lambda a: a if "v" in a.lower()  else "", myList)))
##################################
#e
print("only games with special characters inside the name" ,list(filter(lambda a: a if not a.replace(" ","").isdigit() and not  a.replace(" ","").isalpha() else "", myList)))
###############################
#f
myList:list[str] = [["grand theft auto V", 2017],["Fortnite", 2010], ["The Elder Scrolls V: Skyrim",2018], ["Dark Souls",2009], ["Overwatch", 2020]]
print("only games that were produced after 2014" ,(list(map(lambda a: a[0], list(filter(lambda a: a if a[1] > 2014 else "" , myList))))))
#################################







