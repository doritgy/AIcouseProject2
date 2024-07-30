import statistics

def my_average(a:int = 0, b:int = 0) -> float:
    """the function recieves 2 integers and returns a float of the average"""
    myList:list[int] = (a, b)
    return(statistics.mean(myList))

def my_headline(s:str = "") -> str:
    """the function recieves a string and returns the string with capital letters in words' beginning"""
    return(s.title()+"!")

def concat_list(list1:list[int], list2:list[int], list3:list[int]):
    """the function recieves 3 lists and joins them together, returns the joined list"""
    res = []
    res.extend(list1)
    res.extend(list2)
    res.extend(list3)
    return(res)

def say_bool(a:bool = False) -> str:
    """the function recieves a boolean and returns a string of yes/no according to the variable"""
    return("yes" if a else "no")

def print_zugi(a:list[int] = []) -> list[str]:
    """the function recieves a list of integers and returns odd or even """

    for b in a:
        """if b % 2:
            print(b, "odd")
        else:
            print(b, "even")"""
    list_b:list[str] = ["odd" if a[i] %2 else "even" for i in range(len(a))]
    return(list_b)

def get_int(a:str = "") -> int:
    """the function recieves a string, which she exhibits while an input action of an integer"""
    number:int = 0
    while True:
        try:
            number = int(input(a))
            return(number)
            # if type(number) == "int":
            #     return(number)
            # else:
            #     print("you have to enter an int")
            #     continue
        except Exception as e:
            print("an error occurd", e)
            continue






