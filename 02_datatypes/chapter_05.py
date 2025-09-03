import sys
from fractions import Fraction # this pakage import the fraction part in python
from decimal import Decimal # this help us to import the decimal pakage 

ideal_temp =95
current_temp = 5

print(f" the ideal temp is {ideal_temp}")
print(f" the current  temp is {current_temp}")
print(f" the actual temp is  {current_temp - ideal_temp}")
print(f"the frction part is {float(Fraction(current_temp,ideal_temp))}")
