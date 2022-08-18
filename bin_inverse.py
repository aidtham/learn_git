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
    
    for _ in range(2):
        short_list.pop(0)
    
    for z in short_list[::-1]:
        sum_str += str(z)

    return sum_str

def bin_inv(num):
    inv_str = ''

    for i in num:
        if i == '1':
            inv_str += '0'
        elif i == '0':
            inv_str += '1'
    
    temp_str = bin_add(inv_str, '1')
    
    return temp_str[::-1]