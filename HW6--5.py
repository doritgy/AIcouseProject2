import random


nums: list[float] = []
nums = [random.random() * 1000 for _ in range(1,5)]
print(nums)
while True:
    try:
        index = int(input('Enter an index which is an integer:'))
        if index == -999:
            break
        print(f"number is {nums[index]}")
    except Exception as e:
        print(f'something went wrong --{e}-- ... try again')
print("finished with no exception")
################
