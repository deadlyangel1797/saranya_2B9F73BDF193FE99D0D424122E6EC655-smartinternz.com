# program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.
input__year = int(input("Enter the year to be checked: "))
if (input__year % 400 == 0):
  print("%d is a leap year" % input__year)
elif (input__year % 100 == 0):
  print("%d is not a leap year" % input__year)
elif (input__year % 4 == 0):
  print("%d is a leap year" % input__year)
else:
  print("%d is not a leap year" % input__year)
