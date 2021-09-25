import mysql.connector
from tkinter import *
from tkinter import messagebox

def register():
    print('register invoked')
    try:
        mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='test'
        )
        print('database connected....')
        mycursor=mydb.cursor()
        query='insert into mitali_student(Username,Password)values(%s,%s)'
        Username=str(t1.get())
        Password=str(t2.get())
        value=(Username,Password)
        mycursor.execute(query,value)
        mydb.commit()
        messagebox.showinfo("Success",'record inserted successfully')
        window.destroy()
    except Exception as e:
        print('msg:',e)
window=Tk()

window. configure(background="skyblue")
window .title('Registration-App')

heading=Label(window,text="Registration Form",font=('Arial Bold',42),fg='black')
l1=Label(window,text="Username",font=('Arial Bold',18),bg='yellow',fg='black')
l2=Label(window,text='Password',font=('Arial Bold',18),bg='yellow',fg='black')
t1=Entry(window,width=50,font=("Verdana",12))
t2=Entry(window,width=50,font=("Verdana",12))
b1=Button(window,text='Submit',font=('Arial Bold',16),width=16,bg='black',fg='white',relief=GROOVE,command=register)
b1.pack()
heading.place(x=580,y=200)
l1.place(x=500,y=350)
t1.place(x=650,y=350,height=30)
l2.place(x=500,y=450)
t2.place(x=650,y=450,height=30)
b1.place(x=700,y=550)

window.mainloop()
