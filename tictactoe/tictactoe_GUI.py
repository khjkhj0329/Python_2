import tkinter

from tictactoe_game_engine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300  # 창 크기
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')    #300*300
        self.root.resizable(width=False, height=False)  # 크기가 조절이 안된다.

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}    #{'X': PhotoImage객체, 'O': PhotoImage객체}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)  # 클릭핸들러에 가로가 없다 지금 시작하는것이 아니다. 😻😻
        self.root.mainloop()

    def click_handler(self, event):
        print('click')

    def draw_board(self):
        pass

if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()
