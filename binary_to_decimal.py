def bin_dec(bin_num):
    num_list = []
    temp_list = []
    max_num = 0
    dec_num = 0
    
    for i in bin_num:
        temp_list.append(i)
    for item in temp_list:
        num_list.append(int(item))
        if max_num == 0:
            max_num += 1
        else:
            max_num *= 2

    for val in num_list:
        if val == 1:
            dec_num += max_num
            max_num /= 2
        else:
            max_num /= 2
    dec_num = int(dec_num)
    return dec_num