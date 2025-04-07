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

# Calculate the change in insurance cost due to age increase
change_in_insurance_cost = new_insurance_cost - insurance_cost

# Print the change in insurance cost due to age increase
print(f"The change in cost of insurance after increasing the age by 4 years is {change_in_insurance_cost} dollars")

# Reset age to original value
age = 28

# BMI Factor: Increase BMI by 3.1 and calculate new insurance cost
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance cost due to BMI increase
change_in_insurance_cost = new_insurance_cost - insurance_cost

# Print the change in insurance cost due to BMI increase
print(f"The change in estimated insurance cost after increasing BMI by 3.1 is {change_in_insurance_cost} dollars")

# Reset BMI to original value
bmi = 26.2

# Male vs. Female Factor: Change sex to male and calculate new insurance cost
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance cost due to sex change
change_in_insurance_cost = new_insurance_cost - insurance_cost

# Print the change in insurance cost due to sex change
print(f"The change in estimated cost for being male instead of female is {change_in_insurance_cost} dollars.")
