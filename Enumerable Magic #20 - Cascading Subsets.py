def each_cons(lst, n):
    list_ = []
    for i in range(0, (int(len(lst) / n) + 1)):
        list_.append([])
    index = 0
    flag = 0
    for i in range(0, len(lst)):
        print('i = ', i)
        if index < n:
            index += 1
            list_[flag].append(lst[i])
        elif(index == n):
            list_[flag+1].append(lst[i-1])
        else:
            index = 0 
            flag += 1
    return list_