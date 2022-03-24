# Challenge 1 - To calculate the sum of digit in an integer
twoDigitNum=input('Enter two digit number: ')
firstDigit=twoDigitNum[0]
secondDigit=twoDigitNum[1]
result=int(firstDigit) + int(secondDigit)
print(result)

# Challenge 2 - BMI calculator:
weight=float(input("enter your  body weight in kg: "))
height=float(input("enter your height in m: "))
bmi=weight/height**2
bmi1=int(bmi)
print('Your Body Mass Index(BMI) is: '+ str(bmi1))

# Challenge 3 - Life in weeks
age=input('What is your current age? ')
age_as_int=int(age)
yearsLeft = 90-age_as_int
daysLeft = yearsLeft*365
weeksLeft = yearsLeft*52
monthsLeft = yearsLeft*12
print(f'You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months.')