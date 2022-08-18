from decimal_to_binary import dec_bin

def hex_bin(hex_num):
    hex_num = str(hex_num).upper()
    total = 0
    hex_dict = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15 
    }
    hex_num = hex_num[::-1]
    for ind, item in enumerate(hex_num):
        total += hex_dict[item] * 16 ** ind
    bin_num = dec_bin(total)
    
    return bin_num