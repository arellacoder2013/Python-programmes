from tkinter import *
window=Tk()
window.title("Demo Window")
window.geometry("400x300")
length= Label(window, text='Enter length in inches',fg="white", bg="purple")
entry1 = Entry(window)
def cal_length():
  length = float(entry1.get())
  multiply = 2.54*length
  label3.config(text = multiply)
btn = Button(window, text='Calculate',command=cal_length)
label3 = Label(window, text='Result in cm')
length.pack()
entry1.pack()
btn.pack()
label3.pack()
window.mainloop()