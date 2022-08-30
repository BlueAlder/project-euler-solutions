#!/usr/bin/env python3

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


# Challenge 19

# 0 = Monday
# 6 = Sunday

def main():
  currentYear = 1901
  currentDay = 0

  occurances = 0

  for year in range(1901, 2001):
    for month in range(1, 13):
      days_in_month = get_month_length(month, year % 4 == 0)
      for day in range(1, days_in_month + 1):
        currentDay = (currentDay +  1) % 7
        # print(year, month, day, currentDay)


        if currentDay == 6 and day == 1:
          occurances += 1 
          print(year, month, day)
  
  print(occurances)

def get_month_length(month, isLeap):
  if month in [1, 3, 5, 7, 8, 10, 12]:
    return 31
  elif month in [4, 6, 9, 11]:
    return 30
  elif month == 2:
    if isLeap:
      return 29
    else:
      return 28

if __name__ == "__main__":
  main()



