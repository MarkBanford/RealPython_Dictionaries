prices = {'apple': 0.5, "orange": 0.35, "banana": 0.25}

# Charge extra 10p per fruit


for key in prices:
    prices[key] = (prices[key] + 0.1).__round__(2)

print(prices)
