"""
Завдання 2
Створіть програму для проведення опитування або
анкетування. Зберігайте відповіді користувачів у форматі
JSON файлу. Кожне опитування може бути окремим
об'єктом у файлі JSON, а відповіді кожного користувача -
списком значень.
"""
import json

class Survey:
    def __init__(self, question, options):
        self.question = question
        self.options = options
        self.responses = []

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def collect_responses(self):
        print("Enter the number of answer (1-{0}):".format(len(self.options)))
        response = input()
        try:
            response = int(response)
            if 1 <= response <= len(self.options):
                self.responses.append(response)
                print("Your answer was saved.")
            else:
                print("Try again.")
        except ValueError:
            print("Enter a number.")

    def save_survey_results(self, filename):
        survey_data = {
            "question": self.question,
            "options": self.options,
            "responses": self.responses
        }
        with open(filename, "w") as file:
            json.dump(survey_data, file, indent=2)
        print("Results were saved to file {0}.".format(filename))


def question():
    question = "Wat is your favorite color?"
    options = ["Yellow", "Black", "Blue", "Red", "Other"]

    survey = Survey(question, options)


    survey.display_question()
    survey.collect_responses()

    survey.save_survey_results("survey_results.json")

question()
