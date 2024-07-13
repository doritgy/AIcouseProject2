
highest1:int = 0
highest2:int = 0
noOfStudents = 0
totalGrades = 0
iq:int = int(input("please type an iq grade"))
while iq > 30 and iq < 300:
    if iq > highest1:
        highest1 = iq
    totalGrades += iq
    noOfStudents += 1
    iq:int = int(input("please type an iq grade"))
avg1:float = totalGrades / noOfStudents
print(f"average of class:{avg1}")
print(f"highest grade of class:{highest1}")
print(f"one year of python study is over")
noOfStudents = 0
totalGrades = 0
iq:int = int(input("please type an iq grade"))
while iq > 30 and iq < 300:
    if iq > highest2:
        highest2 = iq
    totalGrades += iq
    noOfStudents += 1
    iq:int = int(input("please type an iq grade"))
avg2:float = totalGrades / noOfStudents
print(f"{'the class did better!' if avg2>avg1 else 'the class did worse!'} first average was {avg1} second average was {avg2} ")
print(f"highest grade of class after a year is: {highest2} the most heigh grade is:{highest1 if highest1>highest2 else highest2}")