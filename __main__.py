from tkinter import *

# This var shows whose turn is now
# True = X's turn, False = 0's turn
turn = False

# This will contain all cell combinations to win the game
win_condition_set = list()


class Cell:
    """Button with own text variable and command

    Every button has self command and all of them refer to Field->check_field() to check, did one of players win or not
    """
    def __init__(self):
        self.text = StringVar()
        self.is_clicked = 0
        self.btn = Button(textvariable=self.text, width=6, height=3, command=self.click)

    def click(self):
        global turn
        if self.is_clicked:
            return
        else:
            self.is_clicked += 1
        turn = not turn
        if turn:
            self.text.set('X')
        else:
            self.text.set('0')
        Field.check_field()


class Field:
    """Matrix 3x3 of Cells
    """
    def __init__(self):
        self.field = [[Cell() for i in range(3)] for ii in range(3)]
        for ii in range(3):
            for i in range(3):
                self.field[ii][i].btn.grid(row=ii, column=i)

    def check_field(self):
        """This will iterate on win_condition_set to check, is this combo of cells only X or 0"""
        pass


if __name__ == '__main__':
    root = Tk()
    root.title('X-0')

    game = Field()

    comment_text = StringVar()
    comment_text.set('Тестовый текст')
    comment = Label(textvariable=comment_text)

    comment.grid(row=3, column=0, columnspan=3)

    root.mainloop()