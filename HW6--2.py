import statistics
temps: list[float] = []
tempe: int = 0
#########################
while True:
    tempe = float(input("let me have a temprature"))
    if tempe == -999:
        break
    if tempe < -50 or tempe > 50:
        continue
    temps.append(tempe)
print(temps)
##while True:
    ##tempe = float(input("let me have a temprature"))
    ## why doesn't this work?
    ##Break if tempe == -999 else continue if  50 < tempe or tempe < -50 else temps.append
########################
temps2 :list[float] = [18.5 ,39.1, -20.0]
print("temps2 is:", temps2)
temps.extend(temps2)
print(temps)
########################
print(f"the highest temp in temps is: {max(temps)}")
########################
print(f"the lowest temp in temps is: {min(temps)}")
########################
print(f"the average temp in temps is: {sum(temps) / len(temps) : .2f}")
########################
print(f"the average temp in temps is: {statistics.mean(temps) : .2f}")
########################
del temps[0]
print(f"after remove first item: {temps}")
########################
temps.remove(39.1)
print(f"after remove of 39.1: {temps}")
########################
tempLast: float = temps.pop()
print(f"the last item in temps is: {tempLast}")
########################
temps.append(50)
temps2 = temps.copy()
print(f"temps2 is: {temps2}")
temps2.sort()
print('after sort of temps2', temps2)
temps2.sort(reverse=True)
print('after sort reverse of temps2 descending', temps2)
########################
##sort changes the original list, it sorts it
##sorted does'nt change the original list and create a new list on the fly
########################
##reversed lcreats an iterator
##if we want to creat a list we have to put it in brackets with the word "list" befor
##please look at the examples
print('after sorted', sorted(temps))
print('after sorted reverse', sorted(temps, reverse=True))
print('after reversed', reversed(temps))  # iterator
print('after list + reversed', list(reversed(temps)))  # iterator
########################



