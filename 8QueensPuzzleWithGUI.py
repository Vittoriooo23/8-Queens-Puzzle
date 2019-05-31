'''
==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
|||-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯|||
==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
    Project: 8 Queens Puzzle
    Class: CSC_480
    Authors:{
        Michael Bajor
        Vittorio Russo
        William Fenley
    }
==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
|||-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯|||
==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
'''

from tkinter import *


# ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
# |||   UI    |||-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯|||
# ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
class UI:
    def __init__(self, _root, queen_puzzle):
        self.dark_gray = "#434447"
        self.light_gray = "#696b72"
        self.queen_puzzle = queen_puzzle
        self.current_board_display_index = 0

        self.main_frame = Frame(_root, bg=self.light_gray)
        self.main_frame.grid()

        # Renders the whole window
        self.render_window()

        _root.bind('<Right>', self.get_next_board_right_keypress)
        _root.bind('<Left>', self.get_next_board_left_keypress)
        
    def render_title(self, light_gray):
        self.title = Label(self.main_frame, text="8 Queens Puzzle", width=20,
                           bg=light_gray, borderwidth=3, relief="groove")
        self.title.config(font=40)
        self.title.grid(row=0, column=0, padx=30, pady=15, ipady=10)
        
    def render_counter(self, light_gray):
        self.counter_frame = Frame(self.main_frame, bg=light_gray)
        self.counter_frame.grid(row=2, column=0, pady=10)

        self.left_button = Button(self.counter_frame, text="<<", bg=light_gray, command=self.get_next_board_left)
        self.left_button.grid(row=0, column=0, padx=15)

        self.index_label = Label(self.counter_frame, text="Solution", bg=light_gray)
        self.index_label.grid(row=0, column=1)

        self.b_index = StringVar()
        self.b_index.set(self.current_board_display_index+1)
        self.board_index = Label(self.counter_frame, textvariable=self.b_index, bg=light_gray)
        self.board_index.grid(row=0, column=2, pady="10")

        self.right_button = Button(self.counter_frame, text=">>", bg=light_gray,
                                   command=self.get_next_board_right)
        self.right_button.grid(row=0, column=3, padx=15)

# Work Zone ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==-
    # If color = True, it is white, else it is black
    def render_board(self):
        self.board = Frame(self.main_frame, borderwidth=3, relief="sunken")
        self.board.grid(row=1, column=0, padx="15")
        color = True
        for row in range(8):
            self.render_row(color, row)  # parameters: bool(color), queen index for row
            if row != 7:
                color = not color

    def render_row(self, first_color, row):
        color = first_color

        for col in range(8):
            queen_index = self.queen_puzzle.allSolutions[self.current_board_display_index][row]

            if col == queen_index:
                is_empty = False
            else:
                is_empty = True
            self.render_square(color, is_empty, row, col)
            color = not color

    def render_square(self, color, is_empty_square, row, col):
        dark_square = "#2b2c2d"
        light_square = "#b5b9bf"
        square_color = None
        text_color = None

        if color == True:
            square_color = dark_square
            text_color = light_square
        elif color == False:
            square_color = light_square
            text_color = dark_square

        content_text = StringVar()
        if is_empty_square == True:
            content_text.set("")
        elif is_empty_square == False:
            content_text.set("♀")

        self.square = Label(self.board, width=6, height=3, textvariable=content_text, bg=square_color, fg=text_color)
        self.square.grid(row=row, column=col)
        
    def render_window(self):
        self.render_title(self.light_gray)
        self.render_board()
        self.render_counter(self.light_gray)
        self.queen_puzzle.print_board(self.current_board_display_index)

    # Two identical functions for different parameter requirements for both get_next_right and get_next_left
    def get_next_board_right(self):
        print("change to board right executed", )
        self.current_board_display_index = (self.current_board_display_index + 1) % 92
        self.b_index.set(self.current_board_display_index+1)
        self.render_window()

    def get_next_board_right_keypress(self, event):
        print("change to board right executed", )
        self.current_board_display_index = (self.current_board_display_index + 1) % 92
        self.b_index.set(self.current_board_display_index+1)
        self.render_window()

    def get_next_board_left(self):
        print("change to board left executed")
        self.current_board_display_index = self.current_board_display_index - 1
        if self.current_board_display_index < 0:
            self.current_board_display_index = 91
        self.b_index.set(self.current_board_display_index+1)
        self.render_window()

    def get_next_board_left_keypress(self, event):
        print("change to board left executed")
        self.current_board_display_index = self.current_board_display_index - 1
        if self.current_board_display_index < 0:
            self.current_board_display_index = 91
        self.b_index.set(self.current_board_display_index+1)
        self.render_window()


# ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
# |||     8 Queens Puzzle Integration     |||-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_|||
# ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
class QueensProblem:
    numSolutions = 0
    allSolutions = [[0 for x in range(8)] for y in range(92)] 
    test = [[0 for x in range(8)] for y in range(92)]
    
    def __init__(self):
        positions = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.recursiveQueen(positions, 0)

    def get_numSolutions(self):
        return self.numSolutions

    def recursiveQueen(self, positions, row):
        if row != 8:
            for column in range(8):
                if not self.checkIfUsed(positions, row, column):
                    positions[row] = column
                    self.recursiveQueen(positions, row + 1)
        else:
            self.allSolutions[self.numSolutions] = positions.copy()
            self.numSolutions += 1
            
    def checkIfUsed(self, positions, row, column):
        for i in range(row):
            if positions[i] == column or \
                 positions[i] - i == column - row or \
                 positions[i] + i == column + row:
                     return True
        return False

    def print_all_boards(self):
        self.helperFunc_board_divider()
        for each_board in range(self.numSolutions):
            self.print_board(each_board)
            self.helperFunc_board_divider()

    def print_board(self, board_index):
        # each queen_index iteration counts as a row while the
        # value passed being the queens column index
        print("Board Solution #", board_index+1)
        for queen_index in self.allSolutions[board_index]:
            self.helperFunc_print_row(queen_index)
        self.helperFunc_board_divider()

    def helperFunc_print_row(self, queen_col_index):
        self.helperFunc_print_border(queen_col_index, "top")
        self.helperFunc_print_content(queen_col_index)
        self.helperFunc_print_border(queen_col_index, "bottom")

    def helperFunc_print_content(self, queen_col_index):
        print_line = ""
        for index in range(8):
            if index == queen_col_index:
                print_line += "  Q  "
            else:
                print_line += " |+| "
        print(print_line)

    def helperFunc_print_border(self, queen_col_index, location):
        symbol = ""
        print_line = ""
        if location == "bottom":
            symbol = " ¯ "
        elif location == "top":
            symbol = " _ "
        for each in range(8):
            if each != queen_col_index:
                print_line += " " + symbol + " "
            else:
                print_line += "     "
        print(print_line)

    def helperFunc_board_divider(self):
        print_line = ""
        for each in range(19):
            print_line += "=-"
        print_line += "="
        print(print_line)


# ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
# |||     Main     |||-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-¯-_-|||
# ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==
root = Tk()
root.title("8 Queens Puzzle")

app = QueensProblem()
user = UI(root, app)

root.mainloop()
