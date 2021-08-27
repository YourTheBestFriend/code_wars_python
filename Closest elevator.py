def elevator(left, right, call):
    print(left, ' ', right, ' ', call)
    if left == right: 
        return "right"
    elif (left > right >= call):
        return "right"
    elif (left < right <= call):
        return "right"
    elif (abs(left - call) == abs(right - call)):
        return "right"
    elif (left <= call < right):
        return "left"
    elif (right < left <= call):
        return "left"
    else:
         return "left"