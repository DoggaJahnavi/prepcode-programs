amount=int(input("enter the amount:"))
balance=int(input("enter the balance"))
if amount<=balance and amount%500==0:
    print("withdrawal is allowed")
else:
    print("withdrawal is not allowed")