import func_with_return

avg1:float = func_with_return.my_average(90,99)
print(f" the average of the numbers is {avg1: .2f}")

head1:str = func_with_return.my_headline("python has concuered the world")
print(head1, head1)

res_con:list[int] = func_with_return.concat_list([9, 8, 7,], [6, 5, 4, 3,],  [2, 1,])
print("the joined list is:", res_con, "the lebgth of it is:", len(res_con))

help(func_with_return)

print(func_with_return.say_bool(True))
print(func_with_return.say_bool(False))

my_list:list[str] = func_with_return.print_zugi([5, 3, 2, 10, 15, 14, 14])
print(my_list)
