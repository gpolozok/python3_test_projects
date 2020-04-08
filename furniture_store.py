# Test project 1. Furniture store called Lovely Loveseats for Neat Suites on Fleet Street.

# First item description
lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''

# First item price
lovely_loveseat_price = 254.00

# Second item description
stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''

# Second item price
stylish_settee_price = 180.50

# Third item description
luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''

# Third item price
luxurious_lamp_price = 52.15

# Tax value
sales_tax = 0.088

# Tally of customer_one expenses
customer_one_total = 0

#  List of the descriptions of things cutomer_one purchasing
customer_one_itemization = ''

# Customer_one purchased Lovely Loveseat
customer_one_total += lovely_loveseat_price

# Tracking items customer_one purchased
customer_one_itemization = lovely_loveseat_description

# Customer_one purchased Luxurious Lamp
customer_one_total += luxurious_lamp_price

# Tracking items customer_one purchased
customer_one_itemization = lovely_loveseat_description + ' ' + luxurious_lamp_description

# Calculate sales tax
customer_one_tax = customer_one_total * sales_tax

# Add sales tax to the customer_one's total cost
customer_one_total += customer_one_tax

# Print cutomer_one receipt
print('Customer One Items:')
print(customer_one_itemization)
print('Customer One Total:')
print(customer_one_total)
