print("Welcome to 'How many seconds are in a year?' '")
print()
print("I will ask you for a year then will tell you how many seconds that year has or had.")
print()

def endGame():
  while True:
    x = input()
    print()
    print("The game has ended, thank you for participating.")
    print()
    print("To play again click Stop on top right page and click Run")
    continue




def getYear():
  while True:
    try:
      year = int(input("Please enter year?: "))
      print()
    except ValueError:
      print()
      print("I am expecting positive numbers.")
      print()
      continue
    if year < 0:
      print()
      print("Year cannot be negative.")
      print()
      continue
    else:
      return year

      
def checkIfLeapYr(year):
  # divided by 100 means century year (ending with 00)
  # century year divided by 400 is leap year
  if (year % 400 == 0) and (year % 100 == 0):
      print("{0} is a leap year".format(year))
      return True
  
  # not divided by 100 means not a century year
  # year divided by 4 is a leap year
  elif (year % 4 ==0) and (year % 100 != 0):
      print("{0} is a leap year".format(year))
      return True
  # if not divided by both 400 (century year) and 4 (not century year)
  # year is not leap year
  else:
      print("{0} is not a leap year".format(year))
      return False



def getSecsInYr():
  if checkYear is True:
    secInYear = 366 * 24 * 60 * 60
    print()
    print("Therefore", year, "has", secInYear, "seconds")
  else:
    secInYear = 365 * 24 * 60 * 60
    print()
    print("Therefore", year, "has", secInYear, "seconds")

year = getYear()
checkYear = checkIfLeapYr(year)
getSecsInYr()
endGame()