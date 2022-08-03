#!/usr/bin/env python3

# Challenge 14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def main():
  MAX_VALUE = 1000000

  max_chain_length = 0
  max_seed = 0
  for i in range(1, MAX_VALUE):
    current_number = i
    chain_length = 1
    while current_number != 1:
      current_number = getNextCollatzValue(current_number)
      chain_length += 1
    if chain_length > max_chain_length:
      max_seed = i
      max_chain_length = chain_length
  print("Max Seed:", max_seed)
  print("Chain Length:", max_chain_length)



def getNextCollatzValue(number):
  if number % 2 == 0:
    return number / 2
  else:
    return (3 * number) + 1

if __name__ == "__main__":
  main()

