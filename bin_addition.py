def bin_add(num1, num2):
    num1_list = []
    num2_list = []
    sum_list = []
    short_list = []
    sum_str = ''
    sum = 0
    max_len = max(len(num1), len(num2))

    num1, num2 = [num1.zfill(max_len), num2.zfill(max_len)]

    for i in num1[::-1]:
        num1_list.append(int(i))
    for z in num2[::-1]:
        num2_list.append(int(z))
    
    for _ in range(max_len + 2):
        sum_list.append(0)
        num1_list.append(0)
        num2_list.append(0)

    for i in range(max_len + 1):
        sum = num1_list[i] + num2_list[i]
        if sum == 3:
            sum_list[i] = 1
            num1_list[i + 1] += 1
        elif sum == 2:
            sum_list[i] = 0
            num1_list[i + 1] += 1
        else:
            sum_list[i] = sum

    for l in sum_list[::-1]:
        short_list.append(l)
    
    while short_list[0] == 0:
        short_list.pop(0)
    
    for z in short_list:
        sum_str += str(z)

    return sum_str