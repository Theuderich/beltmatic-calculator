#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import math
from settings import NumbersRevealedOnMap


def parse_command_line_arguments():
    """
    Parses command line arguments.
    """

    parser = argparse.ArgumentParser(description="Find equation")
    parser.add_argument("number", type=int, help="The number to analyze")
    args = parser.parse_args()
    return args.number


def is_number_dividable(number, divisor):
    """
    Checks if a number is divisible by a divisor.
    """
    return number % divisor == 0


def find_largest_divisor_from_list(number, divisors):
    """
    Finds the largest divisor of a number from a list of divisors.
    """
    for divisor in sorted(divisors, reverse=True):
        if is_number_dividable(number, divisor):
            return divisor
    return None

def find_division(dividend, divisors):
    divisors_found = []
    while(True):
        divisor = find_largest_divisor_from_list(dividend, divisors)
        if( divisor is None):
            break
        divisors.remove(divisor)
        divisors_found.append(divisor)
    divisors_found.remove(1)
    return divisors_found


def find_equation(number):
    """
    
    """
    print(f"\n\nFinding equation for {number}...\n\n")
    
    divisors_available = NumbersRevealedOnMap.available_numbers.copy()
    divisors_possible = find_division(number, divisors_available)
    print(f"divisors_possible1: {divisors_possible}")
    for divisor in divisors_possible:
        quotient = int(number / divisor)
        print(f"quotient: {quotient}, divisor: {divisor}")
        if quotient in NumbersRevealedOnMap.available_numbers:
            return f"{divisor} * {quotient}"
        else:
            equation_segment = find_equation(quotient)
            return(f"{divisor} * ({equation_segment})")

    divisors_available = list(range(1, int(math.sqrt(number)) + 1))
    divisors_possible = find_division(number, divisors_available)
    print(f"divisors_possible2: {divisors_possible}")
    for divisor in divisors_possible:
        quotient = int(number / divisor)
        first_equation_segment = f"{divisor}"
        if divisor not in NumbersRevealedOnMap.available_numbers:
            first_equation_segment = find_equation(divisor)
        second_equation_segment = f"{quotient}"
        if quotient not in NumbersRevealedOnMap.available_numbers:
            second_equation_segment = find_equation(quotient)
        print(f"quotient: {quotient}, divisor: {divisor}")
        return f"({first_equation_segment}) * ({second_equation_segment})"

    minuend = number
    for subtrahend in sorted(NumbersRevealedOnMap.available_numbers, reverse=True):
        if subtrahend >= number:
            continue
        difference = minuend - subtrahend
        print(f"difference: {difference}, subtrahend: {subtrahend}")
        if difference in NumbersRevealedOnMap.available_numbers:
            return f"{subtrahend} + {difference}"
        else:
            equation_segment = find_equation(difference)
            return f"{subtrahend} + ({equation_segment})"

    print(f"Could not find equation for {number}.")
    return None            
    
def main():

    # Parse command line arguments
    number = parse_command_line_arguments()
    if number < 1:
        print("Please enter a positive integer.")
        return

    print("Available numbers on map:", NumbersRevealedOnMap.available_numbers)

    print(f"Found equation: {number} = {find_equation(number)}")

if __name__ == "__main__":
    main()
