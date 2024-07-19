import random

nums: list[int] = [i for i in range(95,106)]
print(nums)
##########################
nums: list[int] = [i for i in range(10,21, 2)]
print(nums)
##########################
nums: list[int] = [random.choice([True, False]) for _ in range(5)]
print(nums)
##########################
##I will use "_" when I use an index which I will never use in my comprehension
## The code is more readable because I can see clearly the range, without the index which is not interesting
##########################
nums = [random.randint(1,100) for _ in range(1,11)]
print(nums)
##########################
nums2: list[int] = [num for num in nums if num > 50]
print(nums2)
##########################
nums: list[int] = [[n for n in (random.randint(1,100) for _ in range(1,11)) if n > 50] ]
print(nums)
#########################
strs: list[str] = []
newStrs: list[str] = []
while True:
    strg = input("please type a string")
    if strg == "end":
        break
    else:
        strs += strg
newStrs = [n for n in strs if n not in ['t' , ' ']]
print(newStrs)
###########################






