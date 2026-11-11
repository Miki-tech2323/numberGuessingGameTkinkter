import tkinter as tk
import random

class myGui:
    def __init__(self):
        self.numRandom = random.randint(0, 100)
        print(self.numRandom)
        self.window = tk.Tk()
        self.window.geometry("500x300")
        self.label = tk.Label(text="Number guesing game!!!")
        self.entry = tk.Entry(self.window, width=5, font=("Arial", 12))
        self.labelEnter = tk.Label(text="Enter a number:")
        self.enterBtn = tk.Button(self.window, text="Click me!!")


        self.enterBtn.place(x= 200,y=70)
        self.labelEnter.place(x = 120,y = 40)
        self.entry.place(x=210, y= 40)
        self.label.place(x=170, y=10)
        self.window.mainloop()
    def clickMe(self):
        num = self.entry.get()
        
        while True:
            if num == self.numRandom:
                self.messagebox.showinfo("Win", "You won")
                break




myGui()
myGui.clickMe()
