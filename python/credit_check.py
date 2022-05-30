#import math
import functools

# Helper function to sum digits of 2-digit numbers
def sum_digits_numbers(num):
    ones = num%10
    tens = int(num/10)
    return ones + tens

def credit_check(str):
    cc_arr = list(str)
    cc_arr_int = list(map(lambda x : int(x),cc_arr))

    # Apply Luhn algorithm to credit card number
    for i in range(len(cc_arr_int)):
        if i%2 == 0:
            cc_arr_int[i] = cc_arr_int[i]*2
            cc_arr_int[i] = sum_digits_numbers(cc_arr_int[i])
    sum = functools.reduce(lambda agg, item: agg + item, cc_arr_int)

    # Return message of CC check
    if sum%10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"

# print(credit_check('5541808923795240'))