grade:int = int(input("what is your grade?"))
if grade >=0 and grade<=40:
    print("try harder")
elif grade>=41 and grade<=60:
    print("you're getting there")
elif grade >=61 and grade<=80:
    print("pretty good")
elif grade >=81 and grade <= 95:
    print("ausome")
elif grade >= 96 and grade<=100:
    print("excellent")
else: print("illegal grade")