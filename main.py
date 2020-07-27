#Function that takes name, birthmonth, birthdate and birthyear
#Have function keep the data of Pi Day
#Say how far away their birthdate pi day in days
#Birthday - pi day = amount of days away
Monthdays = [0,31,59,90,120,151,181,212,243,273,304,334,365]
day = int(input('>>num 1-31: '))
Month = str(input('>>Month of birth(first 3 letters of month): '))

if (Month == 'Jan'):
  print(Monthdays[0]+day)
  print()
if (Month == 'Feb'):
  print(Monthdays[1]+day)
if (Month == 'Mar'):
  print(Monthdays[2]+day)
if (Month == 'Apr'):
  print(Monthdays[3]+day)
if (Month == 'May'):
  print(Monthdays[4]+day)
if (Month == 'Jun'):
  print(Monthdays[5]+day)
if (Month == 'Jul'):
  print(Monthdays[6]+day)
if (Month == 'Aug'):
  print(Monthdays[7]+day)
if (Month == 'Sep'):
  print(Monthdays[8]+day)
if (Month == 'Oct'):
  print(Monthdays[9]+day)
if (Month == 'Nov'):
  print(Monthdays[10]+day)
if (Month == 'Dec'):
  print(Monthdays[11]+day)

