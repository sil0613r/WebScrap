from tkinter import *
import tkinter as tk
import requests
import os
import re

root = tk.Tk()
root.title("WebScrap")
root.geometry("500x130")
root.iconbitmap('webscrap_ico.ico')
input = tk.StringVar(root)

def getvalue():
    if input.get().startswith('file://'):
        if input.get().endswith('.html') or input.get().endswith('.htm') or input.get().endswith('.php') or input.get().endswith('.js') or input.get().endswith('.css'):
            print(input.get())
            localfile = open(re.sub('file://', '', str(input.get())))
            with open('source.txt', 'w', encoding='utf-8') as f:
                f.write(localfile.read())
                os.startfile('source.txt')
        else:
            print('Not a html/htm/php/js/css file')
    else:
        print(input.get())
        r = requests.get(input.get())
        with open('source.txt', 'w', encoding='utf-8') as f:
            f.write(r.text)
            os.startfile('source.txt')

labelvar = Label(root, text="Website url:")
labelvar.pack(side = TOP, anchor=N)

entryvar = Entry(root, textvariable = input, width=50, fg="black", bd=3, selectbackground='blue').pack()

buttonvar = tk.Button(root,
                text='Get source code',
                fg='White',
                bg= 'grey', height = 2, width = 20, command=getvalue).pack()

root.mainloop()

try:
    os.remove('source.txt')
except:
    print('No source code generated')
