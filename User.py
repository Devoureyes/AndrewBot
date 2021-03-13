class User(object):
    def __init__(self, numberOfQuestion, points, start, id):
        """Constructor"""
        self.numberOfQuestion = numberOfQuestion
        self.points = points
        self.start = start
        self.id = id

    def getResult(self):
        points = self.points
        if (points >= 0 and points < 5):
            return f'Ваш результат: {points} Ну что, друг? Так дела не пойдут. Надо повышать увроень фин. грамотности, а то потом поздно будет.' \
                   'Но ты на верном пути! Ты уже начал действовать и разбираться с вопросом финансов. У тебя всё получится, я верю в тебя!' \
                   '\nХотите пройти тест заного?'
        elif (points >= 5 and points <= 9):
            return f'Ваш результат: {points} Вы весьма осведомлены о своих финансах и знаете, что с ними делать. Вы думаете о том, как себя обеспечить' \
                   'и заботитесь о своём фин. здоровье. Продолжайте в том же духе' \
                   '\nХотите пройти тест заного?'
        elif (points >= 10 and points <= 12):
            return f'Ваш результат: {points} Отличный результат. Твой уровень финансовой грамотности выше 90% населения России. Хоть сейчас идти' \
                   ' работать финансовым консультантом.' \
                   '\nХотите пройти тест заного?'

    def start_test(self, replica, questions):
        # global start
        if replica == "да":
            self.points = 0
            self.numberOfQuestion = 0
            self.start = 1
            # global points
            # global numberOfQuestion
            # numberOfQuestion = 0
            # points = 0
            # start = 1
            return questions[self.numberOfQuestion]
        elif replica == "нет":
            self.start = 0
            # start = 0
            return "Хотите пройти тест?"

    def clear_phrase(self, phrase):
        phrase = phrase.lower()
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- '
        result = ''.join(symbol for symbol in phrase if symbol in alphabet)
        if (result == "да") or (result == "нет"):
            return result.strip()
        else:
            return False

    def correctAnswer(self, replica, questions):
        # global numberOfQuestion  # получаем номер вопроса
        if (self.numberOfQuestion != len(questions)):  # если номер вопроса не равен длине массива, то выполняем
            if (replica == 'нет' or replica == 'да'):  # Если введено да/нет, то выполняем
                self.numberOfQuestion += 1  # увеличиваем номер вопроса
                if (replica == "да"):  # если ответ да, то выполняем
                    # global points  # получаем глобальную переменную "очки"
                    self.points += 1  # прибавляем +1
                    return self.numberOfQuestion  # возвращаем номер вопроса
                else:
                    return self.numberOfQuestion  # возвращаем номер вопроса
        else:
            return 100