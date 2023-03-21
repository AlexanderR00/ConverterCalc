# Laboratory_2
# Ritter_Alexander
# Calculator


def main():
    choice = -1
    print("This is a common converter of different systems!")
    while choice !=0:
        print("Select an option:")
        print("1. Decimal to binary")
        print("2. Binary to decimal")
        print("3. Decimal to octal")
        print("4. Octal to decimal")
        print("5. Decimal to hexadecimal")
        print("6. Hexadecimal to decimal")
        print("7. Add binary numbers")
        print("8. Add octal numbers")
        print("9. Add hexadecimal numbers")
        print("10. Subtracting binary numbers")
        print("11. Subtracting octal numbers")
        print("12. Subtracting hexadecimal numbers")
        print("0. Quit\n")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            decimal = float(input("Enter your decimal number: "))
            binary = decimal_to_binary(decimal)
            print(f'Number {decimal} in binary is {binary}')

        elif choice == 2:
            binary = input("Enter a binary number: ")
            decimal = binary_to_decimal(binary)
            print(f"{binary} in decimal is {decimal}")

        elif choice == 3:
            decimal = float(input("Enter a decimal number: "))
            octal = decimal_to_octal(decimal)
            print(f"{decimal} in octal is {octal}")

        elif choice == 4:
            octal = str(input("Enter an octal number: "))
            decimal = octal_to_decimal(octal)
            print(f"{octal} in decimal is {decimal}")

        elif choice == 5:
            decimal = float(input("Enter a decimal number: "))
            hexadecimal = decimal_to_hexadecimal(decimal)
            print(f"{decimal} in hexadecimal is {hexadecimal}")

        elif choice == 6:
            hexadecimal = str(input("Enter a hexadecimal number: "))
            decimal = hexadecimal_to_decimal(hexadecimal)
            print(f"{hexadecimal} in decimal is {decimal}")

        elif choice == 7:
            binary_a = input("Enter first binary number: ")
            binary_b = input("Enter second binary number: ")
            binary_sum = add_binary(binary_a, binary_b)
            print(f"Sum of {binary_a} and {binary_b} is {binary_sum}")

        elif choice == 8:
            octal_a = input("Enter first octal number: ")
            octal_b = input("Enter second octal number: ")
            octal_sum = add_octal(octal_a, octal_b)
            print(f"Sum of {octal_a} and {octal_b} is {octal_sum}")

        elif choice == 9:
            hexadecimal_a = input("Enter first hexadecimal number: ")
            hexadecimal_b = input("Enter second hexadecimal number: ")
            hexadecimal_sum = add_hexadecimal(hexadecimal_a, hexadecimal_b)
            print(f"Sum of {hexadecimal_a} and {hexadecimal_b} is {hexadecimal_sum}")


        elif choice == 10:
            binary_a = input("Enter first binary number: ")
            binary_b = input("Enter second binary number: ")
            binary_result = binary_subtract(binary_a, binary_b)
            print(f"Subtracting {binary_b} from {binary_a} is {binary_result}")

        elif choice == 11:
            octal_a = input("Enter first octal number: ")
            octal_b = input("Enter second octal number: ")
            octal_result = octal_subtract(octal_a, octal_b)
            print(f"Subtracting {octal_b} from {octal_a} is {octal_result}")

        elif choice == 12:
            hexadecimal_a = input("Enter first hexadecimal number: ")
            hexadecimal_b = input("Enter second hexadecimal number: ")
            hexadecimal_result = hexadecimal_subtract(hexadecimal_a, hexadecimal_b)
            print(f"Subtracting {hexadecimal_b} from {hexadecimal_a} is {hexadecimal_result}")



def decimal_to_binary(decimal):
    binary_before_dot = ''
    binary_after_dot = ''

    number_before_dot = int(decimal)
    number_after_dot = round((decimal - number_before_dot), 4)
    while number_before_dot > 0:
        binary_before_dot = str(number_before_dot % 2) + binary_before_dot
        number_before_dot = number_before_dot // 2
    while len(binary_after_dot) < 5:
        number_after_dot *= 2
        binary_after_dot += str(int(number_after_dot))
        number_after_dot -= int(number_after_dot)

    if binary_after_dot == '00000':
        binary = binary_before_dot
    else:
        binary = binary_before_dot + "." + binary_after_dot

    return binary

