import random


print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос', 'Как тебя зовут?', sep='\n')
print('Привет,', input())

variances = [['Бесспорно', 'Всё будет', '100%', 'Да!'],
    ['Возможно', 'Может быть', 'Не могу предположить', 'Вполне возможно, но', 'Есть но', 'Фифти-фифти', 'Выражаю нерешительность'],
    ['Нет', 'Не произойдёт', 'Никак нет', 'Вряд-ли', 'Не будет', 'Точно не это']]

def choice_(answers):
    num_mood = random.randint(0, 2)
    right_wall = len(answers[num_mood]) - 1
    num_item_in = random.randint(0, right_wall)

    return answers[num_mood][num_item_in]

flag = True
counter_questions = 0

while flag == True:
    if counter_questions == 0:
        print('Будешь задавать вопрос')
        text = input()

        if 'да' in text.lower():
            print('Давай)')
            question = input()
            print(choice_(variances))
        else:
            flag = False
            print('Был рад с тобой иметь дело! Даже если ты и не задал вопрос))')
    else:
        rand_index = random.randint(0, 1)
        if rand_index == 0:
            print('Ещё вопрос?)')
        else:
            print('Задашь ещё вопрос?')
        
            text = input()

            if 'да' in text.lower():
                print('Давай)')
                question = input()
                print(choice_(variances))
            else:
                flag = False
                print('Был рад с тобой иметь дело!')
    
    counter_questions += 1