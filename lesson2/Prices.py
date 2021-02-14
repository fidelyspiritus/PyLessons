prices = [57.8, 432.4, 45.4, 76, 33, 34, 83.42, 25.33, 34.68, 535.34, 1, 66.242, 742, 39, 33.2, 174, 28, 547.95, 46.75]
for price in prices:
    zero = ""
    penny = price % 1 * 100  # можно было бы не вводить отдельную переменную, но так быстрее будет считать.
    if penny < 10: zero = 0
    print(f"{int(price)} руб {zero}{int(penny)} коп", end=", ")
print()
print(sorted(prices))
print(prices)
sort_prices = sorted(prices, reverse=True)
print(sort_prices)
print(sorted(prices)[-5:])
