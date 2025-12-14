p=float(input("enter principal amount:"))
r=float(input("enter rate of interest:"))
t=float(input("enter time in years:"))
ci=p*((1+r/100)**t)-p
print("compound interest=",ci)