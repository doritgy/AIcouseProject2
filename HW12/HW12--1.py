

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",\
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron, \
    Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",\
                   "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}
dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman",\
                            "Tom Hardy", "Joseph Gordon-Levitt"}

#a not possible to add Emma Stone because she already exsists in the set
(oscar_winners.add("Emma Watson"))
#print(oscar_winners)
##########################
#b
oscar_winners.clear()
#print(oscar_winners)
###########################
#c
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",\
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
oscar_winners_copy = oscar_winners.copy()
#print(oscar_winners_copy)
#######################
#d
oscar_winners.remove("Meryl Streep")
#print(oscar_winners)
###################
#e no actors in both sets
#print(titanic_actors.intersection(dark_knight_actors))
####################
#f I got False
#print(iron_man_actors.isdisjoint(avengers_actors))
###########################
#g i got a "false" answer
#print(actor_list.issubset(oscar_winners))
###################
#h The answer is False
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",\
                   "Chris Hemsworth", "Jeremy Renner"}
#print(actor_list.issuperset(avengers_actors))
##########################
#i
#print(movie_cast.pop())
#####################
#j
movie_cast.discard("Will Smith")
#print(movie_cast)
#############################
#k
#print(titanic_actors.difference(oscar_winners))
#############################
#l
#print(titanic_actors.symmetric_difference(dark_knight_actors))
#######################
#m
add_s = {"kuki","buki","Leonarde DiCaprio"}
oscar_winners ={"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",\
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
oscar_winners.update(add_s)
#print(oscar_winners)
########################
#n
newSet = titanic_actors.union(dark_knight_actors)
#print(newSet)
############################
#o
#print(dark_knight_actors <= dark_knight_rises_actors)
###########################
#p
print(legendary_actors >= oscar_winners)
#################
#q
#print(avengers_actors - iron_man_actors)
##########################
#r
#print(dark_knight_actors ^ avengers_actors)
##########################
#s
#print(dark_knight_actors | iron_man_actors)
#######################
#t
my_frozen = ([legendary_actors])
print(my_frozen)




