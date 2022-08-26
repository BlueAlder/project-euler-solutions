#!/usr/bin/env python3
import random
# Challenge 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# I disliked this problem
# There is better way to do this, without having to calculate the word in each number, but sack

def main():
  # numberToEnglish(1000)
  count = 0
  for i in range(1, 1000 + 1):
    string = numberToEnglish(i)
    string = string.replace(" ", "")
    print(string, len(string))
    count += len(string)

  print(count)
# 
def numberToEnglish(number):
  assert number < 10000 and number > 0, "Number out of range"

  str_num = str(number).zfill(4)
  thousands = int(str_num[0])
  hundreds = int(str_num[1])
  tens = int(str_num[2])
  ones = int(str_num[3])

  final = ""
  # Get Thousands
  if thousands > 0:
    final += digitToWord(thousands) + "thousand"
    

  # Get Hundreds
  if hundreds > 0:
    final += digitToWord(hundreds) + "hundred"
    if (tens + ones > 0 ):
      final += "and"

  # Get 10s 
  if tens > 0:
    if tens == 1 and ones > 0:
      tens = 10 + ones
      ones = 0
      final += digitToWord(tens)
    else:
      final += tensToWord(tens)

  # Gets 1s 
  if ones > 0:
    final += digitToWord(ones)

  return final

def digitToWord(digit):
  if digit == 1:
    return "one"
  if digit == 2:
    return "two"
  if digit == 3:
    return "three"
  if digit == 4:
    return "four"
  if digit == 5:
    return "five"
  if digit == 6:
    return "six"
  if digit == 7:
    return "seven"
  if digit == 8:
    return "eight"
  if digit == 9:
    return "nine"
  if digit == 10:
    return "ten"
  if digit == 11:
    return "eleven"
  if digit == 12:
    return "twelve"
  if digit == 13:
    return "thirteen"
  if digit == 14:
    return "fourteen"
  if digit == 15:
    return "fifteen"
  if digit == 16:
    return "sixteen"
  if digit == 17:
    return "seventeen"
  if digit == 18:
    return "eighteen"
  if digit == 19:
    return "nineteen"
  if digit == 0:
    return "zero"

def tensToWord(ten):
  if ten == 1:
    return "ten"
  if ten == 2:
    return "twenty"
  if ten == 3:
    return "thirty"
  if ten == 4:
    return "forty"
  if ten == 5:
    return "fifty"
  if ten == 6:
    return "sixty"
  if ten == 7:
    return "seventy"
  if ten == 8:
    return "eighty"
  if ten == 9:
    return "ninety"
  
if __name__ == "__main__":
  main()

