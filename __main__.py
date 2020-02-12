from tkinter import *

# This var shows whose turn is now
# True = X's turn, False = 0's turn
turn = True

is_game_over = False

# All cell combinations to win the game
win_condition_set = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],

    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],

    [(0,0), (1,1), (2,2)],
    [(2,0), (1,1), (0,2)]
]


class Cell:
    """Button with own text variable and command

    Every button has self command and all of them refer to Field->check_field() to check, did one of players win or not
    """
    def __init__(self, master):
        self.master = master
        self.text = StringVar()
        self.is_clicked = 0
        self.btn = Button(textvariable=self.text, width=6, height=3, command=self.click)

    def click(self):
        global turn
        if self.is_clicked or is_game_over:
            return
        else:
            self.is_clicked += 1
        if turn:
            self.text.set('X')
        else:
            self.text.set('0')
        self.master.check_field()
        turn = not turn

class Field:
    """Matrix 3x3 of Cells
    """
    def __init__(self):
        self.field = [[Cell(master=self) for i in range(3)] for ii in range(3)]
        for ii in range(3):
            for i in range(3):
                self.field[ii][i].btn.grid(row=ii, column=i)


    def check_field(self):
        """This will iterate on win_condition_set to check, is this combo of cells only X or 0
        """
        global is_game_over
        for a, b, c in win_condition_set:
            if self.field[a[0]][a[1]].text.get() == 'X' or self.field[a[0]][a[1]].text.get() == '0':
                if self.field[a[0]][a[1]].text.get() == self.field[b[0]][b[1]].text.get() == self.field[c[0]][c[1]].text.get():
                    comment_text.set('Победил ' + self.field[a[0]][a[1]].text.get())
                    is_game_over = True
                    return
        if turn:
            # If is was X's turn, now it is 0's turn
            comment_text.set('Ходит 0')
        else:
            comment_text.set('Ходит X')


def new_game():
    global field
    global turn
    global is_game_over

    turn = True
    is_game_over = False
    del field
    field = Field()
    comment_text.set('Ходит X')

if __name__ == '__main__':
    root = Tk()
    root.title('X-0')

    main_menu = Menu(root)
    root.config(menu=main_menu)
    main_menu.add_command(label="Новая игра", command=new_game)

    field = Field()

    comment_text = StringVar()
    comment_text.set('Крестики-нолики v1')
    comment = Label(textvariable=comment_text)

    comment.grid(row=3, column=0, columnspan=3)

    root.mainloop()