def shortcut( s ):
    # ...
    list_ = ['a','e','i','o','u']
    new_s = ''
    print(s)
    # ...
    for i in s:
        if i not in list_:
            new_s += i   
    return new_s