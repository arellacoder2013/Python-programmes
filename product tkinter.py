from tkinter import *
window=Tk()
window.title("Demo Window")
window.geometry("400x300")

lbl = Label(text="Hey There!, Welcome to calculator app" , fg="white", bg="#072F5F" , height=1, width=30)
lbl1 = Label(window, text='Enter the first number you want to multiply:', fg="white", bg="purple")
entry1 = Entry(window)
lbl2 = Label(window, text='Enter the second number you want to multiply:', fg="white", bg="lightblue")
entry2 = Entry(window)

def product():
  num1 = int(entry1.get())
  num2 = int(entry2.get())
  product1 = num1 * num2
  lbl3.config(text = product1)

btn = Button(window, text='Calculate',command=product, bg="lightpink")
lbl3 = Label(window, text='Result')
lbl.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
btn.pack()
lbl3.pack()
window.mainloop()