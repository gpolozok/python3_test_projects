# Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

# function for the cost of ground shipping
def ground_cost(weight):
  if(weight <= 2):
    return weight*1.50 + 20
  elif(weight <= 6):
    return weight*3.00 + 20
  elif(weight <= 10):
    return weight*4.00 + 20
  else:
    return weight*4.75 + 20

# test function for the cost of ground shipping (53.6)
print(ground_cost(8.4))

# premium shipping cost variable
premium_cost = 125.00

# function for the cost of drone shipping
def drone_cost(weight):
  if(weight <= 2):
    return weight*4.50
  elif(weight <= 6):
    return weight*9.00
  elif(weight <= 10):
    return weight*12.00
  else:
    return weight*14.25

# test function for the cost of drone shipping (6.75)
print(drone_cost(1.5))

# function that takes one parameter, weight and prints a statement that tells the user which shipping method is the cheapest and how much it would cost to ship a package of said weight using this method
def cheapest_shipping(weight):
  if (ground_cost(weight) > 125.00) and (drone_cost(weight) > 125.00):
    print("Premium ground shipping is the cheapest for " + str(weight) + " lb and it will cost " + str(premium_cost) + "$")
  elif ground_cost(weight) < drone_cost(weight):
    print("Ground shipping is the cheapest for " + str(weight) + " lb and it will cost " + str(ground_cost(weight)) + "$")
  elif ground_cost(weight) > drone_cost(weight):
    print("Drone shipping is the cheapest for " + str(weight) + " lb and it will cost " + str(drone_cost(weight)) + "$")

# test cheapest_shipping function (ground, premium, drone)
cheapest_shipping(4.8)
cheapest_shipping(41.5)
cheapest_shipping(1.0)
