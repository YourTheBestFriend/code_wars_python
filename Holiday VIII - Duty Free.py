def duty_free(price, discount, holiday_cost):
    if (price == 0 or discount == 0 or holiday_cost == 0):
        return 0
    else:
        return int(holiday_cost / price // (discount / 100)) 
    