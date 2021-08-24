def period_is_late(last,today,cycle_length):
    print(last, ' ', today, ' ', cycle_length)
    if last.month == today.month:
        if (today.day - last.day <= cycle_length):
            return False
        else:
            return True    
    else:
        if last.month == 2:
            if (28 - last.day + today.day < cycle_length):
                return False
            else:
                return True
        else:
            if (30 - last.day + today.day < cycle_length):
                return False
            else:
                return True