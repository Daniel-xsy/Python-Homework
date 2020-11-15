import tkinter as tk
import login

window=tk.Tk()
#添加标题
window.title('Student Achievement Enquiry System')
window.geometry('550x400')
canvas=tk.Canvas(window,height=95,width=98)
image_file=tk.PhotoImage(file='hust.gif')
image=canvas.create_image(50,10,anchor='n',image=image_file)
canvas.place(x=170,y=40)

login.LoginPage(window)
window.mainloop()