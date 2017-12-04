# """The program below will simulate a random walk """
import random
# import matplotlib
# import matplotlib.pyplot as plt
# import pdb
#
#
# def random_walk(n):
#     """This function will return the coordinates after random walk over n blocks
#     variable 'n' will represent the number of blocks that will be travelled away from the initial position 0,0"""
#
#     # since this is a grid system we will use the cartesian coordinate system where the initial position will be 0,0
#     # pdb.set_trace()
#     x = 0
#     y = 0
#
#     for i in range(n):
#         directions = ['N', 'S', 'E', 'W']
#         step = random.choice(directions)
#         if step == 'N':
#             y = y + 1
#         elif step == 'S':
#             y = y - 1
#         elif step == 'E':
#             x = x + 1
#         else:
#             x = x - 1
#     return (x, y)
#
#
# for i in range(55):
#     # pdb.set_trace()
#     walks_of_life = random_walk(10)
#     print(walks_of_life, "Distance from home =", abs(walks_of_life[0]) + abs(walks_of_life[1]))
#


# now I wanna make this same application shorter

def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

# using monte carlo method let us sample 1000 random walks
number_of_randwalks = 1000

# the probability to walk home in 30 walkssteps
for walks_home in range(1, 31):
    # the whole idea is that we make it back home in 4 walks or less. That is when the walk is free..
    # if you dont make it home in 4 walks then you will have to pay for the ride back home as its too far
    no_transport = 0  # initial number of walks that are 4 or fewer

    for i in range(number_of_randwalks):
        (x, y) = random_walk(walks_home)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
        # now we compute the percentage of random walks that turned out to get home
    percentage_no_transport = float(no_transport) / number_of_randwalks
    print("walk size", walks_home, "/ % of no transport = ", 100*percentage_no_transport)





# for i in range(55):
#     # pdb.set_trace()
#     walks_of_life = random_walk(10)
#     print(walks_of_life, "Distance from home =", abs(walks_of_life[0]) + abs(walks_of_life[1]))

