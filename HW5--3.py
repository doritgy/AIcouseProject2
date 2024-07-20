
num:int = int(input("please enter an integer"))
for i in range(1, num + 1):
    for j in range(1 , i + 1):
        print(j, end = "")
    print()

for k in range(num - 1 , 0 , -1):
   l = 1
   while True:
       print(l, end="")
       l += 1
       if l > k:
           print()
           break
print()