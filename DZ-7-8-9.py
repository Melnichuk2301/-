import sqlite3

# Создание базы данных и подключение к ней
conn = sqlite3.connect('jokes.db')
cursor = conn.cursor()

# Создание таблицы 'Jokes'
cursor.execute('''CREATE TABLE IF NOT EXISTS Jokes
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   joke TEXT)''')

# Вставка анекдотов в таблицу 'Jokes'
jokes = [
    'Какой самый частый вопрос у программиста? - "А это будет работать?"',
    'Как программист заправляет машину? - Пишет клиенту API для самозаправки',
    'Кто такие программисты-интроверты? - Те, кто предпочитает взаимодействовать с компьютером, а не с людьми',
    'Что говорит программа приколист? - "Я шутка-загадка. Разгадай меня!"',
    'Почему программисты не любят ходить на пикник? - Они боятся букашек в коде'
]

for joke in jokes:
    cursor.execute("INSERT INTO Jokes (joke) VALUES (?)", (joke,))

import tkinter as tk


class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Joke App")

        # Создание кнопки
        self.button = tk.Button(self.root, text="Случайный анекдот", command=self.get_joke)
        self.button.pack()

        # Создание текстового виджета
        self.text = tk.Text(self.root, height=10, width=50)
        self.text.pack()

        # Подключение к базе данных
        self.conn = sqlite3.connect('jokes.db')
        self.cursor = self.conn.cursor()

    def get_joke(self):
        # Очистка текстового виджета
        self.text.delete(1.0, tk.END)

        # Выбор случайного анекдота из базы данных
        self.cursor.execute("SELECT joke FROM Jokes ORDER BY RANDOM() LIMIT 1;")
        joke = self.cursor.fetchone()[0]

        # Вставка анекдота в текстовый виджет
        self.text.insert(tk.END, joke)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    app.run()

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()