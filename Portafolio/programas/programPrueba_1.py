from tkinter import *

class HelloNameFrame(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, the_window)

        self.users_name = StringVar()
        self.display_string = StringVar()


        self.friendly_label = Label(self, text="Enter your name")
        self.name_entry = Entry(self, textvariable=self.users_name)
        self.button = Button(self, text="Click me", command=self.display_output)
        self.display_label = Label(self, textvariable=self.display_string, relief="solid")


        self.friendly_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.button.grid(row=1, column=0)
        self.display_label.grid(row=1, column=1)


    def display_output(self):
        self.display_string.set("Hello" + self.users_name.get())


my_window = Tk()
frameA= HelloNameFrame(my_window)

frameA.users_name.set("2")
frameA.button["text"] = "Hola"

frameA.grid(row=0, column=0)
my_window.mainloop()