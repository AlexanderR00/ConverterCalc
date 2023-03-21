def main():
    check = ['ADD', 'SUB', 'MUL', 'INC', 'DEC', 'MOV', 'XCHG']
    ops =['DB', 'DW', 'DD']


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

        if not all(char.isalpha() for char in var):
            ans = False
            if not var[0].isalpha():
                ans = True
            elif not var[len(var)-1].isalpha():
                ans= True
            else:
                print('Неправильно. Переменная содержит непустимые знаки')
                ans = False

        return ans


    def sub(var1,var2):
        try:
            var1 = int(var1)
            var2 = int(var2)
            return var1-var2
        except:
            print("Ошибка операции")

    def add(var1,var2):
        try:
            var1 = int(var1)
            var2 = int(var2)
            return var1+var2
        except:
            print("Ошибка операции")

    def dec(var):
        try:
            first_var = int(var)
            first_var = first_var - 1
            return first_var
        except:
            print("Ошибка операции. Вы ввели текст")

    def inc(var):
        try:
            first_var = int(var)
            first_var = first_var + 1
            return first_var
        except:
            print("Ошибка операции. Вы ввели текст")


    def checkstart(var):
        var = var.split()
        name_var = var[0].upper()
        if checkvar(var[0].upper()):
            value = var[2].upper().split()
            if var[1].upper() in ops:
                try:
                    first_var = int(var[2])
                    return first_var,name_var
                except:
                    if value[0] == value[len(value) - 1]:
                        first_var = var[2].replace("'", "").replace('"', '')
                        return first_var,name_var
                    else: print("Неверный синтаксис")
            else: print("Неверное интерпретирование")
        else: print("Ошибка")


    loop = -1
    while(loop!=0):
        output=0
        var1 =str(input("teST2: "))
        try:
            var1,name_var1 = checkstart(var1)
            output = var1
        except:
            print("Ошибка")
        var2 = str(input(""))
        var3 = str(input(""))
        var4 = str(input(""))
        if not len(var2)==0:
            test = var2.split()
            if test[0].upper() in check:
                if test[0].upper() == 'INC':
                    var1= inc(var1)
                    print(var1)
                elif test[0].upper() == 'DEC':
                    var1 = dec(var1)
                    print(var1)

                else:print("Ошибка")
            else:
                var2,name_var2 = checkstart(var2)


        if not len(var3)==0:
            test = var3.split()
            if test[0].upper() in check:
                if test[0].upper() == 'ADD':
                    if test[1].upper() == name_var1 and test[2].upper() == name_var2:
                        var1 = add(var1,var2)
                    elif test[1].upper() == name_var2 and test[2].upper() == name_var1:
                        var2 = add(var2,var1)
                    else: print("Ошибка значений")



                else: print("Неверная операция")


        if not len(var4) == 0:
            test = var4.split()
            if test[0].upper() in check:
                if test[0].upper() == 'INC':
                    if test[1].upper() == name_var1:
                        var1 = inc(var1)
                        print(var1)
                    elif test[1].upper() == name_var2:
                        var2 = inc(var2)
                        print(var2)
                    else:print("Ошибка")
                elif test[0].upper() == 'DEC':
                    if test[1].upper() == name_var1:
                        var1 = dec(var1)
                        print(var1)
                    elif test[1].upper() == name_var2:
                        var2 = dec(var2)
                        print(var2)
                    else:print("Ошибка")
        else: print(var3)























main()