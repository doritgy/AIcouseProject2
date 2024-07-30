import func_without_return, statistics
func_without_return.my_ascending(7, -12)

func_without_return.my_details("AI is the best")

func_without_return.say_bool(True)
func_without_return.say_bool(False)

func_without_return.print_zugi([5, 3, 2, 10, 15, 14, 14])

gradesList:list[int] = []

while True:
    try:
        a = int(input("please enter a grade"))
        if a == -99:
            break
        if  a > 100 or a < 0:
            print("illegal grade, try again")
            continue
        gradesList.append(a)
    except Exception as e:
        print("something went wrong ", e, "try again")
        continue
func_without_return.my_statistics(gradesList)


help(func_without_return)
