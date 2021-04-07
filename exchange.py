amount = eval(input(" Enter an amount to make change for: "))
print("\n")
print("Your change is...")
print("")
twenties = amount//20
a = amount%20
print(twenties, "twenties")
#print("The balance from here is: ",a)
tens = a//10
b = a%10
print(tens, "tens")
#print("The balance from here is: ",b)
fives = b//5
c = b%5
print(fives, "fives")
#print(c)
one = c//1
d = c%1
print(one, " ones ")
#print("interms of coins: ")
quater = d//0.25
e = d%0.25
q = round(quater,0)
print(q, " quaters ")
dime = e//0.1
f = e%0.1
print(dime, " Dimes")
nickel = f//0.05
g = f%0.05
print(nickel, " nickels")
penny = g//0.01
print(penny, " pennies")