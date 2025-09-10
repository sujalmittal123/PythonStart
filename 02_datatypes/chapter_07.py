#tuples

masala_spices = ("cinnamon","cardamom","ginger","clove","pepper")

(spices1,spices2,spices3,spices4,spices5) = masala_spices

print(f" main masala spices are {spices1},{spices2},{spices3},{spices4},{spices5}")

ginger_ratio ,cardmon_ratio =2,1
print(f"the ginger ratio{ginger_ratio} and the carmon ratio {cardmon_ratio}")

ginger_ratio ,cardmon_ratio =cardmon_ratio,ginger_ratio
print(f"the ginger ratio{ginger_ratio} and the carmon ratio {cardmon_ratio}")#swapping the values

# membership list

print(f" is ginger in masala spices? {'ginger' in masala_spices}")