# Some pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# Associated Prices
prices = [2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2) 
num_pizzas = len(toppings)

print("We sell {} different kinds of pizza!".format(num_pizzas))

pizza_and_prices = list(zip(prices, toppings))
pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[len(pizza_and_prices)-1]