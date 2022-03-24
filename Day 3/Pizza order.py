#  Program to order pizza and calculate the total cost.
print("Welcome to the python pizza deliveries!")
size=input("What size pizza do you want ? S, M or L ")

bill=0
if size=="S":
 bill+=100
 print("Price of small size pizza is Rs 100.")
elif size=="M":
 bill+=200
 print("Price of medium size pizza is Rs 200.")
else:
 bill+=300
 print("Price of large size pizza is Rs 300.")

add_pepperoni=input("Do you want pepperoni? Y or N. ")
if add_pepperoni=="Y":
 if size=="S":
   bill+=200
   print("Price of small size pizza with pepperoni is 200. ")
 else:
   bill+=300
   print("Price of medium and large size pizza with pepperoni is Rs 300.")

extra_cheese=input("Do you want extra cheese? Y or N. ")
if extra_cheese=="Y":
  bill+=100
  print("Price of extra cheese is Rs 100")
print(f"Your total bill is {bill}.") 



