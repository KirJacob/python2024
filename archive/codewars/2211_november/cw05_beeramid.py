def beeramid(bonus, price):
    beers, all_price, index = 0, 0, 0
    if bonus < price:
        return 0
    while (all_price <= bonus):
        index = index + 1
        beers = beers + index * index
        all_price = beers * price
    return index - 1
