#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse

from settings import NumbersRevealedOnMap


def prime_factorization(n):
    """
    Returns the prime factorization of a given number n.
    """
    if n < 2:
        return []

    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors


def parse_command_line_arguments():
    """
    Parses command line arguments.
    """

    parser = argparse.ArgumentParser(description="Prime Factorization Tool")
    parser.add_argument("number", type=int, help="The number to factorize")
    args = parser.parse_args()
    return args.number


def is_factor_available(factor):
    """
    Checks if a factor is available in the NumbersRevealedOnMap.
    """
    return factor in NumbersRevealedOnMap.available_numbers

def beltmatic_factorization(number):
    """
    Run prime factorization and check if each factor is available.
    In case a factor is not available, an available umber is subtracted
    and the prime factorization is run again for this new term.
    """
    
    #run prime factorization
    factors = prime_factorization(number)
    print("\n===")
    print(f"Prime factorization of {number}: {factors}")

    # Check if each factor is available
    all_factors_available = True
    for factor in factors:
        if is_factor_available(factor):
            print(f"Factor {factor} is available.")
        else:
            print(f"Factor {factor} is not available.")
            for available in NumbersRevealedOnMap.available_numbers:
                new_number = factor - available
                print(f"Checking for ({new_number} + {available}).")
                if beltmatic_factorization(new_number):
                    print("\n")
                    break
    return all_factors_available
            
    

def main():

    # Parse command line arguments
    number = parse_command_line_arguments()
    if number < 1:
        print("Please enter a positive integer.")
        return

    print("Available numbers on map:", NumbersRevealedOnMap.available_numbers)
    print("Calculating prime factorization for %d ...", number)

    beltmatic_factorization(number)
    
if __name__ == "__main__":
    main()
