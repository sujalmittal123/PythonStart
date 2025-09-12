
# A local cafe wants a program that suggests a snack. If a customer asks for cookies or samosa, it confirms the order.
# Otherwise, it says it's not available.
# Task:
# Take snack input
# If it's "cookies" or "samosa" confirm the order
# Else, show unavailability

snaks = input("What snack would you like to order? ").lower() # in this  inputhelp us to the value from the user  and lower() convert it into lowercase
if snaks == "cookies" or snaks == "samosa":
    print(f"Order confirmed for {snaks}!")
else:
    print(f"Sorry, we don't have {snaks} available.")   