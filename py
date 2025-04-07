# Create the initial variables for the individual's details
age = 28  # Age of the individual
sex = 0  # 0 for female, 1 for male
bmi = 26.2  # Body Mass Index
num_of_children = 3  # Number of children
smoker = 0  # 0 for non-smoker, 1 for smoker

# Calculate the initial insurance cost using the given formula
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Print the initial insurance cost
print(f"This person's insurance cost is {insurance_cost} dollars")

# Age Factor: Increase age by 4 years and calculate new insurance cost
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
