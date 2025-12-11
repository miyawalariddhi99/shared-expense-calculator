# project- Monthly Shared Expense Splitter

monthly_rent = int(input("Enter the total monthly rent: "))
monthly_food_cost = int(input("Enter the total monthly food/groceries cost: "))
electricity_units_used = int(input("Enter the electricity units consumed: "))
cost_per_unit = int(input("Enter the electricity charge per unit: "))
number_of_persons = int(input("Enter the number of persons sharing the room/flat: "))

total_electricity_cost = electricity_units_used * cost_per_unit
total_monthly_expense = monthly_rent + monthly_food_cost + total_electricity_cost

amount_per_person = total_monthly_expense // number_of_persons

print("Total amount you've to pay is:", amount_per_person)
print("Total amount you've to pay for electricity is:", total_electricity_cost)
