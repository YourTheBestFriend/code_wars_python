def people_with_age_drink(age):
    if age < 14: return 'drink toddy'
    elif age <= 17: return 'drink coke'
    elif age <= 20: return 'drink beer'
    elif age >= 21: return 'drink whisky'
    else: return 0