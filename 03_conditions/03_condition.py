# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.
# Task:
# Input: "small", "medium", "large"
# Small → 10, Medium → ₹15, Large → 20
# If invalid: show "Unknown cup size"

tea_size = input("Enter cup size (small, medium, large): ").lower()
if tea_size == "small":
    print("price of tea is ₹10")
elif tea_size == "medium":
    print("price of tea is ₹15")
elif tea_size == "large":
    print("price of tea is ₹20")
else:
    print("Unknown cup size")