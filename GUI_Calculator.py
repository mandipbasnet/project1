import  tkinter
from tkinter import *

root=Tk()
root.title('GUI Calculator')#it print title in top
root.geometry('570x600+100+200')# it show the height and weith of windo where calculator seen
root.configure(bg='black')# it make background of window black
# below code it is for where user enter number for calculation
lable_result=Label(root, width=25,height=2,font=('arial',30))
lable_result.pack()#if u dont use .pack() it does not show  in window 

equation=''# this line reset back to empty

def show(value):
      global equation
      equation +=value # it let to enter more without disturbing exiting value
      lable_result.config(text=equation)# it update the value with current value

def clear():
      global equation
      equation=''# this line reset back to empty
      lable_result.config(text=equation)

def calculate():
      global equation
      result=''
      if equation !='':
            try:
                  result=eval(equation)#itcheck the value and give answer

            except:
                  result='Error'
                  equation=''
      lable_result.config(text=result)
#bd=1: This sets the width of the button border to 1 pixel.
#fg='yello': This defines the color of the button text as "white".
#place(x=10, y=100): This method positions the button == x=10: This sets the horizontal position == and y for vertical
# #bg='white': This defines the background color of the button as "white
Button(root, text='c', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: clear()).place(x=10, y=100)
Button(root, text='/', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('/')).place(x=150, y=100)
Button(root, text='%', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('%')).place(x=290, y=100)
Button(root, text='x', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('*')).place(x=430, y=100)

Button(root, text='7', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('7')).place(x=10, y=200)
Button(root, text='8', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('8')).place(x=150, y=200)
Button(root, text='9', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('9')).place(x=290, y=200)
Button(root, text='-', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('-')).place(x=430, y=200)

Button(root, text='6', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('4')).place(x=10, y=300)
Button(root, text='5', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('5')).place(x=150, y=300)
Button(root, text='4', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('6')).place(x=290, y=300)
Button(root, text='+', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('+')).place(x=430, y=300)

Button(root, text='3', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('3')).place(x=10, y=400)
Button(root, text='2', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('2')).place(x=150, y=400)
Button(root, text='1', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('1')).place(x=290, y=400)
Button(root, text='0', width=11, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('0')).place(x=10, y=500)

Button(root, text='.', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='black', bg='white',command=lambda: show('.')).place(x=290, y=500)
Button(root, text='=', width=5, height=3, font=('arial', 30, 'bold'), bd=1, fg='black', bg='blue',command=lambda: calculate()).place(x=430, y=400)

root.mainloop()
