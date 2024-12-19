#!/usr/bin/env python3
"""Documentation"""
import sys


def main():
    """ Documentation """
    exit_phrases = {'exit', 'quit', 'goodbye', 'bye'}
    while True:
        user_input = input("Q: ").strip().lower()

        if user_input.lower() in exit_phrases:
            print("A: Goodbye")
            break

        print("A:", user_input)

if __name__ == "__main__":
    main()
