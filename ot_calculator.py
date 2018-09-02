def calculation():
    salary=int(input("What's the salary: "))
    ot_payout=int(input("How much was the OT payout: "))
    hourly_ot=(salary/(4*5*8))*2
    hours_needed=round((ot_payout/hourly_ot),2)
    print("The required hours of work for OT amount of RM"+str(ot_payout)+" is "+str(hours_needed)+" hours.")

while True:
    calculation()
    repeat=input("Do you want to perform another calculation? y/Press Any Key: ")
    if repeat.lower() != "y":
        break
    
