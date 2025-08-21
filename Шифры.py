import tkinter
def dannie():
    global alfavit, shag, slovo
    alfavit = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"   # алфавит
    print("Вы выбрали шифрование методом Цезаря")
    while True:
        shag_input = input("Введите шаг шифровки: ")
        if shag_input.isdigit():
            shag = int(shag_input)   # шаг
            break
        else:
            print("Шаг шифровки должен быть числом. Попробуйте снова.")
    slovo = input("Введите сообщение для шифровки: ")    #сообщение
def ras_dannie():
    global alfavit, shag, slovo
    alfavit = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"   # алфавит
    print("Вы выбрали расшифровку методом Цезаря")
    while True:
        shag_input = input("Введите шаг расшифровки: ")
        if shag_input.isdigit():
            shag = int(shag_input)   # шаг
            break
        else:
            print("Шаг расшифровки должен быть числом. Попробуйте снова.")
    slovo = input("Введите сообщение для расшифровки: ")    #сообщение

def Zezar():
    global alfavit, shag, slovo
    itog = ""
    for i in slovo:
        a = alfavit.find(i)
        a2 = a + shag
        if i in alfavit:
            itog += alfavit[a2 % len(alfavit)]
        else:
            itog += i
    print("Зашифрованный текст:", itog)

import random

def random_alf():     #Случайный алфавит
    alfavit = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    random.shuffle(alfavit)
    return "".join(alfavit)

def alkindi(text, alfavit):
    shifr = ""
    a = {char.upper(): alfavit[i] for i, char in enumerate("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")}
    for char in text:
        if char.isalpha():
            shifr += a.get(char.upper(), char) # Без .get ошибка Key
        else:
            shifr += char
    return shifr

def de_vigener(text, key):
    shifr = ""
    key_repeat = (key * (len(text) // len(key)) + key[:len(text) % len(key)])
    for i in range(len(text)):
        a = text[i]
        if a.isalpha():
            sdvig = ord(key_repeat[i].upper()) - ord('А')
            if a.islower():
                shifr += chr((ord(a) - ord('а') - sdvig) % 33 + ord('а'))
            else:
                shifr += chr((ord(a) - ord('А') - sdvig) % 33 + ord('А'))
        else:
             shifr += a
    return shifr
def ras_de_vigener(text, key):
    ras_text = ""
    key_repeat = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    for i in range(len(text)):
        a = text[i]
        if a.isalpha():
            sdvig = -(ord(key_repeat[i].upper()) - ord('А'))
            if a.islower():
                ras_text += chr((ord(a) - ord('а') - sdvig + 33) % 33 + ord('а'))
            else:
                ras_text += chr((ord(a) - ord('А') - sdvig + 33) % 33 + ord('А'))
        else:
            ras_text += a
    return ras_text

def repeat_ras_de_vigener():
    while True:
        print("Вы выбрали расшифровку методом Виженера.")
        text = input("Введите зашифрованный текст: ")
        key = input("Введите ключ: ")
        ras_text = ras_de_vigener(text, key)
        print("Расшифрованный текст:", ras_text)
        repeat = input("Хотите продолжить? (да - 1/нет - 2/возврат - 3): ")
        if repeat.lower() == "3":
            vopros()
        elif repeat.lower() == "2":
            break


def repeat_Zezar():
    while True:
        dannie()
        Zezar()
        repeat = input("Хотите продолжить? (да - 1/нет - 2/возврат - 3): ")
        if repeat.lower() == "3":
            vopros()
        elif repeat.lower() == "2":
            break

def repeat_al_kindi():
    while True:
        print("Вы выбрали шифрование методом Аль-Кинди")
        text = input("Введите сообщение для зашифровки: ")
        ranalf = random_alf()
        shifr = alkindi(text, ranalf)
        print("Алфавит: ", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
        print("Ключ:    ", ranalf)
        print("Зашифрованный текст: ", shifr)
        repeat = input("Хотите продолжить? (да - 1/нет - 2/возврат - 3): ")
        if repeat.lower() == "3":
            vopros()
        elif repeat.lower() == "2":
            break

def repeat_de_vigener():
    while True:
        print("Вы выбрали шифрование методом Виженера")
        text = input("Введите текст для шифрования: ")
        key = input("Введите ключ для шифрования: ")
        shifr = de_vigener(text, key)
        print("Зашифрованный текст: ", shifr)
        repeat = input("Хотите продолжить? (да - 1/нет - 2/возврат - 3): ")
        if repeat.lower() == "3":
            vopros()
        elif repeat.lower() == "2":
            break
def ras_Zezar():
    global alfavit, shag, slovo
    itog = ""
    for i in slovo:
        a = alfavit.find(i)
        a2 = a - shag
        if i in alfavit:
            itog += alfavit[a2 % len(alfavit)]
        else:
            itog += i
    print("Расшифрованный текст:", itog)
def repeat_ras_Zezar():
    while True:
        ras_dannie()
        ras_Zezar()
        repeat = input("Хотите продолжить? (да - 1/нет - 2/возврат - 3): ")
        if repeat.lower() == "3":
            vopros()
        elif repeat.lower() == "2":
            break

def ras_alkindi(text, alfavit):
        decrypted_text = ""
        a = {char.upper(): alfavit[i] for i, char in enumerate("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")}
        for char in text:
            if char.isalpha():
                decrypted_text += [key for key, value in a.items() if value == char.upper()][0]
            else:
                decrypted_text += char
        return decrypted_text


def repeat_ras_al_kindi():
    while True:
        print("Вы выбрали шифрование методом Аль-Кинди")
        text = input("Введите сообщение для расшифровки: ")
        ranalf = input("Введите ключ: ")
        shifr = ras_alkindi(text, ranalf)
        print("Расшифрованный текст: ", shifr)
        repeat = input("Хотите продолжить? (да - 1/нет - 2/возврат - 3): ")
        if repeat.lower() == "3":
            vopros()
        elif repeat.lower() == "2":
            break

def vopros ():
 vopros1 = input("Выберите режим: Шифрование - 1; Расшифрование - 2: ")
 if vopros1 == "1":
    while True:
     vopros = input("Выберите режим: Цезарь - 1, Аль-Кинди - 2, Блез де Виженер - 3: ")
     if vopros == "1":
       repeat_Zezar()
       break
     elif vopros == "2":
       repeat_al_kindi()
       break
     elif vopros == "3":
       repeat_de_vigener()
       break
     else:
        print("Попробуйте ввести снова")
 else:
     while True:
         vopros3 = input("Выберите режим: Цезарь - 1, Аль-Кинди - 2, Блез де Виженер - 3: ")
         if vopros3 == "1":
             repeat_ras_Zezar()
             break
         elif vopros3 == "2":
             repeat_ras_al_kindi()
             break
         elif vopros3 == "3":
             repeat_ras_de_vigener()
             break
         else:
             print("Попробуйте ввести снова")

vopros()


