from tkinter import *


def button_click():
    answer = round((int(user_input.get()) * 1.609))
    result.config(text=answer)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=50)

user_input = Entry()
user_input.config(width=10)
user_input.focus()
user_input.grid(row=0, column=1)

equal_to = Label(text="is Equal to")
equal_to.grid(row=1, column=0)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

km = Label(text="KM")
km.grid(row=1, column=2)

result = Label(text="0")
result.grid(row=1, column=1)

button = Button(text="Calculate", command=button_click)
button.grid(row=2, column=1)

window.mainloop()
