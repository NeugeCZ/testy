from os import urandom
import binascii


def abc_random_string(length):
    """Return abc + random string."""
    return ('abc' + str(binascii.hexlify(urandom(length)).decode()))[:length]


def is_prime(number):
    """Return True if *number* is prime."""

    if number < 2 or float(number).is_integer() is False:
        return False

    if float(number).is_integer() is True and isinstance(number, float) is True:
        number = int(number)

    for element in range(2, number):
        if (number % element) == 0:
                return False

    return True


def print_next_prime(number):
        """Print the closest prime number larger than *number*."""

        if isinstance(number, float) is True:
            index = int(number)

        else:
            index = number

        if index < 2:
            return 2

        while True:
            index += 1
            if is_prime(index):
                    print(index)
                    return index
