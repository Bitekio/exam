class Question:
    def init(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.prompt)
        for idx, option in enumerate(self.options):
            print(f"{idx + 1}. {option}")
        
        try:
            user_answer = int(input("Введите номер вашего ответа: "))
            return user_answer == self.correct_answer
        except ValueError:
            print("Некорректный ввод. Введите номер варианта ответа целым числом.")
            return False


class Quiz:
    def init(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            if question.display_question():
                self.score += 1
        print(f"Вы ответили правильно на {self.score}/{len(self.questions)} вопросов.")


questions = [
    Question("Сколько планет в Солнечной системе?", ["6", "7", "8", "9"], 3),
    Question("Какая самая высокая гора на Земле?", ["Эверест", "Килиманджаро", "Аконкагуа", "Мак-Кинли"], 1),
    Question("Как называется столица Франции?", ["Мадрид", "Берлин", "Лондон", "Париж"], 4)
]

quiz = Quiz(questions)
quiz.run_quiz()
