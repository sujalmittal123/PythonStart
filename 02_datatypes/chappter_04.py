is_water_boiling = True
water_boil =5
total_action =is_water_boiling + water_boil # upcasting
print(f"total action {total_action}")

is_milk =0
print(F"is any milk there in cup? {bool(is_milk)}")

is_water_hot =True
is_tea_added =False
tea_ready =is_water_boiling and is_tea_added
print(f"can we serve tea {tea_ready}")