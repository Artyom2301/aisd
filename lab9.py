from tkinter import Tk, Button, Label, messagebox, Frame, Radiobutton, IntVar

# Размеры игрового поля
ROWS = 3
COLS = 3


class TicTacToe:
    def __init__(self):
        """
        Конструктор класса, инициализирует главное окно и создает начальный экран.
        """
        self.window = Tk()  # Создаем основное окно приложения
        self.window.title("Крестики-Нолики")  # Устанавливаем заголовок окна
        self.buttons = []  # Список кнопок игрового поля
        self.create_start_screen()  # Вызываем метод создания начального экрана

    def create_start_screen(self):
        """
        Создает начальный экран с выбором первого игрока.
        """
        frame = Frame(self.window)  # Создаем фрейм для размещения виджетов
        label = Label(frame, text="Кто ходит первым?", font=('Arial', 16))  # Заголовок выбора
        label.grid(row=0, column=0, pady=(10, 0), columnspan=2)  # Размещаем заголовок

        self.first_player_var = IntVar(value=1)  # Переменная для хранения значения выбранного игрока
        human_radio = Radiobutton(
            frame, text="Человек", variable=self.first_player_var, value=1
        )  # Радиокнопка для выбора человеком
        human_radio.grid(row=1, column=0, padx=(10, 0))  # Размещение радиокнопки

        computer_radio = Radiobutton(
            frame, text="Компьютер", variable=self.first_player_var, value=2
        )  # Радиокнопка для выбора компьютером
        computer_radio.grid(row=1, column=1, padx=(10, 0))  # Размещение радиокнопки

        start_button = Button(frame, text="Начать игру", command=self.start_game)  # Кнопка начала игры
        start_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))  # Размещение кнопки

        frame.grid()  # Размещение фрейма

    def start_game(self):
        """
        Начинает игру после выбора первого игрока.
        """
        first_player = self.first_player_var.get()  # Получение значения выбранного игрока
        if first_player == 1:
            self.current_player = 'X'  # Человек ходит первым
        else:
            self.current_player = 'O'  # Компьютер ходит первым

        # Удаляем старое окно и создаем новое
        self.window.destroy()  # Закрываем стартовый экран
        self.window = Tk()  # Создаем новое окно
        self.window.title("Крестики-Нолики")  # Устанавливаем новый заголовок

        # Очищаем список кнопок
        self.buttons.clear()

        for i in range(ROWS):  # Проходим по всем рядам
            row_buttons = []  # Список кнопок текущего ряда
            for j in range(COLS):  # Проходим по всем колонкам
                btn = Button(
                    self.window,
                    text=" ",
                    font=('Arial', 20),
                    width=6,
                    height=3,
                    command=lambda x=i, y=j: self.click_button(x, y),
                )
                btn.grid(row=i, column=j)  # Размещаем кнопку в сетке
                row_buttons.append(btn)  # Добавляем кнопку в список кнопок ряда
            self.buttons.append(row_buttons)  # Добавляем ряд кнопок в общий список

        # Сбрасываем счетчик ходов
        self.turn_count = 0
        # Сбрасываем массив состояния игрового поля
        self.board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

        if self.current_player == 'O':  # Если компьютер ходит первым
            self.computer_move()  # Делаем первый ход компьютера

    def click_button(self, x, y):
        """
        Обрабатывает нажатие на кнопку игрового поля.
        :param x: номер строки
        :param y: номер столбца
        """
        if self.board[x][y] == ' ':  # Если клетка пустая
            self.buttons[x][y].config(text=self.current_player)  # Помещаем символ в кнопку
            self.board[x][y] = self.current_player  # Заполняем клетку на игровом поле
            self.turn_count += 1  # Увеличиваем счетчик ходов

            if self.check_win():  # Проверяем, выиграл ли игрок
                messagebox.showinfo("Победитель!", f"Победил {self.current_player}")  # Показываем сообщение о победе
                self.ask_to_replay()  # Предлагаем сыграть заново
            elif self.turn_count >= ROWS * COLS:  # Если все клетки заполнены
                messagebox.showinfo("Ничья!", "Игра закончилась вничью!")  # Сообщаем о ничьей
                self.ask_to_replay()  # Предлагаем сыграть заново
            else:
                self.change_player()  # Меняем текущий игрок

                if self.current_player == 'O':  # Если теперь ходит компьютер
                    self.computer_move()  # Делаем ход компьютера

    def ask_to_replay(self):
        """
        Предлагает игроку начать новую игру с выбором первого игрока.
        """
        result = messagebox.askyesno("Продолжить?", "Хотите сыграть еще раз?")  # Спрашиваем, хочет ли игрок продолжить
        if result:  # Если да
            self.create_start_screen()  # Возвращаемся к начальному экрану
        else:
            self.window.destroy()  # Иначе закрываем приложение

    def computer_move(self):
        """
        Реализует ход компьютера с использованием алгоритма минимакса.
        """
        best_score = float('-inf')  # Лучшая оценка хода
        best_move = None  # Координаты лучшего хода

        for i in range(ROWS):  # Проходим по всем рядам
            for j in range(COLS):  # Проходим по всем колонкам
                if self.board[i][j] == ' ':  # Если клетка пустая
                    self.board[i][j] = 'O'  # Времено ставим крестик
                    score = self.minimax(self.board, False)  # Оцениваем этот ход
                    self.board[i][j] = ' '  # Восстанавливаем состояние клетки

                    if score > best_score:  # Если найден лучший ход
                        best_score = score  # Сохраняем оценку
                        best_move = (i, j)  # Сохраняем координаты

        if best_move is not None:  # Если найдем лучший ход
            i, j = best_move  # Разбираем координаты
            self.board[i][j] = 'O'  # Ставим крестик на лучшее место
            self.buttons[i][j].config(text='O')  # Отображаем крестик на кнопке
            self.turn_count += 1  # Увеличиваем счетчик ходов

            if self.check_win():  # Проверяем, выиграл ли компьютер
                messagebox.showinfo("Победитель!", "Выиграл компьютер!")  # Сообщаем о победе компьютера
                self.ask_to_replay()  # Предлагаем сыграть заново
            elif self.turn_count >= ROWS * COLS:  # Если все клетки заполнены
                messagebox.showinfo("Ничья!", "Игра закончилась вничью!")  # Сообщаем о ничьей
                self.ask_to_replay()  # Предлагаем сыграть заново
            else:
                self.change_player()  # Передаем ход человеку

    def minimax(self, board, maximizing):
        """
        Реализация алгоритма минимакса для нахождения оптимального хода.
        :param board: текущее состояние игрового поля
        :param maximizing: признак максимизирующего игрока
        :return: оценка позиции
        """
        winner = self.get_winner(board)  # Определяем победителя
        if winner == 'X':  # Если победил X
            return -1  # Минимальная оценка
        elif winner == 'O':  # Если победил O
            return 1  # Максимальная оценка
        elif self.is_board_full(board):  # Если доска заполнена
            return 0  # Ничья

        if maximizing:  # Максимизация (ход компьютера)
            best_score = float('-inf')  # Наименьшая возможная оценка
            for i in range(ROWS):  # Проходим по всем рядам
                for j in range(COLS):  # Проходим по всем колонкам
                    if board[i][j] == ' ':  # Если клетка пустая
                        board[i][j] = 'O'  # Ставим крестик
                        score = self.minimax(board, False)  # Рекурсивно вызываем минимакс
                        board[i][j] = ' '  # Восстанавливаем состояние клетки
                        best_score = max(best_score, score)  # Обновляем лучшую оценку
            return best_score  # Возвращаем максимальную оценку
        else:  # Минимизация (ход человека)
            best_score = float('inf')  # Наибольшая возможная оценка
            for i in range(ROWS):  # Проходим по всем рядам
                for j in range(COLS):  # Проходим по всем колонкам
                    if board[i][j] == ' ':  # Если клетка пустая
                        board[i][j] = 'X'  # Ставим нолик
                        score = self.minimax(board, True)  # Рекурсивно вызываем минимакс
                        board[i][j] = ' '  # Восстанавливаем состояние клетки
                        best_score = min(best_score, score)  # Обновляем лучшую оценку
            return best_score  # Возвращаем минимальную оценку

    def get_winner(self, board):
        """
        Определяет победителя по текущему состоянию игрового поля.
        :param board: текущее состояние игрового поля
        :return: символ победителя ('X', 'O') или None, если нет победителя
        """
        for i in range(ROWS):  # Проходим по всем рядам
            if board[i][0] != ' ' and all([board[i][j] == board[i][0] for j in range(COLS)]):  # Проверяем строку
                return board[i][0]  # Возвращаем победителя

        for j in range(COLS):  # Проходим по всем колонкам
            if board[0][j] != ' ' and all([board[i][j] == board[0][j] for i in range(ROWS)]):  # Проверяем столбец
                return board[0][j]  # Возвращаем победителя

        if board[0][0] != ' ' and all([board[i][i] == board[0][0] for i in range(ROWS)]):  # Проверяем главную диагональ
            return board[0][0]  # Возвращаем победителя

        if (
            board[0][COLS - 1] != ' ' and all([board[i][COLS - i - 1] == board[0][COLS - 1] for i in range(ROWS)])
        ):  # Проверяем побочную диагональ
            return board[0][COLS - 1]  # Возвращаем победителя

        return None  # Нет победителя

    def check_win(self):
        """
        Проверяет, есть ли победитель на текущем состоянии игрового поля.
        :return: True, если есть победитель, иначе False
        """
        winner = self.get_winner(self.board)  # Определяем победителя
        return winner is not None  # Есть ли победитель?

    def change_player(self):
        """
        Переключает текущего игрока.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'  # Меняем игрока

    def is_board_full(self, board):
        """
        Проверяет, заполнено ли игровое поле полностью.
        :param board: текущее состояние игрового поля
        :return: True, если все клетки заполнены, иначе False
        """
        for i in range(ROWS):  # Проходим по всем рядам
            for j in range(COLS):  # Проходим по всем колонкам
                if board[i][j] == ' ':  # Если находим пустую клетку
                    return False  # Поле не заполнено
        return True  # Все клетки заполнены

    def start(self):
        """
        Запускает главный цикл обработки событий.
        """
        self.window.mainloop()  # Запускаем главное окно приложения

if __name__ == "__main__":
    game = TicTacToe()  # Создаем экземпляр игры
    game.start()  # Запускаем игру
