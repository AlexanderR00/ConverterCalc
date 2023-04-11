#Ritter Alexander
#28.03.23-
# Vse norm


import Converter



def main():
    check = ['ADD', 'SUB', 'MUL', 'INC', 'DEC', 'MOV', 'XCHG']
    ops = ['DB', 'DW', 'DD']
    bdoh = ['B', 'D', 'O', 'H']



    # Все ок 03,04
    def xchg(var1,var2):
        try:
            var1 = int(var1)
            var2 = int(var2)
            return var2,var1
        except:
            return var2,var1
    #Все ок 03,04
    def mul(var1,var2):
        try:
            var1 = int(var1)
            var2 = int(var2)
            return var1*var2
        except:
            if var1[len(var1) - 1].upper() in bdoh and var2[len(var2) - 1].upper() in bdoh:
                if var1[len(var1) - 1].upper() == 'B':
                    first_var = Converter.binary_to_decimal(var1[:-1]) * Converter.binary_to_decimal(var2[:-1])
                    return str(Converter.decimal_to_binary(first_var)) + "B"
                elif var1[len(var1) - 1].upper() == 'D':
                    first_var = int(var1[:-1]) * int(var2[:-1])
                    return str(first_var) + "D"
                elif var1[len(var1) - 1].upper() == 'O':
                    first_var = Converter.octal_to_decimal(var1[:-1]) * Converter.octal_to_decimal(var2[:-1])
                    return str(Converter.decimal_to_octal(first_var)) + 'O'
                elif var1[len(var1) - 1].upper() == 'H':
                    first_var = Converter.hexadecimal_to_decimal(var1[:-1]) * Converter.hexadecimal_to_decimal(var2[:-1])
                    return str(Converter.decimal_to_hexadecimal(first_var)) + 'H'
                else:
                    print("Ошибка!")
            else:
                print("Ошибка операции")
    # Все ок 03,04
    def mov(var1,var2):
        try:
            var1 = int(var1)
            var2 = int(var2)
            return var2
        except:
            return var2

    # Все ок 31,03
    def sub(var1,var2):
        try:
            var1 = int(var1)
            var2 = int(var2)
            return var1-var2
        except:
            if var1[len(var1) - 1].upper() in bdoh and var2[len(var2) - 1].upper() in bdoh:
                if var1[len(var1) - 1].upper() == 'B':
                    first_var = Converter.binary_subtract(var1[:-1], var2[:-1])
                    return str(first_var) + "B"
                elif var1[len(var1) - 1].upper() == 'D':
                    first_var = int(var1[:-1]) - int(var2[:-1])
                    return str(first_var) + "D"
                elif var1[len(var1) - 1].upper() == 'O':
                    first_var = Converter.octal_subtract(var1[:-1], var2[:-1])
                    return str(first_var) + 'O'
                elif var1[len(var1) - 1].upper() == 'H':
                    first_var = Converter.hexadecimal_subtract(var1[:-1], var2[:-1])
                    return str(first_var) + 'H'
                else:
                    print("Ошибка!")
            else:
                print("Ошибка операции")
    # Все ок 31,03
    def add(var1,var2):
        try:
            var1 = int(var1)
            var2 = int(var2)
            return var1+var2
        except:
            if var1[len(var1) - 1].upper() in bdoh and var2[len(var2)-1].upper() in bdoh:
                if var1[len(var1) - 1].upper() == 'B':
                    first_var = Converter.add_binary(var1[:-1],var2[:-1])
                    return str(first_var)+"B"
                elif var1[len(var1) - 1].upper() == 'D':
                    first_var = int(var1[:-1]) + int(var2[:-1])
                    return str(first_var)+"D"
                elif var1[len(var1) - 1].upper() == 'O':
                    first_var = Converter.add_octal(var1[:-1], var2[:-1])
                    return str(first_var) + 'O'
                elif var1[len(var1) - 1].upper() == 'H':
                    first_var = Converter.add_hexadecimal(var1[:-1],var2[:-1])
                    return str(first_var) + 'H'
                else:
                    print("Ошибка!")
            else:
                print("Ошибка операции")
    # все ок 30,03
    def dec(var):
        try:
            first_var = int(var)
            first_var = first_var - 1
            return first_var
        except:
            if var[len(var) - 1].upper() in bdoh:
                if var[len(var) - 1].upper() == 'B':
                    first_var = Converter.binary_to_decimal(var[:-1]) - 1
                    return Converter.decimal_to_binary(first_var)+"B"
                elif var[len(var) - 1].upper() == 'D':
                    first_var = int(var[:-1]) - 1
                    return str(first_var)+"D"
                elif var[len(var) - 1].upper() == 'O':
                    first_var = Converter.octal_to_decimal(var[:-1]) - 1
                    return Converter.decimal_to_octal(first_var) + 'O'
                elif var[len(var) - 1].upper() == 'H':
                    first_var = Converter.hexadecimal_to_decimal(var[:-1]) - 1
                    return Converter.decimal_to_hexadecimal(first_var) + 'H'
                else:
                    print("Ошибка!")
            else:
                print("Ошибка операции. Вы ввели текст")
    # все ок 30,03
    def inc(var):
        try:
            first_var = int(var)
            first_var = first_var + 1
            return first_var
        except:
            if var[len(var) - 1].upper() in bdoh:
                if var[len(var) - 1].upper() == 'B':
                    first_var = Converter.binary_to_decimal(var[:-1])+1
                    return Converter.decimal_to_binary(first_var)+"B"
                elif var[len(var) - 1].upper() == 'D':
                    first_var = int(var[:-1]) + 1
                    return str(first_var)+"D"
                elif var[len(var) - 1].upper() == 'O':
                    first_var = Converter.octal_to_decimal(var[:-1]) + 1
                    return Converter.decimal_to_octal(first_var) + 'O'
                elif var[len(var) - 1].upper() == 'H':
                    first_var = Converter.hexadecimal_to_decimal(var[:-1]) + 1
                    return Converter.decimal_to_hexadecimal(first_var) + 'H'
                else:
                    print("Ошибка!")
            else:
                print("Ошибка операции. Вы ввели текст")

    def checkvar(var):
        ans = True
        # Проверка на точку
        if '.' in var:
            if not var[0] == '.':
                print("Неправильно! Переменная содержит знак '.' ")
                ans = False

        # Проверка на число
        if var[0].isdigit():
            print("Неправильно.Переменная начинается с цифры")
            ans = False


        # Проверка на знаки
        if not all(char.isalpha() for char in var):
            ans = False
            if not var[0].isalpha():
                ans = True
            elif not var[len(var)-1].isalpha():
                ans = True
            elif '_' in var and var[0] != '_' and var[len(var)-1] != '_':
                ans = True
            else:
                print('Неправильно. Переменная содержит непустимые знаки')
                ans = False

        return ans

    def checkstart(var):
        var = var.split()
        name_var = var[0].upper()
        if checkvar(var[0].upper()):
            value = var[2].upper()
            if var[1].upper() in ops:
                try:
                    first_var = int(var[2])
                    return first_var, name_var
                except:
                    if value[0] == value[len(value) - 1]:
                        first_var = var[2].replace("'", "").replace('"', '')
                        return first_var, name_var
                    elif value[len(value)-1].upper() in bdoh:
                        first_var = var[2].upper()
                        return first_var,name_var
                    else:
                        print("Неверный синтаксис")
            else:
                print("Неверное интерпретирование")
        else:
            print("Ошибка")


    loop = -1
    while(loop != 0):
        output = 0
        var1 = str(input("teST2: "))
        try:
            var1, name_var1 = checkstart(var1)
            output = var1
        except():
            print("Ошибка")
        var2 = str(input(""))
        var3 = str(input(""))
        var4 = str(input(""))
        if not len(var2) == 0:
            test = var2.split()
            if test[0].upper() in check:
                if test[0].upper() == 'INC':
                    if test[1].upper() == name_var1:
                        var1 = inc(var1)
                        output = var1
                    else:
                        print("Переменная не найдена")
                elif test[0].upper() == 'DEC':
                    if test[1].upper() == name_var1:
                        var1 = dec(var1)
                        output = var1
                    else:
                        print("Переменная не найдена")
                else:
                    print("Ошибка")
            else:
                var2, name_var2 = checkstart(var2)


        if not len(var3)==0:
            test = var3.split()
            if test[0].upper() in check:
                if test[0].upper() == 'ADD':
                    if test[1].upper() == name_var1 and test[2].upper() == name_var2:
                        var1 = add(var1, var2)
                        output = var1
                    elif test[1].upper() == name_var2 and test[2].upper() == name_var1:
                        var2 = add(var2, var1)
                        output = var2
                    else: print("Ошибка значений")

                elif test[0].upper() == 'SUB':
                    if test[1].upper() == name_var1 and test[2].upper() == name_var2:
                        var1 = sub(var1,var2)
                        output =var1
                    elif test[1].upper() == name_var2 and test[2].upper() == name_var1:
                        var2 = sub(var2,var1)
                        output=var2
                    else: print("Ошибка значений")

                elif test[0].upper() == 'MUL':
                    if test[1].upper() == name_var1 and test[2].upper() == name_var2:
                        var1 = mul(var1, var2)
                        output = var1
                    elif test[1].upper() == name_var2 and test[2].upper() == name_var1:
                        var2 = mul(var2, var1)
                        output = var2
                    else:
                        print("Ошибка значений")

                elif test[0].upper() == 'MOV':
                    if test[1].upper() == name_var1 and test[2].upper() == name_var2:
                        var1 = mov(var1, var2)
                        output = var1
                    elif test[1].upper() == name_var2 and test[2].upper() == name_var1:
                        var2 = mov(var2, var1)
                        output = var2
                    else:
                        print("Ошибка значений")

                elif test[0].upper() == 'XCHG':
                    if test[1].upper() == name_var1 and test[2].upper() == name_var2:
                        var1,var2 = xchg(var1, var2)
                        output = name_var1 + " = " + str(var1) + "\n" + name_var2 + " = " + str(var2)
                    elif test[1].upper() == name_var2 and test[2].upper() == name_var1:
                        var2,var1 = xchg(var2, var1)
                        output = name_var2 + " = " + str(var2) + "\n" + name_var1 + " = " + str(var1)
                    else:
                        print("Ошибка значений")

                elif test[0].upper() == 'INC':
                    if test[1].upper() == name_var1:
                        var1 = inc(var1)
                        output = var1
                    elif test[1].upper() == name_var2:
                        var2 = inc(var2)
                        output = var2
                    else:
                        print("Переменная не найдена")

                elif test[0].upper() == 'DEC':
                    if test[1].upper() == name_var1:
                        var1 = dec(var1)
                        output = var1
                    elif test[1].upper() == name_var2:
                        var2 = dec(var2)
                        output = var2
                    else:
                        print("Переменная не найдена")

                else:
                    print("Неверная операция")


        if not len(var4) == 0:
            test = var4.split()
            if test[0].upper() in check:
                if test[0].upper() == 'INC':
                    if test[1].upper() == name_var1:
                        var1 = inc(var1)
                        output = var1
                    elif test[1].upper() == name_var2:
                        var2 = inc(var2)
                        output = var2
                    else:print("Ошибка")
                elif test[0].upper() == 'DEC':
                    if test[1].upper() == name_var1:
                        var1 = dec(var1)
                        output =var1
                    elif test[1].upper() == name_var2:
                        var2 = dec(var2)
                        output = var2
                    else:print("Ошибка")

                else:
                    print("Неверная операция")
        print(output)









main()