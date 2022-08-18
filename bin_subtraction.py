from binary_to_decimal import bin_dec

def bin_sub(num1, num2):
    num1_list = []
    num2_list = []
    temp_diff = 0
    difference = ''

    if bin_dec(num1) < bin_dec(num2):
        return('error')

    max_len = max(len(num1), len(num2))
    num1, num2 = [num1.zfill(max_len), num2.zfill(max_len)]
    
    for i in num1[::-1]:
        num1_list.append(int(i))
    for x in num2[::-1]:
        num2_list.append(int(x))
    
    for ind, bit in enumerate(num1_list):
        temp_diff = num1_list[ind] - num2_list[ind]
        if temp_diff >= 0:
            difference += str(temp_diff)
        elif temp_diff < 0:
            for l in range(ind, max_len):
                if num1_list[l] == 1:
                    num1_list[l] = 0
                    temp_diff = 1
                    difference += str(temp_diff)
                    break
                else:
                    num1_list[l] = 1
        
    return(difference[::-1])