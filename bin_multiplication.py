import bin_addition

def bin_mult(num1, num2):
    num1_list = []
    num2_list = []
    prod_sum = ''
    final_str = ''
    unit = 0
    is_short = False
    index = 0
    rev_num1 = ''
    rev_num2 = ''
    max_len = max(len(num1), len(num2))

    for k in num1[::-1]:
        rev_num1 += k
    
    for m in num2[::-1]:
        rev_num2 += m
    
    if len(rev_num1) < max_len:
        for _ in range(max_len - len(rev_num1)):
            rev_num1 += '0'

    if len(rev_num2) < max_len:
        for _ in range(max_len - len(rev_num2)):
            rev_num2 += '0'

    for i in range(max_len):
        num1_list.append(int(rev_num1[i]))
        num2_list.append(int(rev_num2[i]))
    
    for val in num2_list:
        temp_str = ''
        rev_temp = ''
        for s in range(unit):
            temp_str += (str(0))
        for l in num1_list:
            temp_str += str(val * l)
        for z in temp_str[ : :-1]:
            rev_temp += z
        prod_sum = bin_addition.bin_add(prod_sum, rev_temp)
        unit += 1

    while True:
        if is_short == False:
            for ind, val in enumerate(prod_sum):
                if val == '0' and not prod_sum[ind + 1] == '1':
                    pass
                else:
                    index = ind
                    is_short = True
                    break
        else:
            for x in range(index, len(prod_sum)):
                final_str += str(prod_sum[x])
            break

    return final_str