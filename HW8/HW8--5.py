import func_with_return, func_without_return

number:int = func_with_return.get_int("please enter an integer")
print("the number recieved from the function:", number)


gradesList:list[int] = []
while True:
    a = func_with_return.get_int("please enter a grade") ##I am sure to get an integer
    if a == -99: ##end of the program
        break
    if  a > 100 or a < 0:
        print("illegal grade, try again")
        continue
    gradesList.append(a)
func_without_return.my_statistics(gradesList) ##statistics printed