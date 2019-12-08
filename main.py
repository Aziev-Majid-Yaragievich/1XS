from colorama import Fore, Style, Back #Import библиотек
import sqlite3
import sys
import time

#Тест по информатике
def informatic():
    print(Back.GREEN+Fore.BLACK+'Вы выбрали информатику!')
    print(Back.BLACK+Fore.WHITE+'')
    time.sleep(1)#Засыпание программы на 1 секунду, что-бы пользователь прочитал содержимое текста
    #Условия решений задач
    print('ВАЖНО!')
    time.sleep(0.5)
    print('Ответ должен содержать имено слово!')
    time.sleep(2)
    null = input('Нажмините ENTER, если готовы начать:')
    #Вопросы
    voprosi = [
        'Устройство вывода',
        'Устройтво ввода',
        'Python - это',
        'Windows - это'
    ]
    #Варианты ответов
    variants = [
        ['принтер', 'клавиатура', 'мышка', 'микрофон'],
        ['микрофон', 'монитор', 'наушники'],
        ['ЯП','ОС'],
        ['ОС', 'Linux']
    ]
    #Правильные ответы
    pravilnyOtvet = [
        ['принтер'],
        ['микрофон'],
        ['яп'],
        ['ос']
    ]
    count = 0 # текущий номер вопроса чтобы получить набор правильных ответов для этого вопроса
    userResponse = [] # Совподение ответов пользователя с правильными ответами
    userResult = [] 
    for i in voprosi:
        print('')
        print(Fore.RED + 'Вопрос: ', i)
        print(Fore.GREEN + "Варианты ответов:")
        for j in variants[count]:
            print(Fore.WHITE + j)
        #Орагнизовать ввод ответов от пользователя
        response = input(Fore.GREEN + 'Ваш ответ: ')
        print(Fore.WHITE + '')
        response = response.lower()
        #Организовать проверку отеста от пользователя
        responseMassive = response.split()
        userResult.append(responseMassive)
        currentOtvet = pravilnyOtvet[count]
        results = {}
        for res in currentOtvet:
            results[res] = responseMassive.count(res)
        #Сохранить число правильных ответов пользователя в массив
        userResponse.append(results)
        count+=1
    # Печать результатов ответов пользователя
    for i in range(voprosi.__len__()):
        time.sleep(0.2)#Что-бы пользователь учпел немного прочитать
        print('На вопрос номер ', i+1)
        print(voprosi[i])
        print('Пользователь', name ,'дал ответы:', userResult[i])
        print('Правильные ответы:', userResult[i])
        print('--------')


    # Отобразить результаты тестирования
    totalRuleResponsesForUser = 0 # Общее число правильных ответов пользователя
    totalResponses = 0 # Общее число правильных ответов в тесте
    nuvQuestion = 0
    for i in userResponse:
        nuvQuestion +=1
        print ('На вопрос с номером ',nuvQuestion,' пользователь ответил правильлно на ',sum(i.values()),' из ',i.__len__())
        totalRuleResponsesForUser += sum(i.values())
        totalResponses += i.__len__()
    global score
    score = round ((totalRuleResponsesForUser / totalResponses) * 5)
    print('Результат тестирования: ',score)

print(Back.GREEN+Fore.BLACK+'Привет! Это программа beta Гранд')
print(Back.BLACK+Fore.WHITE)
time.sleep(1)

name = input('Ваше имя: ')
fam = input('Ваша фамилия: ')
print('')

if name == '' or fam == '':
    print('Так не пойдёт дружище :), заполняй своё имя и фамилию!')
    sys.exit()

pred = 'Информатика'

print("Наши предметы:", pred)

#Выбор предмета
test = input('Какой предмет вы хотите выбрать? ')
print('')

#В случае выбора информатики
if (test.lower() == "информатика") or (test.lower() == 'инфа') or (test.lower() == 'инфо') or test == '1':
    informatic()
#В случае выбора другого варианта
else:
    print("Пока что этого у нас нет")
    sys.exit() #Выход иг программы

conn = sqlite3.connect('sowpods.csv')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS pan(name TEXT, fam TEXT, pred TEXT, score INT)''')
conn.commit()
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
# Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute('''INSERT INTO pan VALUES(?, ?, ?, ?)''', (name, fam, pred, score))

conn.commit()
conn.close()