prices = [1500, 6000, 4999, 12000, 800]
print("Старые цены:", prices)

new_prices = [price * 0.8 if price > 5000 else price for price in prices]
print("Новые цены:", new_prices)