def binary_to_decimal(binary):
    binary_before_dot = 0
    binary_after_dot = 0
    index = 0
    binary_last = 0

    if "." in binary:
        number_before_dot, number_after_dot = binary.split('.')

        for number in reversed(number_before_dot):
            binary_before_dot += int(number) * (2 ** index)
            index += 1

        index = 0
        for number in number_after_dot:
            index += 1
            binary_after_dot += int(number) * pow(2, -index)
        binary_last = binary_before_dot + binary_after_dot


    else:
        for number in reversed(binary):
            binary_last += int(number) * (2 ** index)
            index += 1

    return binary_last


def decimal_to_octal(decimal):
    octal_before_dot = ''
    octal_after_dot = ''

    number_before_dot = int(decimal)
    number_after_dot = round((decimal - number_before_dot), 4)
    while number_before_dot > 0:
        octal_before_dot = str(number_before_dot % 8) + octal_before_dot
        number_before_dot = number_before_dot // 8
    while len(octal_after_dot) < 5:
        number_after_dot *= 8
        octal_after_dot += str(int(number_after_dot))
        number_after_dot -= int(number_after_dot)
    if octal_after_dot == '00000':
        octal =  octal_before_dot
    else:
        octal = octal_before_dot + "." + octal_after_dot

    return octal

def octal_to_decimal(octal):
    octal_before_dot = 0
    octal_after_dot = 0
    index = 0
    octal_last = 0

    if "." in octal:
        number_before_dot, number_after_dot = octal.split('.')

        for number in reversed(number_before_dot):
            octal_before_dot += int(number) * (8 ** index)
            index += 1

        index = 0
        for number in number_after_dot:
            index += 1
            octal_after_dot += int(number) * pow(8, -index)

        octal_last = octal_before_dot + octal_after_dot


    else:
        for number in reversed(octal):
            octal_last += int(number) * (8 ** index)
            index += 1

    return octal_last


def decimal_to_hexadecimal(decimal):
    hex_digits = "0123456789ABCDEF"
    hex_before_dot = ''
    hex_after_dot = ''

    number_before_dot = int(decimal)
    number_after_dot = round((decimal - number_before_dot), 4)
    while number_before_dot > 0:
        hex_before_dot = hex_digits[number_before_dot % 16] + hex_before_dot
        number_before_dot = number_before_dot // 16
    while len(hex_after_dot) < 5:
        number_after_dot *= 16
        hex_after_dot += hex_digits[int(number_after_dot)]
        number_after_dot -= int(number_after_dot)

    if hex_after_dot == '00000':
        hex = hex_before_dot
    else:
        hex = hex_before_dot + "." + hex_after_dot

    return hex

def hexadecimal_to_decimal(hexadecimal):
    hex_before_dot = 0
    hex_after_dot = 0
    index = 0
    hex = 0

    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                          'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    hexadecimal = hexadecimal.upper()
    if "." in hexadecimal:
        number_before_dot, number_after_dot = hexadecimal.split('.')

        for number in reversed(number_before_dot):
            hex_before_dot += hex_map[number]*(16**index)
            index += 1

        index = 0
        for number in number_after_dot:
            index += 1
            hex_after_dot += hex_map[number]*pow(16,-index)

        hex = hex_before_dot + hex_after_dot


    else:
        for number in reversed(hexadecimal):
            hex += hex_map[number]*(16**index)
            index += 1

    return hex


def add_binary(a,b):
    if '.' in a:
        if '.' in b:
            a_before_dot, a_after_dot = a.split('.')
            b_before_dot, b_after_dot = b.split('.')
            max_len_before_dot = max(len(a_before_dot), len(b_before_dot))
            max_len_after_dot = max(len(a_after_dot), len(b_after_dot))
            a_before_dot = a_before_dot.zfill(max_len_before_dot)
            b_before_dot = b_before_dot.zfill(max_len_before_dot)
            a_after_dot = a_after_dot.ljust(max_len_after_dot, '0')
            b_after_dot = b_after_dot.ljust(max_len_after_dot, '0')
            carry = 0
            result = ''
            for i in range(max_len_after_dot - 1, -1, -1):
                s = carry + int(a_after_dot[i]) + int(b_after_dot[i])
                if s >= 2:
                    carry = 1
                    s -= 2
                else:
                    carry = 0
                result = str(s) + result

            result = '.' + result

            for i in range(max_len_before_dot - 1, -1, -1):
                s = carry + int(a_before_dot[i]) + int(b_before_dot[i])
                if s >= 2:
                    carry = 1
                    s -= 2
                else:
                    carry = 0
                result = str(s) + result

            if carry:
                result = '1' + result

        else:
            print("Error")



    else:
        result = ''
        carry = 0

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            s = carry + int(a[i]) + int(b[i])
            if s >= 2:
                carry = 1
                s -= 2
            else:
                carry = 0
            result = str(s) + result

        if carry:
            result = '1' + result

    return result

