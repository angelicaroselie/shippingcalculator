print("\n~~~~~~~ Shipping price calculator ~~~~~~~")


#Ground premium value
cost_ground_premium = 125.00
default_ground_cost_multiplier = 1.5
default_ground_cost = 20
default_drone_cost_multiplier = 4

#Input for weight
weight = float(input('\nGive the weight of the package in kilograms: '))

#Shipping cost value calculations for ground shipping and drone shipping
if weight <= 2:
  cost_ground = weight * default_ground_cost_multiplier + default_ground_cost
  cost_drone = weight * default_drone_cost_multiplier
elif weight <= 6:
  cost_ground = weight * (default_ground_cost_multiplier * 2) + default_ground_cost
  cost_drone = weight * (2 * default_drone_cost_multiplier)
elif weight <= 10:
  cost_ground = weight * (default_ground_cost_multiplier * 2.5) + default_ground_cost
  cost_drone = weight * (2.5 * default_drone_cost_multiplier)
else:
  cost_ground = weight * (default_ground_cost_multiplier * 3) + default_ground_cost
  cost_drone = weight * (3 * default_drone_cost_multiplier)


print()

#Printing calculated prices

print(f"Shipping with ground shipping costs: ${cost_ground}", "\n")

print(f"Shipping with ground premium costs: ${cost_ground_premium}", "\n")

print(f"Shipping with drone shipping costs: ${cost_drone}", "\n")