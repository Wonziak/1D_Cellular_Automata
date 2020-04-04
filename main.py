import numpy
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure





def ca1d(number, columns, rows):
    output_pattern = [int(x) for x in numpy.binary_repr(number, width=8)]
    input_pattern = numpy.zeros([8, 3])
    for i in range(8):
        input_pattern[i, :] = [int(x) for x in numpy.binary_repr(7-i, width=3)]
    canvas = numpy.zeros([rows, columns+3])
    canvas[0, int(columns/2)+1] = 1
    for i in numpy.arange(0, rows-1):
        for j in numpy.arange(0, columns+1):
            canvas[i, 0] = canvas[i, columns+1]
            canvas[i, columns+2] = canvas[i, 1]
            for k in range(8):
                if numpy.array_equal(input_pattern[k, :], canvas[i, j:j+3]):
                    canvas[i+1, j+1] = output_pattern[k]

    plt.imshow(canvas[:, 1:columns+1], cmap='Greys', interpolation='nearest')
    plt.title("automaty komorkowe 1D regula {} periodyczne".format(number))
    plt.show()


def ca1dnotperiodic(number, columns, rows):
    output_pattern = [int(x) for x in numpy.binary_repr(number, width=8)]
    input_pattern = numpy.zeros([8, 3])
    for i in range(8):
        input_pattern[i, :] = [int(x) for x in numpy.binary_repr(7-i, width=3)]
    canvas = numpy.zeros([rows, columns+2])
    canvas[0, int(columns/2)+1] = 1
    for i in numpy.arange(0, rows-1):
        for j in numpy.arange(0, columns):
            for k in range(8):
                if numpy.array_equal(input_pattern[k, :], canvas[i, j:j+3]):
                    canvas[i+1, j+1] = output_pattern[k]
    plt.imshow(canvas[:, 1:columns+1], cmap='Greys', interpolation='nearest')
    plt.title("automaty komorkowe 1D regula {} statyczny".format(number))
    plt.show()



def rysujwykres(event):
    number = int(entry_1.get())
    if number > 255:
        number = 255
    columns = int(entry_2.get())
    if columns < 0:
        columns = 1
    rows = int(entry_3.get())
    if rows < 0:
        rows = 1
    ca1d(number, columns, rows)


def rysujwykresnieper(event):
    number = int(entry_1.get())
    if number > 255:
        number = 255
    columns = int(entry_2.get())
    if columns < 0:
        columns = 1
    rows = int(entry_3.get())
    if rows < 0:
        rows = 1
    ca1dnotperiodic(number, columns, rows)


root = Tk()
root.wm_title("CA1D")
topFrame = Frame(root, width=300, height=250)
topFrame.pack(side=TOP)
botFrame = Frame(root, width=300, height=250)
botFrame.pack(side=BOTTOM)

fig = Figure(figsize=(5, 4), dpi=100)
Przycisk = Button(topFrame, text="Rysuj", fg="red")
Przycisk2 = Button(topFrame, text="Rysuj statyczny", fg="red")
label_1 = Label(topFrame, text="Regula")
label_2 = Label(topFrame, text="Szerokosc")
label_3 = Label(topFrame, text="Krok")
entry_1 = Entry(topFrame)
entry_2 = Entry(topFrame)
entry_3 = Entry(topFrame)
label_1.grid(row=0, sticky=W)
label_2.grid(row=0, column=3)
label_3.grid(row=0, column=5)

entry_1.grid(row=0, column=2)
entry_1.grid(row=0, column=2)
entry_2.grid(row=0, column=4)
entry_3.grid(row=0, column=6)
Przycisk.grid(row=0, column=7)
Przycisk2.grid(row=0, column=8)
Przycisk.bind("<Button-1>", rysujwykres)
Przycisk2.bind("<Button-1>", rysujwykresnieper)
root.mainloop()