def add_octal(a,b):
    if '.' in a:
        if '.' in b:
            a_before_dot, a_after_dot = a.split('.')
            b_before_dot, b_after_dot = b.split('.')
            max_len_before_dot = max(len(a_before_dot),len(b_before_dot))
            max_len_after_dot = max(len(a_after_dot),len(b_after_dot))
            a_before_dot = a_before_dot.zfill(max_len_before_dot)
            b_before_dot = b_before_dot.zfill(max_len_before_dot)
            a_after_dot = a_after_dot.ljust(max_len_after_dot, '0')
            b_after_dot = b_after_dot.ljust(max_len_after_dot, '0')
            carry = 0
            result = ''
            for i in range(max_len_after_dot-1, -1, -1):
                s = carry + int(a_after_dot[i]) + int(b_after_dot[i])
                if s >=8:
                    carry = 1
                    s -= 8
                else:
                    carry = 0
                result = str(s) + result


            result = '.' + result

            for i in range(max_len_before_dot - 1, -1, -1):
                s = carry + int(a_before_dot[i]) + int(b_before_dot[i])
                if s >= 8:
                    carry = 1
                    s -= 8
                else:
                    carry = 0
                result = str(s) + result

            if carry:
                result = '1' + result

        else:
            print("Error")



    else:
        result = ''
        carry = 0

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            s = carry + int(a[i]) + int(b[i])
            if s >= 8:
                carry = 1
                s -= 8
            else:
                carry = 0
            result = str(s) + result

        if carry:
            result = '1' + result

    return result

def add_hexadecimal(a,b):
    hex_map = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    hex_map_back = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}

    a = a.upper()
    b = b.upper()

    if '.' in a:
        if '.' in b:
            a_before_dot, a_after_dot = a.split('.')
            b_before_dot, b_after_dot = b.split('.')
            max_len_before_dot = max(len(a_before_dot),len(b_before_dot))
            max_len_after_dot = max(len(a_after_dot),len(b_after_dot))
            a_before_dot = a_before_dot.zfill(max_len_before_dot)
            b_before_dot = b_before_dot.zfill(max_len_before_dot)
            a_after_dot = a_after_dot.ijust(max_len_after_dot, '0')
            b_after_dot = b_after_dot.ijust(max_len_after_dot, '0')
            carry = 0
            result = ''
            for i in range(max_len_after_dot-1, -1, -1):
                s = carry + int(hex_map[a_after_dot[i]]) + int(hex_map[b_after_dot[i]])
                if s >=16:
                    carry = 1
                    s -= 16
                else:
                    carry = 0
                result = str(hex_map_back[s]) + result


            result = '.' + result

            for i in range(max_len_before_dot - 1, -1, -1):
                s = carry + int(hex_map[a_before_dot[i]]) + int(hex_map[b_before_dot[i]])
                if s >= 16:
                    carry = 1
                    s -= 16
                else:
                    carry = 0
                result = str(hex_map_back[s]) + result

            if carry:
                result = '1' + result

        else:
            print("Error")



    else:
        result = ''
        carry = 0

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            s = carry + int(a[i]) + int(b[i])
            if s >= 16:
                carry = 1
                s -= 16
            else:
                carry = 0
            result = str(hex_map_back[s]) + result

        if carry:
            result = '1' + result

    return result


