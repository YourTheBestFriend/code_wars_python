def points(games):
    point = 0
    for i in games:
        if int(i[0]) == int(i[2]):
            point += 1
        elif(int(i[0]) > int(i[2])):
             point += 3
        else:
            pass
    return point