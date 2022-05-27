#import math
import functools
def sum_digits_numbers(num):
    ones = num%10
    tens = int(num/10)
    return ones + tens
#print(sum_digits_numbers(16))

def credit_check(str):
    cc_arr = list(str)
    cc_arr_int = list(map(lambda x : int(x),cc_arr))
    #print(list(cc_arr_int))
    for i in range(len(cc_arr_int)):
        if i%2 == 0:
            cc_arr_int[i] = cc_arr_int[i]*2
            cc_arr_int[i] = sum_digits_numbers(cc_arr_int[i])
            #print(cc_arr_int[i])
            # cc_arr_int[i]+=cc_arr_int[i]%10
            # cc_arr_int[i]+=int(cc_arr_int[i]/10)
            # print(cc_arr_int[i])
            # print(math.floor(int(cc_arr_int[i])))
    sum = functools.reduce(lambda agg, item: agg + item, cc_arr_int)
   # print(cc_arr_int)
    if sum%10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"

    pass

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

credit_check('5541808923795240')