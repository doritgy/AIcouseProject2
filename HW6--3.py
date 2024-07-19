import random
bools: bool = []
for i in range(1,4):
    bools.append(random.choice([True, False]))
print(bools)
########################
print(f"the list contains only True:True/False: {all(bools)}")
########################
print(f"the list contains at leas one True:True/False: {any(bools)}")
########################
print(f"the list contains all False:True/False: {not any(bools)}")
########################
print(f"the list contains at least one False:True/False: {not all(bools)}")
#########################
nums: int = []
for i in range(10):
    nums.append(random.randint(-2,2))
print(nums)
#########################
print(f"all numbers in nums are not zero: {all(nums)}")
#########################
print(f"at least one number in nums is not zero: {any(nums)}")
#########################
print(f"all numbers in nums are zero: { not any(nums)}")
#########################
print(f"at least one number in nums is zero: {not all(nums)}")


