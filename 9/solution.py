#!/usr/bin/env python3

# Challenge 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Using Euclids formula for finding pythagorean triples
# Where

# a = 2 * m * n
# b = (m * m) - (n * n)
# c = (m * m) + (n * n)

# We can simplify and solve that a + b + c = 1000
# Therefore m(m + n) = 500
# Therefore in finding m and n, m must be a factor of 500 and (m + n) must
# also be a factor

# Factors of 500 are
# 1, 2, 5, 10, 20, 25, 50, 100, 125, 250, 500

# This leaves us with a two options given m > n
# m = 100, n = 25
# m = 20, n = 5
# Trying both yields that m = 20 and n = 5 is the solution.


def main():
  part_sum = 1000

  m = 20
  n = 5

  assert ((part_sum) / 2) % m == 0, "m does not divide n/2"
  assert ((part_sum) / 2) % (m + n) == 0, "m + n does not divide the sum divided by 2"

  a = 2 * m * n
  b = (m * m) - (n * n)
  c = (m * m) + (n * n)

  print("a:", a)
  print("b:", b)
  print("c:", c)

  print("a+b+c:", a+b+c)
  print("abc", a * b * c)

  sum = (a ** 2) + (b ** 2)
  c2 = c ** 2

  print("sum:", sum)
  print("c2:", c2)

if __name__ == "__main__":
  main()

