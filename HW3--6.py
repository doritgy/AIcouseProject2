noOfFriends:int = int(input("how mand friends came to visit Daby"))
noOfPizzas:int = int(input("how many pizzas were ordered"))
noOfPizzaFriend:int
noOfPizzasLeft:int
noOfPizzaFriend = int(noOfPizzas / noOfFriends)
noOfPizzasLeft = noOfPizzas % noOfFriends
print(f"there were {noOfFriends} friends, everyone got {noOfPizzaFriend} pizzas and there were left {noOfPizzasLeft:} pizzas")
