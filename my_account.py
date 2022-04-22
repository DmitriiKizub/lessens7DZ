# ДЗ № 7 Задание № 1
import os
import json
import pickle
import shutil

FILEACCOUNT = 'my_account.txt'
HISTORY = 'history.txt'
history_summ = {}
CHEK_SUMM ='На Вашем счете:'

if os.path.exists(FILEACCOUNT):
    with open(FILEACCOUNT, 'r') as f:
        result = json.load(f)
        summ_account = result
        for k,y in summ_account.items():
            print(f'На Вашем счете: {y}')
else:
    print(f'На Вашем счете: 0')
    summ_account = {
        'На Вашем счете:': 0
    }

while True:
    print('Банковский счет')
    print('1. Пополнить счет\n2. История покупок\n3. Купить товар\n4. Балланс\n5. Просмотр рабочей директории\n6. Сохранить содержимое рабочей директории в файл\n7. listdir.txt\n8. Выход')

    select_menu = input('Выберете пункт:')
    if select_menu == '1':
        summ_account_input = input('Введите сумму пополнения: ')
        for k,y in summ_account.items():
            summ_account[CHEK_SUMM] = y+int(summ_account_input)
        summ_acount_bit = json.dumps(summ_account)
        print(summ_acount_bit)
        with open(FILEACCOUNT, 'w') as f:
            f.write(summ_acount_bit)

    if select_menu == '2':
        if os.path.exists(HISTORY):
            with open(HISTORY, 'r') as f:
                result = json.load(f)
                print('*' * 29)
                for k,y in result.items():
                    print(k,y)
                print('*' * 29)
        else:
            print('*'*29)
            print('***Список покупок пуст!!!!***')
            print('*' * 29)

    if select_menu == '3':
        if not os.path.exists(HISTORY):
            prod = input('Введите название продукта: ')
            chek = input('Введите стоимость: ')
            if prod != '' or chek != '':
                with open(HISTORY, 'w') as f:

                    history_summ.update({prod: chek})
                    json.dump(history_summ, f)
            else:
                print('*' * 29)
                print('Введены не все данные!!!')
                print('*' * 29)

        else:
            if os.path.exists(FILEACCOUNT):
                with open(FILEACCOUNT, 'r') as f:
                    summ_account = json.load(f)

                with open(HISTORY, 'r') as f:
                    result = json.load(f)
                    prod = input('Введите название продукта: ')
                    chek = int(input('Введите стоимость: '))
                    if chek != '' or prod != '':
                        if int(summ_account[CHEK_SUMM]) - chek >= 0:
                            for k,y in summ_account.items():
                                summ_account[CHEK_SUMM] = y - chek
                                summ_account_bit = json.dumps(summ_account)
                            with open(FILEACCOUNT, 'w') as f:
                                 f.write(summ_account_bit)
                        else:
                            print('*' * 29)
                            print('На Вашем счете недостаточно средств')
                            print('*' * 29)

                        with open(HISTORY, 'w') as f:

                            history_summ = result
                            history_summ.update({prod: chek})
                            json.dump(history_summ, f)
                    else:
                        print('*' * 29)
                        print('Введены не все данные!!!')
                        print('*' * 29)
            else:
                print('*' * 29)
                print('На Вашем счете недостаточно средств!')
                print('*' * 29)
    if select_menu == '4':
        with open(FILEACCOUNT, 'r') as f:
            result = json.load(f)
            for k,y in result.items():
                print(f'Ваш балланс: {y}')
    if select_menu == '5':
        print('*' * 29)
        for i in os.listdir():
            print(i)
        print('*' * 29)
    if select_menu == '6':
        dir_list = []
        for i in os.listdir():
           dir_list.append(i)
        dir_list_bit = json.dumps(dir_list)
        with open('dir_file.txt', 'w') as f:
            f.write(dir_list_bit)

    if select_menu == '7':
        dir_show_constant = []
        show_dir = os.getcwd()
        for i in os.listdir(show_dir):
            if os.path.isdir(os.path.join(show_dir, i)):
                dir_show_constant.append(i)
        file_show_constant = []
        for i in os.listdir():
            if os.path.isfile(os.path.join(show_dir,i)):
                file_show_constant.append(i)

        with open('listdir.txt', 'w') as f:
             result_dir_bit = json.dumps(file_show_constant)
             result_file_bit = json.dumps(dir_show_constant)

             f.write(f'File: {result_file_bit}\nDirs:{result_dir_bit}')

    if select_menu == '8':
        break

















