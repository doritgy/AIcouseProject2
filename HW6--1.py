
numbers: list[int] = []
for i in range(80, 101):
    numbers.append(i)
print(numbers)
numbers = []
numbers = [i for i in range(80, 101)]
#############################
print(f"the first number in numbers is: {numbers[0]}")
#############################
print(f"the last number in numbers is: {numbers[-1]}")
print(f"the last number in numbers is: {numbers[len(numbers) - 1]}")
#############################
print(f"the list contains {len(numbers)} items")
#############################
print(f"the numbers with index 3 to 12 are: {numbers[3:12]}")
#############################
print(f"the numbers with index 3 to the end: {numbers[3::]}")
#############################
print(f"the numbers with index from start to 9: {numbers[:9]}")
#############################
numbers.insert(len(numbers)//2, -999)
print(numbers)
#############################
print(numbers[:: -1])
#############################
numbers.remove(-999)
print(numbers[1::2])
#############################





