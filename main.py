from bin_addition import bin_add
from bin_division import bin_div
from bin_inverse import bin_inv
from bin_multiplication import bin_mult
from bin_subtraction import bin_sub
from bin_to_hex import bin_hex
from hex_to_bin import hex_bin
from binary_to_decimal import bin_dec
from decimal_to_binary import dec_bin

def is_bin(num):
    bin_options = ['1','0']
    valid = True
    for i in num:
        if i not in bin_options:
            valid = False
        else:
            pass
    
    return valid

def is_hex(num):
    hex_options = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    num = num.upper()
    valid = True
    for i in num:
        if i not in hex_options:
            valid = False
        else:
            pass

    return valid

def menu():
    options = ['0','1','2','3','4','5','6','7','8','9']
    while True:
        print("\nWhat would you like to do?")
        print(f"[0] Quit")
        print(f"[1] Convert decimal number to binary.")
        print(f"[2] Convert binary number to decimal.")
        print(f"[3] Add two binary numbers.")
        print(f"[4] Subtract two binary numbers.")
        print(f"[5] Multiply two binary numbers.")
        print(f"[6] Divide two binary numbers.")
        print(f"[7] Find the inverse of a binary number.")
        print(f"[8] Convert binary number into hexadecimal.")
        print(f"[9] Convert hexadecimal number into binary.")
        choice = str(input('\n>>>> '))
        
        
        if choice not in options:
            print('\n<!That is not a valid input!>')
            continue
        
        
        if choice == '0':
            print('\nExited Program.')
            break
        
        
        elif choice == '1':
            print('\n-=-==-==-==-==-==-==-==-==-==-=-')
            print('| Decimal to Binary Conversion |')
            print('-=-==-==-==-==-==-==-==-==-==-=-')
            while True:
                num = input("\nPlease enter the number you wish to convert.\n>>>> ")
                if not num.isnumeric():
                    print("\n<!That is not a valid input!>")
                    continue
                else:
                    num = int(num)
                    print(f'\nDecimal: {num}\n{"Binary:":>8} {dec_bin(num)}')
                    break
        
        
        elif choice == '2':
            print('\n-=-==-==-==-==-==-==-==-==-==-=-')
            print('| Binary to Decimal Conversion |')
            print('-=-==-==-==-==-==-==-==-==-==-=-')
            while True:
                num = input("\nPlease enter the number you wish to convert.\n>>>> ")
                num = str(num)
                if not num.isnumeric():
                    print("\n<!That is not a valid input!>")
                    continue
                if not is_bin(num):
                    print('\n<!The number must be binary!>')
                    continue
                else:                 
                    num = str(num)
                    print(f'\n{"Binary:":>8} {num}\nDecimal: {bin_dec(num)}')
                    break
        
        
        elif choice == '3':
            print('\n-==-==-==-==-==-==-')
            print('| Binary Addition |')
            print('-==-==-==-==-==-==-')
            while True:
                num1 = input("\nPlease enter the first number you would like to add.\n>>>>")
                if not num1.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num1):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    num1 = str(num1)
                    break
            while True:
                num2 = input("\nPlease enter the second number you would like to add.\n>>>>")
                if not num2.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num2):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    num2 = str(num2)
                    break  
            print(f'\n{num1} + {num2} = {bin_add(num1, num2)}')
        
        
        elif choice == '4':
            print('\n-==-==-==-==-==-==-==-')
            print('| Binary Subtraction |')
            print('-==-==-==-==-==-==-==-')
            while True:
                num1 = input("\nPlease enter the number you would like to subtract from.\n>>>>")
                if not num1.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num1):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    num1 = str(num1)
                    break
            while True:
                num2 = input("\nPlease enter the number you would like to subtract.\n>>>>")
                if not num2.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num2):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    num2 = str(num2)
                    if bin_sub(num1, num2) == 'error':
                        print('\n<!Second number cannot be greater that the first!>')
                        continue
                    else:
                        break
            print(f'\n{num1} - {num2} = {bin_sub(num1, num2)}')
        
        
        elif choice == '5':
            print('\n-==-==-==-==-==-==-==-==-')
            print('| Binary Multiplication |')
            print('-==-==-==-==-==-==-==-==-')
            while True:
                num1 = input("\nPlease enter the first number you would like to multiply.\n>>>>")
                if not num1.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num1):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    num1 = str(num1)
                    break
            while True:
                num2 = input("\nPlease enter the second number you would like to multiply.\n>>>>")
                if not num2.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num2):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    num2 = str(num2)
                    break
            print(f'\n{num1} * {num2} = {bin_mult(num1, num2)}')
        
        
        elif choice == '6':
            print('\n-==-==-==-==-==-==-')
            print('| Binary Division |')
            print('-==-==-==-==-==-==-')
            while True:
                num1 = input("\nPlease enter the dividend.\n>>>>")
                if not num1.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num1):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    num1 = str(num1)
                    break
            while True:
                num2 = input("\nPlease enter the divisor.\n>>>>")
                if not num2.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num2):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    num2 = str(num2)
                    if bin_div(num1, num2) == 'error':
                        print('<!Divisor cannot be greater than the dividend!>')
                        continue
                    else:
                        break
            print(f'\n{num1} / {num2} = {bin_div(num1, num2)}')
        
        
        elif choice == '7':
            print('\n-=-==-==--==-==-=-')
            print('| Binary Inverse |')
            print('-=-==-==--==-==-=-')
            while True:
                num = str(input('\nPlease enter the binary number to invert.\n>>>>'))
                if not num.isnumeric():
                    print('\n<!That is not a valid input!>')
                    continue
                elif not is_bin(num):
                    print('\n<!The number must be a binary number!>')
                    continue
                else:
                    print(f'\nOriginal: {num}\n{"Inverse:":>9} {bin_inv(num)}')
                    break
        
        
        elif choice == '8':
            print('\n-==-==-==-==-===-===-==-==-==-==-==-')
            print('| Hexadecimal to Binary Conversion |')
            print('-==-==-==-==-===-===-==-==-==-==-==-')
            while True:
                num = str(input("\nPlease enter the hexadecimal number to convert.\n>>>>"))
                if not is_hex(num):
                    print('\n<!The number must be hexadecimal!>')
                    continue
                else:
                    print(f'\n{"Hex:":>7} {num.upper()}\nBinary: {hex_bin(num)}')
                    break
        
        
        elif choice == '9':
            print('\n-==-==-==-==-===-===-==-==-==-==-==-')
            print('| Binary to Hexadecimal Conversion |')
            print('-==-==-==-==-===-===-==-==-==-==-==-')
            while True:
                num = str(input("\nPlease enter the hexadecimal number to convert.\n>>>>"))
                if not num.isnumeric():
                    print('\n<!That is an invalid input!>')
                elif not is_bin(num):
                    print('\n<!The number must be binary!>')
                    continue
                else:
                    print(f'\nBinary: {num}\n{"Hex:":>7} {bin_hex(num).upper()}')
                    break
            
def main():
    print('\n-==-==-==-==-==-==-==-==-==-==-==-==-')
    print('| Welcome to the Binary Calculator! |')
    print('-==-==-==-==-==-==-==-==-==-==-==-==-')
    menu()

main()