from tkinter import *
from PIL import Image
import json
import os

def Excel():
    os.system('start excel.exe Книга1.xlsx')

def Txt():
    os.system('start notepad.exe TxtFile.txt')

def Graphic():
    img = Image.open('graphic.png')
    img.show()

def Tablica():
    img = Image.open('tablica.png')
    img.show()

def Json():
    with open('data.json', 'r', encoding='utf8') as f:
        text = json.load(f)
        print(text)
        


root = Tk()
root.geometry('800x600')

def main(event):
    MainFrame = Frame(root)
    MainFrame.pack()

    TextBox = Text(MainFrame, width=500, undo=True)
    TextBox.pack(fill=BOTH)

button = Button(text = 'Таблиця excel', command=Excel)
button.pack()



button2 = Button(text = 'Текстовий документ', command=Txt)
button2.pack()



button3 = Button(text = 'Файл JSON (вивід у термінал)', command=Json)
button3.pack()



button4 = Button(text = 'Графік проекту', command=Graphic)
button4.pack()


button5 = Button(text = 'Таблиця', command=Tablica)
button5.pack()


button6 = Button(text="Вийти", command=lambda: quit_program())
def quit_program():
    root.destroy()
button6.pack()
root.mainloop()

root.mainloop()