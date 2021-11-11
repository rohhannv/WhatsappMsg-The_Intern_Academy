# importing_the_required_libraries
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
import pyautogui
import pywhatkit as wp
import time

# creating the GUI window
window = Tk()
window.title("WP Auto Wisher")
window.geometry("700x500+300+320")
no = StringVar()
txt = StringVar()


def wp_send(num, text):
    # function for sending whatsapp message
    num = str(num)
    text = str(text)
    wp.sendwhatmsg(num, text, 18, 12, 5)
    pyautogui.click(1050, 950)
    time.sleep(2)
    pyautogui.click(1866, 974)


def save():
    # functionality of 'submit' button
    no = wp_number.get()
    txt = wp_message.get()
    wp_send(no, txt)


# Heading part
header_font = Font(family="Helvetica", size=20 )
Label(window, text="The Intern Academy Task", font=header_font).pack()
header_font = Font(family="Helvetica", size=24, weight="bold")
Label(window, text="Whatsapp Auto Wisher", font=header_font).pack()
space = Font(family="Helvetica", size=12)
Label(window, text=" ", font=space).pack()



number = Label(window, text="Enter Number(with country code)")
number.pack()
wp_number = Entry(window, textvariable=no, width=20)
wp_number.pack()

Label(window, text=" ", font=space).pack()
message = Label(window, text="Enter message")
message.pack()
wp_message = Entry(window, textvariable=txt, width=70)
wp_message.pack()
Label(window, text=" ", font=space).pack()

# buttons
submit = Button(window, text="Wish", command=save, padx=20, pady=10, bg='black', fg='yellow', activebackground='green', activeforeground='white').place(x=250, y=280)
Label(window, text=" ", font=space).pack()
exitButton = Button(window, text="Exit", command=window.destroy, padx=20, pady=10, bg="black", fg='yellow').place(x=350, y=280)

# custom icon
window.mainloop()
