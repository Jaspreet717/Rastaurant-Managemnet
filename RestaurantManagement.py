#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
#import random    
import time

root = Tk()
root.geometry("1400x1000+150+300")
root.resizable(width=True, height=True)
root.title("Restaurant Management System")

# Top
Tops = Frame(root, width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

# Time
localtime = time.asctime(time.localtime(time.time()))

# Info
lblinfo = Label(Tops, font=('algerian', 30, 'bold'), text="Restaurant Management System", fg="crimson", bg=None, bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('algerian', 25), text=localtime, fg="purple", bg=None, anchor=W)
lblinfo.grid(row=1, column=0)

# Items
lbit = Label(root, font=('algerian', 30, 'bold'), text="Menu", fg="dark orange", bd=10)
lbit.place(x=100, y=140)
lbit = Label(root, font=('arial black', 18), text="Burger", fg="sky blue", bd=1)
lbit.place(x=20, y=200)
lbit = Label(root, font=('arial black', 18), text="Tea", fg="sky blue", bd=1)
lbit.place(x=20, y=250)
lbit = Label(root, font=('arial black', 18), text="Coffie", fg="sky blue", bd=1)
lbit.place(x=20, y=300)
lbit = Label(root, font=('arial black', 18), text="Pizza", fg="sky blue", bd=1)
lbit.place(x=20, y=350)
lbit = Label(root, font=('arial black', 18), text="Cold Drink", fg="sky blue", bd=1)
lbit.place(x=20, y=400)
lbit = Label(root, font=('arial black', 18), text="Cakes", fg="sky blue", bd=1)
lbit.place(x=20, y=450)
lbit = Label(root, font=('arial black', 18), text="Maggie", fg="sky blue", bd=1)
lbit.place(x=20, y=500)

# Price
lbit = Label(root,font=( 'arial black' ,18,  ),text="₹ 49",fg="sky blue",bd=1)
lbit.place(x=220,y=200)
lbit = Label(root,font=( 'arial black' ,18,  ),text="₹ 34",fg="sky blue",bd=1)
lbit.place(x=220,y=250)
lbit = Label(root,font=( 'arial black' ,18,  ),text="₹ 32",fg="sky blue",bd=1)
lbit.place(x=220,y=300)
lbit = Label(root,font=( 'arial black' ,18,  ),text="₹ 79",fg="sky blue",bd=1)
lbit.place(x=220,y=350)
lbit = Label(root,font=( 'arial black' ,18,  ),text="₹ 47",fg="sky blue",bd=1)
lbit.place(x=220,y=400)
lbit = Label(root,font=( 'arial black' ,18,  ),text="₹ 222",fg="sky blue",bd=1)
lbit.place(x=220,y=450)
lbit = Label(root,font=( 'arial black' ,18,  ),text="₹ 37",fg="sky blue",bd=1)
lbit.place(x=220,y=500)

# Order
lbit = Label(root, font=('algerian', 30, 'bold'), text="Order", fg="crimson", bd=1)
lbit.place(x=650, y=140)

order = []

def order_add(item):
    order.append(item)
    order_text.delete("1.0", END)  # Clear the text box
    order_text.insert(END, '\n'.join(order))  # Display the updated order

#cancel order


#generate bill
def generate_bill():
    total_amount = 0

    # Calculate total amount
    for item in order:
        if item == "Burger":
            total_amount += 49
        elif item == "Tea":
            total_amount += 34
        elif item == "Coffie":
            total_amount += 32
        elif item == "Pizza":
            total_amount += 79
        elif item == "Cold Drink":
            total_amount += 47
        elif item == "Cakes":
            total_amount += 222
        elif item == "Maggie":
            total_amount += 37

    # Calculate taxes
    cgst = (total_amount * 6) / 100
    sgst = (total_amount * 6) / 100
    vat = (total_amount * 12) / 100

    # Calculate total bill amount including taxes
    total_bill = total_amount + cgst + sgst + vat

    # Create a new window for the bill
    bill_window = Toplevel(root)
    bill_window.title("Bill")
    bill_window.geometry("900x900")
    bill_window.config(bg='white')

    # Display the bill
    bill_label = Label(bill_window, font=("Times New Roman", 20, 'bold'), text="Item\t\tPrice")
    bill_label.pack()

    for item in order:
        price = 0
        if item == "Burger":
            price = 49
        elif item == "Tea":
            price = 34
        elif item == "Coffie":
            price = 32
        elif item == "Pizza":
            price = 79
        elif item == "Cold Drink":
            price = 47
        elif item == "Cakes":
            price = 222
        elif item == "Maggie":
            price = 37

        item_label = Label(bill_window, font=("Times New Roman", 20), text=f"{item}\t\t{price}")
        item_label.pack()

    # Display the total amount
    total_label = Label(bill_window, font=("Times New Roman", 20, 'bold'), text=f"Total Amount: ₹{total_amount}")
    total_label.pack()

    # Display taxes
    cgst_label = Label(bill_window, font=("Times New Roman", 20), text=f"CGST (6%): ₹{cgst}")
    cgst_label.pack()

    sgst_label = Label(bill_window, font=("Times New Roman", 20), text=f"SGST (6%): ₹{sgst}")
    sgst_label.pack()

    vat_label = Label(bill_window, font=("Times New Roman", 20), text=f"VAT (12%): ₹{vat}")
    vat_label.pack()

    # Display total bill amount
    total_bill_label = Label(bill_window, font=("Times New Roman", 20, 'bold'), text=f"Total Bill: ₹{total_bill}")
    total_bill_label.pack()

    # Clear the order list and the order text box
    order.clear()
    order_text.delete("1.0", END)
def order_cancel():
    order.clear()
    
# Text box
order_text = Text(root, height=10, width=20, fg="purple", font=('arial black', 20))
order_text.place(x=550, y=200)

# Add buttons
btn1 = Button(root, text="+", fg="red", font=('arial black', 10), command=lambda: order_add("Burger"))
btn1.place(x=360, y=200)

btn2 = Button(root, text="+", fg="red", font=('arial black', 10), command=lambda: order_add("Tea"))
btn2.place(x=360, y=250)

btn3 = Button(root, text="+", fg="red", font=('arial black', 10), command=lambda: order_add("Coffie"))
btn3.place(x=360, y=300)

btn4 = Button(root, text="+", fg="red", font=('arial black', 10), command=lambda: order_add("Pizza"))
btn4.place(x=360, y=350)

btn5 = Button(root, text="+", fg="red", font=('arial black', 10), command=lambda: order_add("Cold Drink"))
btn5.place(x=360, y=400)

btn6 = Button(root, text="+", fg="red", font=('arial black', 10), command=lambda: order_add("Cakes"))
btn6.place(x=360, y=450)

btn7 = Button(root, text="+", fg="red", font=('arial black', 10), command=lambda: order_add("Maggie"))
btn7.place(x=360, y=500)


btncncl=Button(root,text='Cancel',font=('algerian', 20, 'bold'), fg="blue", bd=1,command=lambda:order_cancel())
btncncl.place(x=650,y=600)
btnbill=  Button(root,text='Bill',font=('algerian', 20, 'bold'), fg="blue", bd=1,command=lambda:generate_bill())
btnbill.place(x=1200,y=140)
root.mainloop()


# In[ ]:




