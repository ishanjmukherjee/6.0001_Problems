annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
monthly_salary = annual_salary / 12

r = 0.04
portion_down_payment = 0.25 * total_cost
current_savings = 0

months = 0

while current_savings < portion_down_payment:
    current_savings += monthly_salary * portion_saved + current_savings * r / 12
    months += 1
    
print("Number of months:", months)
