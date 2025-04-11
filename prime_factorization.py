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


def main():

    # Parse command line arguments
    number = parse_command_line_arguments()
    if number < 1:
        print("Please enter a positive integer.")
        return

    print("Calculating prime factorization for %d ...", number)

    # Example usage
    factors = prime_factorization(number)
    print(f"Prime factorization of {number}: {factors}")

    # Check if each factor is available
    for factor in factors:
        if is_factor_available(factor):
            print(f"Factor {factor} is available.")
        else:
            print(f"Factor {factor} is not available.")

    # Example usage of NumbersRevealedOnMap
    print("Available numbers:", NumbersRevealedOnMap.available_numbers)


if __name__ == "__main__":
    main()
