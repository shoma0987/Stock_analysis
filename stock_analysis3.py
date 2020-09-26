# scroll bar

import tkinter
from tkinter import *


with open("stock_225.txt","r",encoding="utf-8", errors="ignore") as f:
    r = f.read()
N225 = list(r.split())
# print(N225)

a225,b225 =[],[]
for i in range(0,450,2):
   a225.append(N225[i])
for j in range(1,450,2):
   b225.append(N225[j])

window = Tk()
scrollBar = Scrollbar(window, orient=tkinter.VERTICAL)
#スクロールバーのwidthは一番長い文字列に合わせる
scrollBar.pack(side=RIGHT, fill=Y)
window.title("N225")


#スクロールバー
myList = Listbox(window, height= 17, width= 25, yscrollcommand= scrollBar.set)
for line in range(225):
    myList.insert(END, a225[line]+" : "+b225[line])

#ラベルを作成・配置する
label1 = tkinter.Label(window,
                       text="東証1部上場会社リスト",
                       foreground="red")
label1.pack()

myList.pack()
scrollBar.config(command = myList.yview)
window.mainloop() #N225をスクロールバーに表示させることまでは成功
