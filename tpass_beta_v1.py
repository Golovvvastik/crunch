import os 
import time

def start(): # Старт
    print("START")
    time.sleep(1)
    print("/.../")
    time.sleep(1)
    print("/#../")
    time.sleep(1)
    print("/##./")
    time.sleep(1)
    print("/###/")

def pre_close(): # Перед закрытием
    print("/###/")
    time.sleep(1)
    print("/##./")
    time.sleep(1)
    print("/#../")
    time.sleep(1)
    print("/.../")
    time.sleep(1)
    print()

def vvod(): # Ввод данных, можно добавить свой вопрос
    l.append(set(str(input("Имя: "))))
    l.append(set(str(input("Фамилия: "))))
    l.append(set(str(input("Петомец: "))))

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

def summary(uni_do): # Сложение и запись, каждой буквы, в каждем индексе
    tmp_uni = list(uni_do)
    for i in range(len(tmp_uni)):
        crunch.write(tmp_uni[i])
    print


l = []
start()
vvod()

with open("tpass.lst", "w") as crunch:
    crunch.write("tmp = [")
    summary(uni())
    crunch.write("]")
    pre_close()
    crunch.close()

print("OK, go use FILE = tpass.lst")
