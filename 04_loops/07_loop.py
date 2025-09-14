flavours = ["chocolate", "out of stock", "strawberry", "banana", "discontined", "vanilla", "chocolate"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    elif flavour == "discontined":
        break
    print(f"{flavour} is available")

    
print(f"{flavour}")

    