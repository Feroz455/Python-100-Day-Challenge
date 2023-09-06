import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)


# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
def click():
    my_label["text"] = input.get()
    return f"i got click"
button =tkinter.Button(text="click me", command=click)
button.pack()
input = tkinter.Entry()
input.pack()

window.mainloop()
 