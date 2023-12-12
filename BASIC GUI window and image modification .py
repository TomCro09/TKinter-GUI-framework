from tkinter import *

window = Tk()
window.title("GUI_window")
photo = PhotoImage(file='memeface-removebg-preview.png')

label = Label(window,
              text="bro, do you even code?",
              font=('Arial',40,'bold'),
              fg='#00ff00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label.pack()



window.mainloop()

