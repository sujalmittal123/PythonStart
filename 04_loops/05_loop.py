# You're preparing an order summary with customer names and their total bill.
# Task:
# Use two lists: one for names and one for bills.
# Print: "[Name] paid [amount]"


names = ["sujal", "vivek","vansh","vasu","vinay"]
bills = [ 100,200,300,400,500]

for name,amount in zip(names,bills):# zip add two list in one
    print(f"hello {name}, your bill amount is ₹{amount}")