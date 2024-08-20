import random

my_list:list[int] = [random.randint(100, 500) for _ in range(50)]
my_set = set(my_list)
print(len(my_set))