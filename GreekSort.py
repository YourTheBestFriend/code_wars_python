def greek_comparator(lhs, rhs):
    print(lhs, ' ', rhs)
    if len(lhs) > len(rhs):
        return '< 0'
    elif (len(lhs) < len(rhs)):
          return '> 0'
    else:    
        return 0