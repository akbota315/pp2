#1
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


#2
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")


#3
i = 1
while i < 6:
  print(i)
  i += 1

#4
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

#5
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  
