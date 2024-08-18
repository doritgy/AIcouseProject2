import statistics
#a
my_tuple:tuple[int] = (99,)
#########################
#b
my_tuple:tuple[int] = (77,88,99)
############################
#c
def len_tuple(t:tuple[any]) -> int:
    return(len(t))
#################################
#d
def add_tuple(t1:tuple[any], t2:tuple[any]) -> tuple:
    return t1 + t2
#############################
#e
def shared_tuple(t1:tuple[any], t2:tuple[any])-> tuple:
    return tuple(a for a in t1 if a in  t2)
####################################
#f
def not_shared_tuple(t1:tuple[any], t2:tuple[any])-> tuple:
    return tuple(a for a in t1 + t2 if a not in shared_tuple(t1, t2))
#########################
#g
def item_in_index(t:tuple[any], index:int):
    try:
        return t[index - 1]
    except Exception as e:
        return None
##############################
#h
def reverse_tuple(t:tuple[any]) -> tuple:
    return(sorted(t, reverse = True))
######################
#i
def count_multiples(t:tuple[int], n:int) -> int:
    return sum(t.count(i) for i in tuple(j for j in range(1, n + 1) if n % j == 0))
####################################
#j
def multiple_tuple(t:tuple[any], i:int) -> tuple:
    return(tuple(t * i))
###############################
#k
def index_and_tuple(t:tuple[any]) -> tuple:
    #return tuple((t.index(a), a) for a in t)
    return tuple((a, b) for (a, b)  in enumerate(t))
##################################
#l
def statistic_tuple(t:tuple[int]) -> dict:
    return(dict([("max", max(t)), ("min", min(t)), ("mean", statistics.mean(t)), ("len", len(t)),
            ("reversal", tuple(sorted(t, reverse = True))), ("sorted", tuple(sorted(t)))]))
    #return dict([["max", max(t)], ["min", min(t)], ["mean", statistics.mean(t)], ["len", len(t)],
                 #["reversal", tuple(sorted(t, reverse=True))], ["sorted", tuple(sorted(t))],
                 #[[item, t.count(item)] for item in t]])
    #didn't succeed with the bonus
##################################
#m
def create_word(t:tuple[str]) ->str:
    return ''.join(t)
##############################
#n
def create_tuple(myStr:str) -> tuple:
    return tuple(myStr[i] for i in range(len(myStr)))
############################
#o
def minus_number(t:tuple[int], n:int):
    return tuple(tu for tu in t if tu != n )
##########################
#p
def no_dup(t:tuple[any]) -> tuple:
    return tuple(a for a in list(a for a in t) if t.count(a) < 2)
############################
#q
def index_count(t:tuple[int], n:int) -> tuple:
    return tuple(i for  i in range(len(t)) if t[i] == n)
##########################
#r
def our_zip() -> tuple:
    name_list:list[str] = []
    grade_list:list[int] = []
    name:str = ""
    grade:int = 0
    while True:
        name = input("please enter a name")
        if name == "done":
            break
        name_list.append(name)

    while True:
        grade = int(input("please enter a grade"))
        if grade == (-999):
            break
        grade_list.append(grade)

    return tuple(zip(name_list, grade_list))


    #zugi_dict = {item: item ** 2 for item in list1 if item % 2 == 0}






def main():
    print("statistic_tuple", statistic_tuple((1, 3, 5, 5, 7, 100, 100)))

if __name__ == "__main__":
    main()


