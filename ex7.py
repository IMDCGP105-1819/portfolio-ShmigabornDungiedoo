annual_sallary=float(input("What is your annual sallary?"))
total_cost=float(input("How much does your house cost?"))
r=0.04

savings_percent = float(input("What is your return on investment in decimal?"))
portion_deposit=total_cost*0.2
current_savings=0
portion_saved = (annual_sallary/12)*savings_percent
time=0

while current_savings<=portion_deposit:

    monthly_return=current_savings*r/12
    current_savings = current_savings + portion_saved + monthly_return
    time=time+1


print("Number of months: "+ str(time))
