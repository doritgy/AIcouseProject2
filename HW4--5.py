
noOfStudents = 0
totalGrades = 0
iq:int = int(input("please type an iq grade"))
while iq > 30 and iq < 300:
    totalGrades += iq
    noOfStudents += 1
    iq:int = int(input("please type an iq grade"))
avg1:float = totalGrades / noOfStudents
print(f"one year of python study is over")
noOfStudents = 0
totalGrades = 0
iq:int = int(input("please type an iq grade"))
while iq > 30 and iq < 300:
    totalGrades += iq
    noOfStudents += 1
    iq:int = int(input("please type an iq grade"))
avg2:float = totalGrades / noOfStudents
print(f"{'the class did better' if avg2>avg1 else 'the class did worse'} first average was {avg1} second average was {avg2} ")
