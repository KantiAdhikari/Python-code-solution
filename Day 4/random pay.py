# To find out who's paying
import random
nameAsCsv=input("Give me everybody's names, seperated by comma.\n")
names=nameAsCsv.split(", ")

num_items=len(names)
random_choice=random.randint(0, num_items-1)
person_who_will_pay=names[random_choice]
print(person_who_will_pay+" is going to buy meal today!  ")
