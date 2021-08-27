def twice_as_old(dad_years_old, son_years_old):
    print(dad_years_old,' ', son_years_old)
    col_years = 0
    while col_years <= 100:
        if (son_years_old != 0 and dad_years_old / son_years_old == 2):
            return col_years
        else:
            col_years += 1
            dad_years_old += 1
            son_years_old += 1
            
            
