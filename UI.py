import tkinter as tk
from pricing import calculatePrice5

root = tk.Tk()
root.geometry("1500x800")

breakDown = tk.Text(root, height=16, width=32, font=('Arial', 24))
breakDown.grid(row=0, column=1)

milkTeaBase = 2.25
normalBase = 2.0

def takeDrinkType(drinkType):
    
    price = milkTeaBase if drinkType == 'Milk Tea' else normalBase

    breakDown.delete(1.0, "end")
    breakDown.insert(1.0, "Drink Type: " + drinkType + "    : " + str(price) )
    return drinkType, price

# Button for Drink Type
btHot = tk.Button(root, text="Hot", command=lambda: takeDrinkType('Hot'), width=10, font=('Ariel', 14) )
btHot.grid(row=0, column=7)

btCold = tk.Button(root, text="Cold", command=lambda: takeDrinkType('Cold'), width=10, font=('Ariel', 14) )
btCold.grid(row=0, column=8)

btBlend = tk.Button(root, text="Blend", command=lambda: takeDrinkType('Blend'), width=10, font=('Ariel', 14) )
btBlend.grid(row=0, column=9)

btMilkTea = tk.Button(root, text="Milk Tea", command=lambda: takeDrinkType('Milk Tea'), width=10, font=('Ariel', 14) )
btMilkTea.grid(row=0, column=10)

# Button for Size

def takeSize(size):
    if size == 'M':
        price = 0.5
    if size == 'L':
        price = 1.0
    if size == 'XL':
        price = 1.5

    breakDown.delete(2.0, "end")
    breakDown.insert(2.0, "Drink Size: " + size + "    : " + str(price) )
    return size, price


btS = tk.Button(root, text="S", command=lambda: takeDrinkType('S'), width=10, font=('Ariel', 14) )
btS.grid(row=1, column=7)

btCold = tk.Button(root, text="M", command=lambda: takeDrinkType('M'), width=10, font=('Ariel', 14) )
btCold.grid(row=1, column=8)

btBlend = tk.Button(root, text="L", command=lambda: takeDrinkType('L'), width=10, font=('Ariel', 14) )
btBlend.grid(row=1, column=9)

btMilkTea = tk.Button(root, text="XL", command=lambda: takeDrinkType('XL'), width=10, font=('Ariel', 14) )
btMilkTea.grid(row=1, column=10)

root.mainloop()