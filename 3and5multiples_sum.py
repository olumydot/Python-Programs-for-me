# simple problem on projecteuler.com to sum multiples of 3 and 5 for 0 <= number < 1000

# using list comprehension

multiples = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]

# more explicitly

# for x in range(1000):
#     if x % 3 == 0 or x % 5 == 0:
#         multiples.append(x)

print(sum(multiples))

