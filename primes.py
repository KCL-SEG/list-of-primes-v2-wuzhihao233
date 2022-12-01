"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    Num = 2

    if number_of_primes <= 0:
        raise ValueError
    elif not number_of_primes:
        raise ValueError

    while len(list) < number_of_primes:
        prime = True
        for i in range(2, Num):
            if Num % i == 0:
                prime = False

        if prime:
            list.append(Num)
        Num += 1

    return list
