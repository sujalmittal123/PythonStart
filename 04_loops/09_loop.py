# using dictionary  instead of repeated class

users = [ 
    { "id":1, "total":144,"coupons":"acd123"},
    { "id":2, "total":150,"coupons":"acd126"},
    { "id":3, "total":156,"coupons":"acd129"},
    ]

discounts ={
    "acd123":(0.4,0),
    "acd126":(0.6,0),
    "acd129":(0,20),
}

for user in users:
    percent,flat = discounts.get(user["coupons"],(0,0))
    discount = user["total"]*percent + flat
    print(f"User {user['id']} has a discount of {discount}")
