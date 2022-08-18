from bin_subtraction import bin_sub
from binary_to_decimal import bin_dec
from decimal_to_binary import dec_bin

def bin_div(dividend, divisor):
    current = ''
    previous = ''
    quotient = ''

    if bin_dec(dividend) < bin_dec(divisor):
        return('error')

    for bit in dividend:
        previous += bit
        max_length = max(len(previous), len(divisor))
        previous, divisor = [previous.zfill(max_length), divisor.zfill(max_length)]

        if divisor <= previous:
            quotient += '1'
            current = divisor
        else:
            quotient += '0'
            current = '0'
        previous = bin_sub(previous, current)

    remainder = dec_bin(bin_dec(dividend) % bin_dec(divisor))
    quotient_list = []
    remainder_list = []
    quo_fin = ''
    rem_fin = ''

    if bin_dec(quotient):
        for i in quotient:
            quotient_list.append(i)
        while quotient_list[0] == '0' and quotient_list[1] == '0':
            quotient_list.pop(0)
        for i in quotient_list:
            quo_fin += str(i)

    if bin_dec(remainder):
        for i in remainder:
            remainder_list.append(i)
        while remainder_list[0] == '0' and remainder_list[1] == '0':
            remainder_list.pop(0)
        for i in remainder_list:
            rem_fin += str(i)
    else:
        rem_fin = 0

    return f'{quo_fin} r {rem_fin}'