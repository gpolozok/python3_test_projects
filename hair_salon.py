# Data analytics in the hair salon

# initial data
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# total price of all haircuts
total_price = 0
for price in prices:
  total_price += price

# average price of a haircut
average_price = total_price / len(prices)
print('Average Haircut Price: ' + str(average_price))

# cut all prices by 5 dollars
new_prices = [price - 5 for price in prices]
print(new_prices)

# calculating total revenue
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total Revenue: ' + str(total_revenue))

# average daily revenue
average_daily_revenue = total_revenue / 7
print('Average Daily Revenue: ' + str(average_daily_revenue))

# haircuts that are under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)
