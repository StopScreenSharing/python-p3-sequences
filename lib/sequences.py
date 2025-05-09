#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [] 
    if length == 0:
        fibonacci_sequence = []
    elif length == 1:
        fibonacci_sequence = [0]
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
    print(fibonacci_sequence)
