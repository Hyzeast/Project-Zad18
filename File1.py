from tkinter import *
from PIL import Image
import json
import os

def Excel():
    os.system('start excel.exe Книга1.xlsx')

def Txt():
    os.system('start notepad.exe TxtFile.txt')

def Graphic():
    img = Image.open('Graphic.png')
    img.show()

def Tablica():
    img = Image.open('Tablica.png')
    img.show()

def Json():
    os.system('start notepad.exe TxtFile.json')
        


root = Tk()
root.geometry('200x150')

def main(event):
    MainFrame = Frame(root)
    MainFrame.pack()

    TextBox = Text(MainFrame, width=500, undo=True)
    TextBox.pack(fill=BOTH)

button = Button(text = 'Таблиця excel', command=Excel)
button.place(x=1, y=1)



button2 = Button(text = 'Текстовий документ', command=Txt)
button2.place(x=1, y=25)



button3 = Button(text = 'Файл JSON (вивід у термінал)', command=Json)
button3.place(x=1, y=50)



button4 = Button(text = 'Графік проекту', command=Graphic)
button4.place(x=1, y=75)


button5 = Button(text = 'Таблиця', command=Tablica)
button5.place(x=1, y=100)


button6 = Button(text="Вийти", command=lambda: quit_program())
def quit_program():
    root.destroy()
button6.place(x=1, y=125)
root.mainloop()

root.mainloop()