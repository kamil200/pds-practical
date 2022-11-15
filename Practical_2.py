amount=int(input("Enter amount:"))
discount=0
if amount<1000:
    discount=0.05
elif amount>1000:
    discount=0.1

dis=discount*amount
newAmount=amount-dis
print(newAmount)

