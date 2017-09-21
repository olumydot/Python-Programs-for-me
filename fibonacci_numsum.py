
def sumfib(n):
    n = int(n)
    a = 1  # initial value in loop
    b = 2  # initial value within loop
    c = a + b  # initializes the loop
    d = 2  # initialize d within loop
    e = 1
    sum_of = 0
    print(a)
    print(b)
    while c < n:
        c = a + b
        a = b
        b = c
        print(c)
        sum_of += c
        if c % 2 == 0:
            d += c
        elif c % 2 == 1:
           e += c

    print("\nFinal sum of first {} fibonacci numbers is {} ".format(n, sum_of+3))
    print("Final sum of first {} even fibonacci numbers  is {}".format(n, d))
    print("Final sum of first {} odd fibonacci numbers is {}".format(n, e))




n = input("input an integer value greater than or equal to 3:  ")
sumfib(n)