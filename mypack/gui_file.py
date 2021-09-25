import mysql . connector
from tkinter import *
from tkinter import messagebox


def login():
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
        query='select * from mitali_student where Username=%s and Password=%s'
        username=str(t1.get())
        password=str(t2.get())
        value=(username,password)
        mycursor.execute(query,value)
        result=mycursor.fetchall()
        if not result:
            messagebox.showinfo('result','invalid credentials')
            t1.delete(0,'end')
            t2.delete(0,'end')
        else:
            for i in result:
                messagebox.showinfo('result','sucessfully login:'+str(i[0]))
                window.destroy()
    except Exception as e:
        print('msg:',e)
window=Tk()
window .title('login-App')
window.configure(background='grey')

heading=Label(window,text="Login-Details",font=('Arial Bold',42),fg='black')
l1=Label(window,text="Username",font=('Arial Bold',18),bg='lightgreen',fg='black')
l2=Label(window,text='Password',font=('Arial Bold',18),bg='lightgreen',fg='black')
t1=Entry(window,width=50)
t2=Entry(window,width=50)
b1=Button(window,text='Login',font=('Arial Bold',16),width=16,relief=GROOVE,command=login)

heading.place(x=580,y=200)
l1.place(x=500,y=350)
t1.place(x=650,y=350,height=30)
l2.place(x=500,y=450)
t2.place(x=650,y=450,height=30)
b1.place(x=700,y=550)

window.mainloop()
