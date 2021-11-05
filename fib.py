import numpy as np
import time

def calc_n_fib(n):
    fib_numbers = np.array([1,1])
    print(fib_numbers)
    for i in range(2, n):
        fib_i = fib_numbers[i-1] + fib_numbers[i-2]
        print(fib_i)
        fib_numbers = np.append(fib_numbers, fib_i)
    print(f"Fibonacci number at n: {fib_numbers[n-1]}")

def calc_n_fib_recursive(n):
    if(n == 1 or n == 2):
        result = 1
    else:
        result = calc_n_fib_recursive(n-1) + calc_n_fib_recursive(n-2)
        print(result)
    return result

mode = ""
while mode != "q":
    mode = input("Modes\n\t1. Loop\n\t2. Recursive\n\tQ\\q. Quit\nEnter mode: ")
    if(mode == "1"):
        n = input("Loop\n\tEnter fibonacci number you want to calc: ")
        start = time.time()
        calc_n_fib(int(n))
        print(f"\tThat took {time.time() - start}")
    elif(mode == "2"):
        n = input("Recursive\n\tEnter fibonacci number you want to calc: ")
        start = time.time()
        calc_n_fib_recursive(int(n))
        print(f"\tThat took {time.time() - start}")
    elif(mode == "q" or mode == "Q"):
        break
    else:
        print("No clue what you mean mate")


