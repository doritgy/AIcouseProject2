
def my_ascending(x:int = 0, y:int = 0) -> None:
    """the function gets two integer parameters
    and prints them in ascending order, the function returns None"""
    print((x , y) if x <= y else (y , x))

def my_details(a:str = "") -> None:
    """the function gets a string and prints
     the first letter, the letter in the middle and the last letter
     the function returns None"""
    print(a[1], a[len(a) // 2], a[-1])

def say_bool(a:bool = False) -> None:
    """the function recieves a bool variant and print yes or no according to it's value"""
    print("yes" if a else "no")

def print_zugi(a:list[int] = []) -> None:
    """the function recieves a list of integers and prints odd or even """

    for b in a:
        """if b % 2:
            print(b, "odd")
        else:
            print(b, "even")"""
    b = ["odd" if a[i] %2 else "even" for i in range(len(a))]
    print(b)

def my_statistics(grades:list[int] = []) -> None:
    """the function recieves a list of grades and prints various statistics"""
    import statistics
    countFail:int = 0
    countExcelent:int = 0
    countDiff:float = 0
    avrCountDiff:float = 0
    avegerage:float = statistics.mean(grades)
    for a in grades:
        countFail += 1 if a < 55 else 0
        countExcelent += 1 if a > 90 else 0
        countDiff += (a - avegerage) ** 2 ## how far is every grade from the average? sum the distance

    avgCountDiff = countDiff / len(grades) ## average of the distances
    sd = avgCountDiff ** 0.5 ## sd is the standart deviation

    print("lowest grade:", min(grades), "highest:", max(grades), "average:", statistics.mean(grades), "no of grades:",len(grades))
    print("number of failures:", countFail, "numbers of excelents:", countExcelent)
    print(f"standart deviation:  {sd: .2f}")





def main():
    my_statistics([5, 10, 90, 100])

if __name__ == "__main__":
    main()



