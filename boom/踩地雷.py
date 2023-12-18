import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger
import random

class MinesweeperGame:
    def __init__(self, master, rows=None, cols=None, mines=None):
        self.master = master

        # 詢問大小設定
        if rows is None or cols is None or mines is None:
            self.set_size_and_mines()
        # 圖片 A（標記的炸彈）
        self.mine_flag_image = tk.PhotoImage(file="A.png")  # 替換成您的圖片檔案路徑
        # 圖片 B（失敗時顯示的炸彈）
        self.mine_image = tk.PhotoImage(file="B.png")  # 替換成您的圖片檔案路徑

        self.board = self.initialize_board()
        self.revealed = [[False] * self.cols for _ in range(self.rows)]
        self.flags = [[False] * self.cols for _ in range(self.rows)]

        self.create_widgets()

    def initialize_board(self):
        board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        mine_positions = random.sample(range(1, self.rows * self.cols + 1), self.mines)

        for mine_pos in mine_positions:
            row = (mine_pos - 1) // self.cols
            col = (mine_pos - 1) % self.cols
            board[row][col] = 'M'

        return board

    def create_widgets(self):
        self.buttons = [[None] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                button = tk.Button(self.master, text=' ', width=4, height=2,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j)
                button.bind('<ButtonRelease-3>', lambda event, row=i, col=j: self.handle_right_click(row, col))  # 綁定右鍵事件
                self.buttons[i][j] = button

        # 設定焦點為第一個按鈕
        self.buttons[0][0].focus_set()

    def handle_click(self, row, col):
        if self.flags[row][col]:
            return  # Skip click on flagged cells

        if self.board[row][col] == 'M':
            self.game_over()
        else:
            self.reveal_cell(row, col)
            if self.check_win():
                self.game_won()

    def reveal_cell(self, row, col):
        if self.revealed[row][col]:
            return

        self.revealed[row][col] = True
        mines_nearby = self.count_adjacent_mines(row, col)

        if mines_nearby == 0:
            for i in range(max(0, row - 1), min(self.rows, row + 2)):
                for j in range(max(0, col - 1), min(self.cols, col + 2)):
                    self.reveal_cell(i, j)
        else:
            self.buttons[row][col].configure(text=str(mines_nearby))

        # 更改已揭示區域的背景色
        self.buttons[row][col].configure(bg='darkgray')

    def count_adjacent_mines(self, row, col):
        count = 0

        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if self.board[i][j] == 'M':
                    count += 1

        return count

    def mark_flag(self, row, col):
        if not self.revealed[row][col]:
            self.flags[row][col] = not self.flags[row][col]
            if self.flags[row][col]:
                self.buttons[row][col].configure(image=self.mine_flag_image)  # 使用圖片 A
            else:
                self.buttons[row][col].configure(image='', text=' ')

    def game_over(self):
        messagebox.showinfo("Game Over", "You hit a mine!")

        # 顯示所有炸彈位置並使用圖片 B
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'M':
                    self.buttons[i][j].configure(image=self.mine_image)

        self.reset_game()
    def check_win(self):
        revealed_count = sum(row.count(True) for row in self.revealed)
        total_cells = self.rows * self.cols
        non_mine_cells = total_cells - self.mines

        return revealed_count == non_mine_cells

    def game_won(self):
        messagebox.showinfo("Congratulations!", "You won!")
        self.reset_game()

    def reset_game(self):
        # 清除舊的按鈕
        if hasattr(self, 'buttons') and self.buttons:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.buttons[i][j].grid_forget()
            self.buttons = None  # 將按鈕列表設為 None，以確保再次創建新的按鈕

        # 重新初始化遊戲
        self.board = self.initialize_board()
        self.revealed = [[False] * self.cols for _ in range(self.rows)]
        self.flags = [[False] * self.cols for _ in range(self.rows)]

        # 創建新的按鈕
        self.create_widgets()

    def set_size_and_mines(self):
        self.rows = askinteger("Set Size and Mines", "輸入長度:", parent=self.master)
        self.cols = askinteger("Set Size and Mines", "輸入寬度:", parent=self.master)
        self.mines = askinteger("Set Size and Mines", "炸彈數量:", parent=self.master)

        if self.rows is None or self.cols is None or self.mines is None:
            # 如果使用者取消了詢問，可以設定一個預設值或採取其他行動
            self.rows, self.cols, self.mines = 5, 5, 4

    def handle_right_click(self, row, col):
        # 檢查右鍵是否點擊在已開啟的區域
        if self.revealed[row][col]:
            # 開始周圍未標記炸彈的格子
            mines_nearby = self.count_adjacent_mines(row, col)
            flagged_count = 0

            for i in range(max(0, row - 1), min(self.rows, row + 2)):
                for j in range(max(0, col - 1), min(self.cols, col + 2)):
                    if self.flags[i][j]:
                        flagged_count += 1

            if mines_nearby == flagged_count:
                for i in range(max(0, row - 1), min(self.rows, row + 2)):
                    for j in range(max(0, col - 1), min(self.cols, col + 2)):
                        if not self.revealed[i][j] and not self.flags[i][j]:
                            self.handle_click(i, j)

        # 在未開啟的區域按下右鍵，切換標記為旗子
        self.mark_flag(row, col)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")

    game = MinesweeperGame(root)

    root.mainloop()