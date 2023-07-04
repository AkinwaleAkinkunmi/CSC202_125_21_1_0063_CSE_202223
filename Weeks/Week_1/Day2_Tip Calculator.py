print("Welcome to the tip calculator.")
total_bill = float(input("What is the total bill?  "))

percent = int(input("What percentage tip would you like to give? 10, 12 , or 15?  "))
people = int(input("How many people are splitting the bill? "))

percent_tip = 1 + (percent/100)

percent_of_total = total_bill * percent_tip

each_tip_value = percent_of_total / people

app_each_tip_value = round(each_tip_value, 2)

print(f"Each person should pay {app_each_tip_value} dollars.")