staff =[("sujal",16),("vivek",15),("vansh" ,12),("vasu",10),("vinay",9)]

for name ,age in staff:
    if  age >=18:
        print(F"{name,age} is eligible for voting")
        break
    else:
        print(F"{name,age} is not eligible for voting")