print("Welcome to the tip calculator")
bill= float(input("what was the total bill?"))
tip_percent =int(input("how much tip would you like to give? 10, 12, 15?"))
tip = (tip_percent/100)*bill
split = int(input("how many people to split the bill"))
total = bill + tip
last_total = total/split
print(f"Each person should pay: ${last_total: .2f}")
