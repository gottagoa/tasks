# Imagine you weigh 16.5% of your weight on Earth when you're on the Moon. 
# To calculate this, you need to multiply your Earth weight by 0.165. 
# If for the next 15 years, you gain 1 kg each year, 
# how will your weight on the Moon change every year?
# Your task is to receive the user's weight, calculate how their weight on the 
# Moon will change each year, and display the results.

# Example:

# Earth Weight: 60 kg
# 1st year - 9.9 kg
# 2nd year - 10.065 kg
# 3rd year - 10.23 kg
# ...and so on.

weight = float(input('Enter your weight: '))
moon_weight_ratio = 0.165
period_range = 15
weight_moon = weight * 0.165

print(f"Earth Weight: {weight} kg")
print(f"1st year - {round(weight_moon, 2)} kg (Moon Weight)")

for year in range(2, period_range + 1):
    weight += 1
    weight_moon = weight * moon_weight_ratio
    print(f"{year} year - {round(weight_moon, 3)} kg (Moon Weight)")
