import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers=[
    "python",
    "java",
    "swift",
    "canada",
    "India",
    "America",
    "London",
    "count",
    "program",
    "package",
]

words=[
    "nptoyh",
    "ajva",
    "wfsit",
    "cdanaa",
    "aIdin",
    "Aiearcm",
    "odnLon",
    "tocnu",
    "rargopm",
    "egakcap",
]
num=random.randrange(0,len(words),1)
def default():
    global words,answers,num
    lbl.config(text=words[num])
def res():
    global words, answers, num
    num = random.randrange(0, len(words), 1)
    lbl.config(text=words[num])
    e1.delete(0,END)

def checkans():
    global words ,answers,num
    var=e1.get()
    if var==answers[num]:
        messagebox.showinfo("Success","This Is Correct Answer")
    else:
        messagebox.showinfo("Error","This Is Not Correct")
        e1.delete(0,END)

root=tkinter.Tk()
root.geometry("300x400+400+300")
root.title("Jumbbled")
root.configure(background="pink")

lbl=Label(root,text="Your here",font=("Verdana",18),bg="yellow",fg="black")
lbl.pack(pady=30,ipady=10,ipadx=10)

ans1=StringVar()
e1=Entry(root,font=("Verdana",16),textvariable=ans1)
e1.pack(ipady=5,ipadx=5)

btncheck=Button(root,text="Check",font=("Comic sans ms",16),width=16,fg="white",bg="black",relief=GROOVE,
                command=checkans,)
btncheck.pack(pady=40)
btnreset=Button(root,text="Reset",font=("Comic sans ms",16),width=16,fg="white",bg="black",relief=GROOVE,
                command=res,)
btnreset.pack()

default()
root.mainloop()