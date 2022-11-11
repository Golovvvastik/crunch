import os 
import time
from sys import platform 

def start(): # Старт
    for i in range(11):
        sim = "#"
        time.sleep(0.2)
        print(sim*i,"\r",end="")
    print()

def pre_close(): # Перед закрытием
    for i in range(12, 0, -1):
        sim = "#"
        i2 = i-1
        time.sleep(0.2)
        print(sim*i2, "\r",end="")
    print("\r")

def os_platform():              # Удалить по желанию, и вызов функции удалить не забудте внизу
    if platform == "win32":
        os.system("cls")
    elif platform == "linux" or "darwin":
        os.system("clear")


def vvod(): # Ввод данных, можно добавить свой вопрос
    while True:
        t_input = input(f"{len(l)+1}| Факт/q: ") # создать вопрос, либо выйти - q
        if t_input == "q":
            break
        else:
            l.append(set(str(t_input)))
            ques.write(f"{len(l)}| {t_input}\n")


def y_n_register():
    while True:
        print("y == [Dog] => [DdoOgG], n == [Dog] => [Dog]")
        yes_no_register = str(input("y/n: ")) #без превращения верхних регистров в нижнии или нет
        if str.islower(yes_no_register) == True:
            if str(yes_no_register) == "y":
                break
            if str(yes_no_register) == "n":
                break
            else:
                print("Не пиши чипухи!")
                os_platform()
                continue
        else:
            print("Не пиши чипухи!")
            os_platform()
            continue
    return yes_no_register


def uni():  # Объединение
    tmp_pop = list(range(len(l)))
    tmp_pop.pop(-1)
    all_input = set()
    for i in tmp_pop:
        count = i + 1
        if count == 1:
            all_input = l[i].union(l[count])
        elif count > 1:
            all_input = all_input.union(l[count])
    return all_input


def if_registr(un):    # Смотрит на большие и маленькие символы, и ищет есть ли похожий, если нет, то добавляет
    
    tmp_pop = list(range(len(un))) # длинна set(un), в листе от 0 до ...
    tmp_list = list(un) # временный лист
    end_list = tmp_list # конечный лист, на возврат

    for i in tmp_pop:
        tmp_register = str(tmp_list[i]) # временная буква из временного списка, для сравнения
        
        if str.isupper(tmp_register) == True:      # Если буква из индекса [i] большая, то мы УМЕНЬШАЕМ и сравниваем со списком
            tmp_register_lower = tmp_register.lower()
            count_lower = 0
            for x_lower in tmp_list:
                if x_lower != tmp_register_lower:
                    count_lower += 1
                if x_lower == tmp_register_lower:
                    count_lower = 0
                    continue
            if count_lower == int(len(tmp_list)):
                end_list.append(tmp_register_lower)
                continue
            else:
                continue

        if str.islower(tmp_register) == True:      # Если буква из индекса [i] маленькая, то мы УВЕЛИЧИВАЕМ и сравниваем со списком
            tmp_register_upper = tmp_register.upper()
            count_upper = 0
            for x_upper in tmp_list:       
                if x_upper != tmp_register_upper:
                    count_upper += 1
                if x_upper == tmp_register_upper:
                    count_upper = 0
                    continue
            if count_upper == int(len(tmp_list)):
                end_list.append(tmp_register_upper)    
                continue
            else:
                continue

    return set(end_list)


def summary(uni_do): # Сложение и запись, каждой буквы, в каждем индексе
    tmp_uni = list(uni_do)
    for i in range(len(tmp_uni)):
        crunch.write(tmp_uni[i])
    print



l = []
start()
with open("question.txt", "a") as ques:
    vvod()
    ques.write("\n")
    ques.close()

with open("tpass.lst", "w") as crunch: # Открытие файла, и начало работы функций
    crunch.write("tmp = [")
    if_y_n_register = y_n_register()
    if str(if_y_n_register) == "y":
        summary(if_registr(uni()))
    if str(if_y_n_register) == "n":
        summary(uni())
    crunch.write("]")
    pre_close()
    crunch.close()

os_platform()
print("OK, go use FILE = tpass.lst")
time.sleep(3)
