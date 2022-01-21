def fillable(stock, merch, n):    
    for k, v in stock.items():
        if merch == k:
            if n <= v:
                return True
    return False