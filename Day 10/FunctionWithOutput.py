#!/usr/bin/env python3

import argparse


def format_name(firstName, lastName):
    return (f"{firstName.title()} {lastName.title()}")


def main():
    FirstName = input("Enter your name:\t")
    lastName = input("Enter your last name:\t")
    print(format_name(FirstName, lastName))


if __name__ == "__main__":
    main()
