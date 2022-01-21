def logical_calc(array, op):
    print(array,' ', op)
    flag = False
    g = 0
    for i in range(1, len(array)):
        if op == 'AND':
            flag = array[g] and array[i]
        elif(op == 'OR'):
            flag = array[g] or array[i]
        elif(op == 'XOR'):
            flag = array[g] ^ array[i]
        else:
            pass
        g += 1
    return flag