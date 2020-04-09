# Organize some of sales data in Len’s Slice pizzeria

#  track of the kinds of pizzas are selling
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# price list
prices = [2, 6, 1, 3, 2, 7, 2]

# toppings length
num_pizzas = len(toppings)
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

# combine pizzas with their prices
pizzas = list(zip(prices, toppings))
print(pizzas)

# sort pizzas so that the pizzas with the lowest prices are at the start of the list
pizzas.sort()

# the cheapist pizza
cheapest_pizza = pizzas[0]

# the MOST EXPENSIVE pizza!
priciest_pizza = pizzas[-1]

# three lowest cost pizzas
three_cheapest = pizzas[0:3]
print(three_cheapest)

# count the number of occurrences of 2 in the prices list
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
