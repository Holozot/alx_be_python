income = float(input("Enter your monthly income:"))
expenses= float(input("Enter your monthly expenses:"))

#calculate monthly savings
savings = income - expenses
print("Your monthly savings are $",savings)

#calculate annual savings
annual_savings = (savings *12 + (savings* 12 * 0.05))
print("Projected savings after one year, with interest, is: $",annual_savings)
