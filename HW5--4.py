import random

songs: list[str] = ["uga uga uga", "bamaagal", "berosh hashana"]
songs.append("bambi")
print(songs)
songs.insert(0, "buba yocheved")
print(songs)
print("in songs there are ", len(songs), "songs")
#########################
numbers:list[int] = []
for i in range(10):
    numbers.append(random.randint(1,100))
print(numbers)
##########################
bools:list[bool] = []
bools = [random.choice([True, False]) for _ in range(10)]
print(bools)
#########################
word:str = ""
length:int = random.randint(5,20)
print(f" length of word is: {length}")
for i in range(length):
    word += random.choice(["a", "b", "c"])
print(word)
###########################
lengthOfWords:int = 0
words:list[str] = []
lengthOfWords = random.randint(10, 21)
for j in range(lengthOfWords):
    word:str = ""
    length:int = random.randint(5,20)
    print(f" length of word is: {length}")
    for i in range(length):
        word += random.choice(["a", "b", "c"])
    print(word)
    words.append(word)
print(f"my random list of words is: {words}")



