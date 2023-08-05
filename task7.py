""" The bakery sells bread at $3.49 per loaf. There's a 60% discount on yesterday's bread. 
Write a program that prompts the user for the quantity of yesterday's purchased bread.
The output should include the regular price per loaf, the price with the 60% discount,
and the total cost for the purchased bread. 
All values should be displayed on separate lines with corresponding descriptions."""

quantity = int(input('Enter the quantity of yesterday\'s purchased bread: '))
price = 3.49
discount = 0.60
discount_bread = float(price - price * discount)
total_sum = float(discount_bread * quantity)
print(f'Price per loaf of bread (without discount): ${price}')
print(f'Price per loaf of bread (with 60% discount): ${round(discount_bread, 3)}')
print(f'Total cost for {quantity} loaves of bread with 60% discount: ${round(total_sum, 3)}')
