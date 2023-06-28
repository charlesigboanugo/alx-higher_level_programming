#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as va_err:
        print("Exception: {}".format(va_err), file=sys.stderr)
        return False
    except TypeError as ty_err:
        print("Exception: {}".format(ty_err), file=sys.stderr)
        return False
    return True
