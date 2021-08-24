def array_madness(a,b):
    sum_a = 0
    sum_b = 0
    for i in a:
        sum_a += i**2
    for i in b:
        sum_b += i**2
    #print(sum_a, '>', sum_b, ' = ', sum_a > sum_b)
    return sum_a > sum_b if True else False