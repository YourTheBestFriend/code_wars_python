# Floating point comparison.py
def approx_equals(a, b):
    a = round(a, 4)
    b = round(b, 4)
    print(a, ' ', b)
    if (a == b or (a + 0.001 == b or a - 0.001 == b)) and int(a) == int(b):
        return True
    else:       
        return False
