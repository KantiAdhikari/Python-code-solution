# Rollercoaster
print("Welcome to the rollercoaster")
height=int(input("What is your height in cm? "))
if height>=120:
  print("You can ride the rollercoaster.")
  age=int(input("What is your age? "))
  bill=0
  if age<12:
    bill=500
    print("Child tickets are Rs500.")
  elif age<=18:
      bill=700
      print("Youth tickets are Rs700.")
  else:
      bill=1200
      print("Adult tickets are Rs1200.")
  want_photo=input("Do you want photo? Y or N. ")
  if want_photo=="Y":
    bill+=300
    print(f"Your total bill is {bill}.")
else:
 print("Sorry, you have to grow taller before you can ride.")