def binary_subtract(a, b):
    if '.' in a:
        if '.' in b:
            a_before_dot, a_after_dot = a.split('.')
            b_before_dot, b_after_dot = b.split('.')
            max_len_before_dot = max(len(a_before_dot), len(b_before_dot))
            max_len_after_dot = max(len(a_after_dot), len(b_after_dot))
            a_before_dot = a_before_dot.zfill(max_len_before_dot)
            b_before_dot = b_before_dot.zfill(max_len_before_dot)
            a_after_dot = a_after_dot.ijust(max_len_after_dot, '0')
            b_after_dot = b_after_dot.ijust(max_len_after_dot, '0')
            carry = 0
            result = ''
            for i in range(max_len_after_dot - 1, -1, -1):

                s = int(a_after_dot[i]) - int(b_after_dot[i]) - carry
                if s < 0:
                    carry = 1
                    s += 2
                else:
                    carry = 0
                result = str(s) + result

            result = '.' + result

            for i in range(max_len_before_dot - 1, -1, -1):
                s = int(a_before_dot[i]) - int(b_before_dot[i]) - carry
                if s < 0:
                    carry = 1
                    s += 2
                else:
                    carry = 0
                result = str(s) + result

            result = result.lstrip('0')

        else:
            print("Error")



    else:
        result = ''
        carry = 0

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            s = int(a[i]) - int(b[i]) - carry
            if s < 0:
                carry = 1
                s += 2
            else:
                carry = 0
            result = str(s) + result

        result = result.lstrip('0')

    return result if result else '0'

def octal_subtract(a,b):
    if '.' in a:
        if '.' in b:
            a_before_dot, a_after_dot = a.split('.')
            b_before_dot, b_after_dot = b.split('.')
            max_len_before_dot = max(len(a_before_dot), len(b_before_dot))
            max_len_after_dot = max(len(a_after_dot), len(b_after_dot))
            a_before_dot = a_before_dot.zfill(max_len_before_dot)
            b_before_dot = b_before_dot.zfill(max_len_before_dot)
            a_after_dot = a_after_dot.ijust(max_len_after_dot, '0')
            b_after_dot = b_after_dot.ijust(max_len_after_dot, '0')
            carry = 0
            result = ''
            for i in range(max_len_after_dot - 1, -1, -1):

                s = int(a_after_dot[i]) - int(b_after_dot[i]) - carry
                if s < 0:
                    carry = 1
                    s += 8
                else:
                    carry = 0
                result = str(s) + result

            result = '.' + result

            for i in range(max_len_before_dot - 1, -1, -1):
                s = int(a_before_dot[i]) - int(b_before_dot[i]) - carry
                if s < 0:
                    carry = 1
                    s += 8
                else:
                    carry = 0
                result = str(s) + result

            result = result.lstrip('0')

        else:
            print("Error")



    else:
        result = ''
        carry = 0

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            s = int(a[i]) - int(b[i]) - carry
            if s < 0:
                carry = 1
                s += 8
            else:
                carry = 0
            result = str(s) + result

        result = result.lstrip('0')

    return result if result else '0'

def hexadecimal_subtract(a,b):
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    hex_map_back = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    a = a.upper()
    b = b.upper()

    if '.' in a:
        if '.' in b:
            a_before_dot, a_after_dot = a.split('.')
            b_before_dot, b_after_dot = b.split('.')
            max_len_before_dot = max(len(a_before_dot), len(b_before_dot))
            max_len_after_dot = max(len(a_after_dot), len(b_after_dot))
            a_before_dot = a_before_dot.zfill(max_len_before_dot)
            b_before_dot = b_before_dot.zfill(max_len_before_dot)
            a_after_dot = a_after_dot.ijust(max_len_after_dot, '0')
            b_after_dot = b_after_dot.ijust(max_len_after_dot, '0')
            carry = 0
            result = ''
            for i in range(max_len_after_dot - 1, -1, -1):
                s = int(hex_map[a_after_dot[i]]) - int(hex_map[b_after_dot[i]]) - carry
                if s < 0:
                    carry = 1
                    s += 16
                else:
                    carry = 0
                result = str(hex_map_back[s]) + result

            result = '.' + result

            for i in range(max_len_before_dot - 1, -1, -1):
                s = int(hex_map[a_before_dot[i]]) - int(hex_map[b_before_dot[i]]) - carry
                if s < 0:
                    carry = 1
                    s += 16
                else:
                    carry = 0
                result = str(hex_map_back[s]) + result

            result = result.lstrip('0')

        else:
            print("Error")



    else:
        result = ''
        carry = 0

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            s = int(a[i]) - int(b[i]) - carry
            if s < 0:
                carry = 1
                s += 16
            else:
                carry = 0
            result = str(hex_map_back[s]) + result

        result = result.lstrip('0')

    return result if result else '0'



main()