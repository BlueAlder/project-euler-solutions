#!/usr/bin/env python3

# Challenge 22

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

def main():
  f = open("p022_names.txt", "r")
  line = f.read()

  names = line.split(',')
  names = list(map(lambda name: name.replace('"', ""), names))
  names = sorted(names)

  total = 0
  for idx, name in enumerate(names):
    score = getNameScore(name) * (idx + 1)
    total += score
  print(total)

def getNameScore(name):
  score = 0
  for char in name:
    score += ord(char) - 64
  return score

if __name__ == "__main__":
  main()

