from binary_to_decimal import bin_dec

def bin_hex(bin_num):
    num = bin_dec(str(bin_num))
    hex_dict = {
        0:'0',
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'
    }
    hex_num = ''
    rev_hex = ''

    while True:
        if num < 16:
            rev_hex += hex_dict[num]
            break
        else:
            rev_hex += hex_dict[num % 16]
            num = num // 16
            continue
        
    hex_num = rev_hex[::-1]
    return hex_num