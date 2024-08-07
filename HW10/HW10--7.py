
countries:list = [ {'name': 'Israel', 'population': 9.3, 'birth': 1948},
{'name': 'United States', 'population': 331.9, 'birth': 1776}, {'name': 'Japan',
'population': 125.8, 'birth': 660 }, {'name': 'Australia', 'population': 25.7, 'birth': 1901},
{'name': 'Canada', 'population': 38.0, 'birth': 1867} ]


print("more than 30 mil", list(filter(lambda a: {a.get("population")} if a["population"] > 30 else None, countries )))
#######################
print("birth after 1800", list(filter(lambda a: {a.get("birth")} if a["birth"] > 1800 else None, countries )))
#######################
print("names of countries", list(map(lambda a: {a.get("name")},countries)))
#####################
print("year of birth", list(map(lambda a: {a.get("birth")},countries)))
#####################
print("sorted with year of birth", list(sorted(countries, key = lambda a: a["birth"])))
#########################
print("sorted with population", list(sorted(countries, key = lambda a: a["population"])))




