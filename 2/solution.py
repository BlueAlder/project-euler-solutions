#!/usr/bin/env python3

# Each new term in the Fibonacci sequence is generated by adding the previous two
#  terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.


fib_index = {
  0: 1,
  1: 2
}

def main():
  MAX_VALUE = 4000000

  sum = 0
  current_fib_index = 0
  while True:
    num = getFibNumber(current_fib_index)
    print(num)
    if num > MAX_VALUE:
      break
    if num % 2 == 0:
      sum += num
    current_fib_index += 1



  print(sum)


def getFibNumber(index):
  if index in fib_index.keys():
    return fib_index[index]
  else:
    val = getFibNumber(index - 1) + getFibNumber(index - 2)
    fib_index[index] = val
    return val



if __name__ == '__main__':
  main()