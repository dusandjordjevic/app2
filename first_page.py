from tkinter import *
import tkinter.messagebox as mb

class First_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Video klub")

        self.label1 = Label(root, text="Dobrodosli u nas video klub")
        self.label1.config(font=("Arial", 15))
        self.label1.grid(row=0, column=0)

        self.label2 = Label(root, text="Molim vas da se prijavite")
        self.label2.config(font=("Arial", 15))
        self.label2.grid(row=1, column=0)

        self.label3 = Label(root, text="Korisnicko ime:")
        self.label3.config(font=("Arial", 15))
        self.label3.grid(row=3, column=0)
        
        self.entry1 = Entry(root, bd = '3')
        self.entry1.grid(row=4, column=0)
        
        self.label4 = Label(root, text="Sifra:")
        self.label4.config(font=("Arial", 15))
        self.label4.grid(row=5, column=0)
        
        self.entry2 = Entry(root, bd = '3', show="*")
        self.entry2.grid(row=6, column=0)

        self.btn1 = Button(root, text = "Uloguj se", command = self.get_login)
        self.btn1.grid(row=7, column=0)
        
    def get_login(self):
        self.username = self.entry1.get()
        self.entry1.delete(0, 'end')

        self.password = self.entry2.get()
        self.entry2.delete(0, 'end')
    def get_value(self):
        return self.username, self.password
    
root = Tk()
first_page = First_page(root)
root.mainloop()