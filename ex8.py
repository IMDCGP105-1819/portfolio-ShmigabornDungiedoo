annual_sallary=float(input("What is your annual sallary?"))
total_cost=float(input("How much does your house cost?"))
r=0.04
semi_annual_raise=float(input("What is your semi-annual raise in percent?"))
semi_annual_raise=semi_annual_raise/100

savings_percent = float(input("What is your return on investment in decimal?"))
portion_deposit=total_cost*0.2
current_savings=0
portion_saved = (annual_sallary/12)*savings_percent
time=0

while current_savings<=portion_deposit:
    timeadd=0

    monthly_return=current_savings*r/12
    current_savings = current_savings + portion_saved + monthly_return
    time=time+1
    timeadd+=1
    if timeadd==6:
        annual_sallary+(annual_sallary*semi_annual_raise)




print("Number of months: "+ str(time))
