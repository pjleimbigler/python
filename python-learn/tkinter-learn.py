#!/usr/bin/env python

import Tkinter as tk

class App:
    def __init__(self, parent):
        frame = tk.Frame(parent)
        frame.pack()

        btn1 = tk.Button(frame, text='1', command=lambda: self.printNum(1))
        btn1.pack(side=tk.LEFT)
        btn2 = tk.Button(frame, text='2', command=lambda: self.printNum(2))
        btn2.pack(side=tk.LEFT)
        btn3 = tk.Button(frame, text='3', command=lambda: self.printNum(3))
        btn3.pack(side=tk.LEFT)
        quitBtn = tk.Button(frame, text="quit", fg="red", command=frame.quit)
        quitBtn.pack(side=tk.LEFT)

    def printNum(self, num):
        print "You pressed button %s." % num

if __name__ == '__main__':
    tkroot = tk.Tk()
    app = App(tkroot)
    tkroot.mainloop()
