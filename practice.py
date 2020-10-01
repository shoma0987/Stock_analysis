from tkinter import *
from tkinter import ttk


def show_selection():
    for i in lb.curselection():
        print(lb.get(i))


if __name__ == '__main__':
    root = Tk()
    root.title('Scrollbar 2')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Frame
    frame = ttk.Frame(root, padding=10)
    frame.grid(sticky=(E, W, S, N))
    # frame.columnconfigure(0, weight=1)
    # frame.rowconfigure(0, weight=1)

    # Listbox
    currencies = ('JPY', 'USD', 'EUR', 'CNY', 'MXN', 'CAD')
    v1 = StringVar(value=currencies)
    lb = Listbox(frame, listvariable=v1, height=3)
    lb.grid(row=0, column=0, sticky=(E, W, S, N))

    # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame,
        orient=VERTICAL,
        command=lb.yview)
    lb['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0, column=1, sticky=(N, S))

    # Button
    button1 = ttk.Button(
        frame, text='OK',
        command=lambda: show_selection())
    button1.grid(
        row=1, column=0, columnspan=2,
        pady=5, sticky=(S))

    root.mainloop()