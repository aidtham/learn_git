def dec_bin(num):
    num_list = [0, 0, 0, 0, 0, 0, 0, 0]
    num_str = ''
    max_num = 1
    times = 0

    while max_num * 2 - 1 < num:
        max_num *= 2
        times += 1
        if max_num > 128:
            num_list.append(0)
    
    while True:
        if num >= max_num:
            num_list[-times - 1] = 1
            times -= 1
            num -= max_num
            max_num /= 2
            continue
        elif num > 0:
            times -= 1
            max_num /= 2
            continue
        else:
            break
    
    for i in num_list:
        num_str += str(i)

    return num_str