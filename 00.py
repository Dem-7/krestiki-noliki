import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print("Произошла ошибка:", e)

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Получаем английское слово и его определение
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский
        tt = translator.translate(word, dest='ru').text
        nn = translator.translate(word_definition, dest='ru').text

        # Начинаем игру
        print(f"Значение слова - {nn}")
        user = input("Что это за слово? ")
        if user == tt.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {tt}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? да/нет: ")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

word_game()