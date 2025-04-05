from tkinter import *
window=Tk()
window.title("Demo Window")
window.geometry("400x300")
label = Label(window, text='Enter birthyear',fg="white", bg="purple")
entry1 = Entry(window)
def difference():
  birthyear = int(entry1.get())
  difference = 2025 - birthyear 
  label3.config(text = difference)
btn = Button(window, text='Calculate',command=difference)
label3 = Label(window, text='Result')
label.pack()
entry1.pack()
btn.pack()
window.mainloop()