from colorama import Fore, Style, Back #Import библиотек
import sys

#Тест по информатике
def informatic():
    voprosi = [
        'Устройство вывода (возможно несколько вариантов)',
        'Устройтво ввода (возможно несколько вариантов)',
        'Монитор - это (возможно несколько вариантов)',
        'Windows - это (возможно несколько вариантов)'
    ]
    variants = [
        ['Принтер', 'Клавиатура', 'Мышка', 'Микрофон'],
        ['Клавиатура', 'Микрофон', 'Монитор', 'Наушники'],
        ['Устройство ввода','Устройство вывода'],
        ['Операционная Система', 'Программа для игр']
    ]
    pravilnyOtvet = [
        ['Принтер'],
        ['Клавиатура', 'Микрофон'],
        ['Устройство вывода'],
        ['Операционная Система']
    ]
    count = 0 # текущий номер вопроса чтобы получить набор правильных ответов для этого вопроса
    userResponse = [] # Совподение ответов пользователя с правильными ответами
    userResult = [] 
    for i in voprosi:
        print(Fore.RED + i)
        print(Fore.GREEN + "Варианты ответов:")
        for j in variants[count]:
            print(Fore.BLUE + j)
        #Орагнизовать ввод ответов от пользователя
        response = input(Fore.GREEN + 'Ваш ответ: ')

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
        print('На вопрос номер ', i+1)
        print(voprosi[i])
        print('Пользователь', name ,'дал ответы:', userResult[i])
        print('Правильные ответы:', pravilnyOtvet[i])
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
    score = round ((totalRuleResponsesForUser / totalResponses) * 5)
    print('Результат тестирования: ',score)

print("Важно, надо вводить варианты через пробел.")

pred = 'Информатика'
clas = 'Мажид', 'Юрий', 'Наум', 'Муслим'

#Имя пользователя
name = input("Ваше имя: ")
if name in clas:
    print("Привет! Можешь зайти!")
else:
    print("Вас нету в списках пользователей!")
    print('Ну ладно, можете войти')
#Вывод существующих предметов
print('')

print("Наши предметы:", pred)

#Выбор предмета
test = input('Какой предмет вы хотите выбрать? ')
print('')

if (test.lower() == "информатика"):
    informatic()
else:
    print("Пока что этого у нас нет")

