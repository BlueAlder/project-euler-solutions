#!/usr/bin/env python3

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
  # Approach:
  # Need a function that will check if a number is a palindrome
  # Loop through all 900 3 digit numbers and multiply them together?
  # Save a set of all palindromes and then max it.

  palindromes = set()

  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j
      if isPalindrome(product):
        palindromes.add(product)

  print(max(palindromes))

def isPalindrome(number):
  stringd = str(number)
  first_half = stringd[:len(stringd) // 2]
  second_half = stringd[-(len(stringd) // 2):]
  return first_half == second_half[::-1]

if __name__ == '__main__':
  main()
