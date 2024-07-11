from tkinter import *
from tkinter import messagebox,ttk
import random
import os
import tempfile

user_credentials = {
    'admin': 'admin123',
    'user1': 'password1',
    'user2': 'password2'
}
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo('Login Successful', f'Welcome, {username}!')
        root.deiconify()  
        login_window.withdraw()  
    else:
        messagebox.showerror('Login Failed', 'Invalid username or password')

def open_login_window():
    global login_window
    login_window = Toplevel(root)
    login_window.title('Login')
    login_window.geometry('300x150')
    login_window.config(background='black')
    login_window.attributes('-topmost', True)  

    Label(login_window, text='Username:',font=('arial', 14),bg='black',fg='gold').pack()
    global username_entry
    username_entry = Entry(login_window)
    username_entry.pack()

    Label(login_window, text='Password:',font=('arial', 14),bg='black',fg='gold').pack()
    global password_entry
    password_entry = Entry(login_window, show='*')
    password_entry.pack()

    Button(login_window, text='Login',bg='white',fg='black',relief=GROOVE, command=login).pack(pady=10)

    login_window.update_idletasks()
    width = login_window.winfo_width()
    height = login_window.winfo_height()
    x = (login_window.winfo_screenwidth() // 2) - (width // 2)
    y = (login_window.winfo_screenheight() // 2) - (height // 2)
    login_window.geometry(f'+{x}+{y}')

    root.withdraw()

root = Tk()
root.title('Billing Software')
root.geometry('1350x700+0+0')
root.config(bg='black')

product_list = {
    'Soap': {'price': 40, 'stock': 10},
    'Face Cream': {'price': 120, 'stock': 5},
    'Hair Spray': {'price': 180, 'stock': 15},
    'Face Wash': {'price': 60, 'stock': 10},
    'Hair Gel': {'price': 140, 'stock': 5},
    'Body Lotion': {'price': 180, 'stock': 8},
    'Daal': {'price': 100, 'stock': 20},
    'Wheat': {'price': 50, 'stock': 50},
    'Rice': {'price': 60, 'stock': 30},
    'Oil': {'price': 120, 'stock': 20},
    'Tea': {'price': 150, 'stock': 15},
    'Sugar': {'price': 40, 'stock': 25},
    'Maaza': {'price': 40, 'stock': 10},
    'Pepsi': {'price': 40, 'stock': 8},
    'Sprite': {'price': 50, 'stock': 10},
    'Dew': {'price': 45, 'stock': 5},
    'Frooti': {'price': 30, 'stock': 12},
    'Coca Cola': {'price': 50, 'stock': 7}
}

def add_product():
    add_window = Toplevel(root)
    add_window.title('Add Product')
    add_window.geometry('400x300')

    name_label = Label(add_window, text='Product Name', font=('arial', 14)).pack(pady=10)
    name_entry = Entry(add_window, bd=5, relief=GROOVE)
    name_entry.pack(pady=5)

    price_label = Label(add_window, text='Product Price', font=('arial', 14)).pack(pady=10)
    price_entry = Entry(add_window, bd=5, relief=GROOVE)
    price_entry.pack(pady=5)

    stock_label = Label(add_window, text='Stock Quantity', font=('arial', 14)).pack(pady=10)
    stock_entry = Entry(add_window, bd=5, relief=GROOVE)
    stock_entry.pack(pady=5)

    def save_product():
        try:
            name = name_entry.get()
            price = int(price_entry.get())
            stock = int(stock_entry.get())
            product_list[name] = {'price': price, 'stock': stock}
            messagebox.showinfo('Success', 'Product added successfully!')
            add_window.destroy()
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid details')

    save_btn = Button(add_window, text='Save Product', command=save_product)
    save_btn.pack(pady=20)

def edit_product():
    edit_window = Toplevel(root)
    edit_window.title('Edit Product')
    edit_window.geometry('400x300')

    name_label = Label(edit_window, text='Product Name', font=('arial', 14)).pack(pady=10)
    name_entry = Entry(edit_window, bd=5, relief=GROOVE)
    name_entry.pack(pady=5)

    price_label = Label(edit_window, text='New Price', font=('arial', 14)).pack(pady=10)
    price_entry = Entry(edit_window, bd=5, relief=GROOVE)
    price_entry.pack(pady=5)

    stock_label = Label(edit_window, text='New Stock Quantity', font=('arial', 14)).pack(pady=10)
    stock_entry = Entry(edit_window, bd=5, relief=GROOVE)
    stock_entry.pack(pady=5)

    def update_product():
        try:
            name = name_entry.get()
            price = int(price_entry.get())
            stock = int(stock_entry.get())
            if name in product_list:
                product_list[name]['price'] = price
                product_list[name]['stock'] = stock
                messagebox.showinfo('Success', 'Product updated successfully!')
                edit_window.destroy()
            else:
                messagebox.showerror('Error', 'Product not found')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid details')

    update_btn = Button(edit_window, text='Update Product', command=update_product)
    update_btn.pack(pady=20)

def delete_product():
    delete_window = Toplevel(root)
    delete_window.title('Delete Product')
    delete_window.geometry('400x200')

    name_label = Label(delete_window, text='Product Name', font=('arial', 14)).pack(pady=10)
    name_entry = Entry(delete_window, bd=5, relief=GROOVE)
    name_entry.pack(pady=5)

    def remove_product():
        name = name_entry.get()
        if name in product_list:
            del product_list[name]
            messagebox.showinfo('Success', 'Product deleted successfully!')
            delete_window.destroy()
        else:
            messagebox.showerror('Error', 'Product not found')

    delete_btn = Button(delete_window, text='Delete Product', command=remove_product)
    delete_btn.pack(pady=20)

def low_stock_report():
    report_window = Toplevel(root)
    report_window.title('Low Stock Report')
    report_window.geometry('400x400')

    report_text = Text(report_window, bd=5, relief=GROOVE, font=('arial', 14))
    report_text.pack(fill=BOTH, expand=1)

    report_text.insert(END, 'Low Stock Products\n')
    report_text.insert(END, '=================\n\n')
    for product, details in product_list.items():
        if details['stock'] < 10:
            report_text.insert(END, f'{product} - {details["stock"]} left\n')


def clear():
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)
    facewashEntry.delete(0, END)

    daalEntry.delete(0, END)
    wheatEntry.delete(0, END)
    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    teaEntry.delete(0, END)
    sugarEntry.delete(0, END)

    pepsiEntry.delete(0, END)
    maazaEntry.delete(0, END)
    dewEntry.delete(0, END)
    cocacolaEntry.delete(0, END)
    frootiEntry.delete(0, END)
    spriteEntry.delete(0, END)

    bathsoapEntry.insert(0, 0)
    facecreamEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)
    facewashEntry.insert(0, 0)

    daalEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    teaEntry.insert(0, 0)
    sugarEntry.insert(0, 0)

    pepsiEntry.insert(0, 0)
    maazaEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    cocacolaEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    spriteEntry.insert(0, 0)

    cosmetictaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    colddrinktaxEntry.delete(0, END)

    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    colddrinkpriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    textarea.delete(1.0, END)

def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
        #else:
            #messagebox.showerror('Error', 'Invalid Bill Number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'Bill Number {billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)

billnumber = random.randint(500, 1000)

def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif cosmeticpriceEntry.get() == '' or grocerypriceEntry.get() == '' or colddrinkpriceEntry.get() == '':
        messagebox.showerror('Error', 'No products are selected')
    elif cosmeticpriceEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and colddrinkpriceEntry.get() == '0 Rs':
        messagebox.showerror('Error', 'No products are selected')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '\t**Welcome Customer**\n')
        textarea.insert(END, f'\nBillNumber: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END, '\n======================================')
        textarea.insert(END, 'Product\t\tQuantity\t\tPrice')
        textarea.insert(END, '\n======================================')
        total_amount = 0.0

        # Check each product and add it to the bill if quantity is greater than zero
        if int(bathsoapEntry.get()) > 0:
            textarea.insert(END, f'\nBath Soap\t\t{bathsoapEntry.get()}\t\t{int(bathsoapEntry.get()) * soapprice} Rs')
            total_amount += int(bathsoapEntry.get()) * soapprice
        if int(hairsprayEntry.get()) > 0:
            textarea.insert(END, f'\nHair Spray\t\t{hairsprayEntry.get()}\t\t{int(hairsprayEntry.get()) * hairsprayprice} Rs')
            total_amount += int(hairsprayEntry.get()) * hairsprayprice
        if int(facewashEntry.get()) > 0:
            textarea.insert(END, f'\nFace Wash\t\t{facewashEntry.get()}\t\t{int(facewashEntry.get()) * facewashprice} Rs')
            total_amount += int(facewashEntry.get()) * facewashprice
        if int(facecreamEntry.get()) > 0:
            textarea.insert(END, f'\nFace Cream\t\t{facecreamEntry.get()}\t\t{int(facecreamEntry.get()) * facecreamprice} Rs')
            total_amount += int(facecreamEntry.get()) * facecreamprice
        if int(hairgelEntry.get()) > 0:
            textarea.insert(END, f'\nHair Gel\t\t{hairgelEntry.get()}\t\t{int(hairgelEntry.get()) * hairgelprice} Rs')
            total_amount += int(hairgelEntry.get()) * hairgelprice
        if int(bodylotionEntry.get()) > 0:
            textarea.insert(END, f'\nBody Lotion\t\t{bodylotionEntry.get()}\t\t{int(bodylotionEntry.get()) * bodylotionprice} Rs')
            total_amount += int(bodylotionEntry.get()) * bodylotionprice

        if int(riceEntry.get()) > 0:
            textarea.insert(END, f'\nRice\t\t{riceEntry.get()}\t\t{int(riceEntry.get()) * riceprice} Rs')
            total_amount += int(riceEntry.get()) * riceprice
        if int(daalEntry.get()) > 0:
            textarea.insert(END, f'\nDaal\t\t{daalEntry.get()}\t\t{int(daalEntry.get()) * daalprice} Rs')
            total_amount += int(daalEntry.get()) * daalprice
        if int(oilEntry.get()) > 0:
            textarea.insert(END, f'\nOil\t\t{oilEntry.get()}\t\t{int(oilEntry.get()) * oilprice} Rs')
            total_amount += int(oilEntry.get()) * oilprice
        if int(sugarEntry.get()) > 0:
            textarea.insert(END, f'\nSugar\t\t{sugarEntry.get()}\t\t{int(sugarEntry.get()) * sugarprice} Rs')
            total_amount += int(sugarEntry.get()) * sugarprice
        if int(teaEntry.get()) > 0:
            textarea.insert(END, f'\nTea\t\t{teaEntry.get()}\t\t{int(teaEntry.get()) * teaprice} Rs')
            total_amount += int(teaEntry.get()) * teaprice
        if int(wheatEntry.get()) > 0:
            textarea.insert(END, f'\nWheat\t\t{wheatEntry.get()}\t\t{int(wheatEntry.get()) * wheatprice} Rs')
            total_amount += int(wheatEntry.get()) * wheatprice

        if int(maazaEntry.get()) > 0:
            textarea.insert(END, f'\nMaaza\t\t{maazaEntry.get()}\t\t{int(maazaEntry.get()) * maazaprice} Rs')
            total_amount += int(maazaEntry.get()) * maazaprice
        if int(frootiEntry.get()) > 0:
            textarea.insert(END, f'\nFrooti\t\t{frootiEntry.get()}\t\t{int(frootiEntry.get()) * frootiprice} Rs')
            total_amount += int(frootiEntry.get()) * frootiprice
        if int(dewEntry.get()) > 0:
            textarea.insert(END, f'\nDew\t\t{dewEntry.get()}\t\t{int(dewEntry.get()) * dewprice} Rs')
            total_amount += int(dewEntry.get()) * dewprice
        if int(pepsiEntry.get()) > 0:
            textarea.insert(END, f'\nPepsi\t\t{pepsiEntry.get()}\t\t{int(pepsiEntry.get()) * pepsiprice} Rs')
            total_amount += int(pepsiEntry.get()) * pepsiprice
        if int(spriteEntry.get()) > 0:
            textarea.insert(END, f'\nSprite\t\t{spriteEntry.get()}\t\t{int(spriteEntry.get()) * spriteprice} Rs')
            total_amount += int(spriteEntry.get()) * spriteprice
        if int(cocacolaEntry.get()) > 0:
            textarea.insert(END, f'\nCoca Cola\t\t{cocacolaEntry.get()}\t\t{int(cocacolaEntry.get()) * cocacolaprice} Rs')
            total_amount += int(cocacolaEntry.get()) * cocacolaprice

        textarea.insert(END, '\n--------------------------------------')

        if cosmetictaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nCosmetic Tax\t\t\t\t {cosmetictaxEntry.get()}')
            total_amount += float(cosmetictaxEntry.get().split()[0])
        if grocerytaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nGrocery Tax\t\t\t\t {grocerytaxEntry.get()}')
            total_amount += float(grocerytaxEntry.get().split()[0])
        if colddrinktaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nCold Drink Tax\t\t\t\t {colddrinktaxEntry.get()}')
            total_amount += float(colddrinktaxEntry.get().split()[0])

        textarea.insert(END, '\n--------------------------------------')
        textarea.insert(END, f'\nTotal Amount:\t\t\t\t {total_amount} Rs')
        textarea.insert(END, '\n--------------------------------------')
        textarea.insert(END, '\n\t**Thanks For Shopping**')
        textarea.insert(END, '\t**Visit Again**')

        save_bill()

def total():
    if (
        bathsoapEntry.get() == '0' and facecreamEntry.get() == '0' and hairsprayEntry.get() == '0'
        and facewashEntry.get() == '0' and hairgelEntry.get() == '0' and bodylotionEntry.get() == '0'
        and daalEntry.get() == '0' and wheatEntry.get() == '0' and riceEntry.get() == '0'
        and oilEntry.get() == '0' and teaEntry.get() == '0' and sugarEntry.get() == '0'
        and maazaEntry.get() == '0' and pepsiEntry.get() == '0' and spriteEntry.get() == '0'
        and dewEntry.get() == '0' and frootiEntry.get() == '0' and cocacolaEntry.get() == '0'
    ):
        messagebox.showerror('Error', 'No product is selected')
    else:
        global soapprice, facecreamprice, hairsprayprice, facewashprice, hairgelprice, bodylotionprice
        global daalprice, wheatprice, riceprice, oilprice, teaprice, sugarprice
        global maazaprice, pepsiprice, spriteprice, dewprice, frootiprice, cocacolaprice
        global cosmeticprice, groceryprice, colddrinkprice
        global totalcosmetictax, totalgrocerytax, totalcolddrinktax

        soapprice = int(bathsoapEntry.get()) * 40
        facecreamprice = int(facecreamEntry.get()) * 120
        hairsprayprice = int(hairsprayEntry.get()) * 180
        facewashprice = int(facewashEntry.get()) * 60
        hairgelprice = int(hairgelEntry.get()) * 140
        bodylotionprice = int(bodylotionEntry.get()) * 180

        cosmeticprice = (
            soapprice + facecreamprice + hairsprayprice + facewashprice + hairgelprice + bodylotionprice
        )

        daalprice = int(daalEntry.get()) * 180
        wheatprice = int(wheatEntry.get()) * 240
        riceprice = int(riceEntry.get()) * 60
        oilprice = int(oilEntry.get()) * 180
        teaprice = int(teaEntry.get()) * 40
        sugarprice = int(sugarEntry.get()) * 45

        groceryprice = (
            daalprice + wheatprice + riceprice + oilprice + teaprice + sugarprice
        )

        maazaprice = int(maazaEntry.get()) * 60
        pepsiprice = int(pepsiEntry.get()) * 60
        spriteprice = int(spriteEntry.get()) * 60
        dewprice = int(dewEntry.get()) * 60
        frootiprice = int(frootiEntry.get()) * 50
        cocacolaprice = int(cocacolaEntry.get()) * 60

        colddrinkprice = (
            maazaprice + pepsiprice + spriteprice + dewprice + frootiprice + cocacolaprice
        )

        totalcosmetictax = round((cosmeticprice * 0.05), 2)
        totalgrocerytax = round((groceryprice * 0.1), 2)
        totalcolddrinktax = round((colddrinkprice * 0.05), 2)

        totalamount = (
            cosmeticprice + groceryprice + colddrinkprice
            + totalcosmetictax + totalgrocerytax + totalcolddrinktax
        )

        cosmeticpriceEntry.delete(0, END)
        grocerypriceEntry.delete(0, END)
        colddrinkpriceEntry.delete(0, END)

        cosmeticpriceEntry.insert(0, str(cosmeticprice) + ' Rs')
        grocerypriceEntry.insert(0, str(groceryprice) + ' Rs')
        colddrinkpriceEntry.insert(0, str(colddrinkprice) + ' Rs')

        cosmetictaxEntry.delete(0, END)
        grocerytaxEntry.delete(0, END)
        colddrinktaxEntry.delete(0, END)

        cosmetictaxEntry.insert(0, str(totalcosmetictax) + ' Rs')
        grocerytaxEntry.insert(0, str(totalgrocerytax) + ' Rs')
        colddrinktaxEntry.insert(0, str(totalcolddrinktax) + ' Rs')

        totalbillEntry.delete(0, END)
        totalbillEntry.insert(0, str(totalamount) + ' Rs')

# Heading
heading = Label(
    root, text='Inventory Management System', bg='black', fg='gold',
    font=('times new roman', 30, 'bold'), relief=GROOVE, bd=10
).pack(fill=X)

# Customer Frame
F1 = LabelFrame(
    root, text='Customer Details', font=('times new roman', 15, 'bold'),
    fg='gold', bg='black', relief=GROOVE, bd=10
)
F1.place(x=0, y=80, relwidth=1)

nameLabel = Label(
    F1, text='Customer Name', font=('times new roman', 18, 'bold'),
    bg='black', fg='white'
).grid(row=0, column=0, padx=20, pady=5)
nameEntry = Entry(
    F1, bd=8, relief=GROOVE, textvariable=StringVar(),
    font=('arial', 10)
)
nameEntry.grid(row=0, column=1, ipadx=30, pady=5)

phoneLabel = Label(
    F1, text='Phone Number', font=('times new roman', 18, 'bold'),
    bg='black', fg='white'
).grid(row=0, column=2, padx=20)
phoneEntry = Entry(
    F1, bd=8, relief=GROOVE, textvariable=StringVar(),
    font=('arial', 10)
)
phoneEntry.grid(row=0, column=3, ipadx=30, pady=5)

billnumberLabel = Label(
    F1, text='Bill Number', font=('times new roman', 18, 'bold'),
    bg='black', fg='white'
).grid(row=0, column=4, padx=20)
billnumberEntry = Entry(
    F1, bd=8, relief=GROOVE, textvariable=StringVar(),
    font=('arial', 10)
)
billnumberEntry.grid(row=0, column=5, ipadx=30, pady=5)

billBtn = Button(
    F1, text='Search', bd=7, relief=GROOVE, font='arial 12 bold',
    bg='gray', fg='black', command=search_bill
)
billBtn.grid(row=0, column=6, padx=20, pady=10)

# Cosmetics Frame
F2 = LabelFrame(
    root, text='Cosmetics', font=('times new roman', 15, 'bold'),
    fg='gold', bg='black', relief=GROOVE, bd=10
)
F2.place(x=5, y=180, width=325, height=380)

bathsoapLabel = Label(
    F2, text='Bath Soap', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=0, column=0, padx=10, pady=10)
bathsoapEntry = Entry(
    F2, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
bathsoapEntry.grid(row=0, column=1, ipady=5, ipadx=5)
bathsoapEntry.insert(0, 0)

facecreamLabel = Label(
    F2, text='Face Cream', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=1, column=0, padx=10, pady=10)
facecreamEntry = Entry(
    F2, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
facecreamEntry.grid(row=1, column=1, ipady=5, ipadx=5)
facecreamEntry.insert(0, 0)

hairsprayLabel = Label(
    F2, text='Hair Spray', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=2, column=0, padx=10, pady=10)
hairsprayEntry = Entry(
    F2, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
hairsprayEntry.grid(row=2, column=1, ipady=5, ipadx=5)
hairsprayEntry.insert(0, 0)

facewashLabel = Label(
    F2, text='Face Wash', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=3, column=0, padx=10, pady=10)
facewashEntry = Entry(
    F2, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
facewashEntry.grid(row=3, column=1, ipady=5, ipadx=5)
facewashEntry.insert(0, 0)

hairgelLabel = Label(
    F2, text='Hair Gel', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=4, column=0, padx=10, pady=10)
hairgelEntry = Entry(
    F2, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
hairgelEntry.grid(row=4, column=1, ipady=5, ipadx=5)
hairgelEntry.insert(0, 0)

bodylotionLabel = Label(
    F2, text='Body Lotion', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=5, column=0, padx=10, pady=10)
bodylotionEntry = Entry(
    F2, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
bodylotionEntry.grid(row=5, column=1, ipady=5, ipadx=5)
bodylotionEntry.insert(0, 0)

# Grocery Frame
F3 = LabelFrame(
    root, text='Grocery', font=('times new roman', 15, 'bold'),
    fg='gold', bg='black', relief=GROOVE, bd=10
)
F3.place(x=340, y=180, width=325, height=380)

daalLabel = Label(
    F3, text='Daal', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=0, column=0, padx=10, pady=10)
daalEntry = Entry(
    F3, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
daalEntry.grid(row=0, column=1, ipady=5, ipadx=5)
daalEntry.insert(0, 0)

wheatLabel = Label(
    F3, text='Wheat', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=1, column=0, padx=10, pady=10)
wheatEntry = Entry(
    F3, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
wheatEntry.grid(row=1, column=1, ipady=5, ipadx=5)
wheatEntry.insert(0, 0)

riceLabel = Label(
    F3, text='Rice', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=2, column=0, padx=10, pady=10)
riceEntry = Entry(
    F3, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
riceEntry.grid(row=2, column=1, ipady=5, ipadx=5)
riceEntry.insert(0,0)

oilLabel = Label(
    F3, text='Oil', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=3, column=0, padx=10, pady=10)
oilEntry = Entry(
    F3, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
oilEntry.grid(row=3, column=1, ipady=5, ipadx=5)
oilEntry.insert(0, 0)

teaLabel = Label(
    F3, text='Tea', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=4, column=0, padx=10, pady=10)
teaEntry = Entry(
    F3, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
teaEntry.grid(row=4, column=1, ipady=5, ipadx=5)
teaEntry.insert(0, 0)

sugarLabel = Label(
    F3, text='Sugar', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=5, column=0, padx=10, pady=10)
sugarEntry = Entry(
    F3, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
sugarEntry.grid(row=5, column=1, ipady=5, ipadx=5)
sugarEntry.insert(0, 0)

# Cold Drink Frame
F4 = LabelFrame(
    root, text='Cold Drinks', font=('times new roman', 15, 'bold'),
    fg='gold', bg='black', relief=GROOVE, bd=10
)
F4.place(x=670, y=180, width=325, height=380)

maazaLabel = Label(
    F4, text='Maaza', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=0, column=0, padx=10, pady=10)
maazaEntry = Entry(
    F4, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
maazaEntry.grid(row=0, column=1, ipady=5, ipadx=5)
maazaEntry.insert(0, 0)

pepsiLabel = Label(
    F4, text='Pepsi', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=1, column=0, padx=10, pady=10)
pepsiEntry = Entry(
    F4, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
pepsiEntry.grid(row=1, column=1, ipady=5, ipadx=5)
pepsiEntry.insert(0, 0)

spriteLabel = Label(
    F4, text='Sprite', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=2, column=0, padx=10, pady=10)
spriteEntry = Entry(
    F4, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
spriteEntry.grid(row=2, column=1, ipady=5, ipadx=5)
spriteEntry.insert(0, 0)

dewLabel = Label(
    F4, text='Dew', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=3, column=0, padx=10, pady=10)
dewEntry = Entry(
    F4, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
dewEntry.grid(row=3, column=1, ipady=5, ipadx=5)
dewEntry.insert(0, 0)

frootiLabel = Label(
    F4, text='Frooti', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=4, column=0, padx=10, pady=10)
frootiEntry = Entry(
    F4, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
frootiEntry.grid(row=4, column=1, ipady=5, ipadx=5)
frootiEntry.insert(0, 0)

cocacolaLabel = Label(
    F4, text='Coca Cola', font=('times new roman', 16, 'bold'),
    bg='black', fg='white'
).grid(row=5, column=0, padx=10, pady=10)
cocacolaEntry = Entry(
    F4, bd=8, relief=GROOVE, textvariable=IntVar(),
    font=('times new roman', 16, 'bold')
)
cocacolaEntry.grid(row=5, column=1, ipady=5, ipadx=5)
cocacolaEntry.insert(0, 0)

# Bill Area Frame
F5 = Frame(
    root, relief=GROOVE, bd=10
)
F5.place(x=1000, y=180, width=350, height=380)

billLabel = Label(
    F5, text='Bill', font='arial 15 bold', bd=7, relief=GROOVE
).pack(fill=X)

scrollbar = Scrollbar(F5, orient=VERTICAL)
textarea = Text(
    F5, yscrollcommand=scrollbar.set
)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)

# Buttons Frame
F6 = LabelFrame(
    root, text='Billing Menu', font=('times new roman', 15, 'bold'),
    fg='gold', bg='black', relief=GROOVE, bd=10
)
F6.place(x=0, y=560, relwidth=1, height=145)

cosmeticpriceLabel = Label(
    F6, text='Total Cosmetic Price', font=('times new roman', 14, 'bold'),
    bg='black', fg='white'
).grid(row=0, column=0, padx=20, pady=1, sticky='w')
cosmeticpriceEntry = Entry(
    F6, bd=8, relief=GROOVE, textvariable=StringVar(),
    font='arial 10 bold'
)
cosmeticpriceEntry.grid(row=0, column=1, ipadx=5, ipady=2)

cosmetictaxLabel = Label(
    F6, text='Cosmetic Tax', font=('times new roman', 14, 'bold'),
    bg='black', fg='white'
).grid(row=0, column=2, padx=20, pady=1, sticky='w')
cosmetictaxEntry = Entry(
    F6, bd=8, relief=GROOVE, textvariable=StringVar(),
    font='arial 10 bold'
)
cosmetictaxEntry.grid(row=0, column=3, ipadx=5, ipady=2)

grocerypriceLabel = Label(
    F6, text='Total Grocery Price', font=('times new roman', 14, 'bold'),
    bg='black', fg='white'
).grid(row=1, column=0, padx=20, pady=1, sticky='w')
grocerypriceEntry = Entry(
    F6, bd=8, relief=GROOVE, textvariable=StringVar(),
    font='arial 10 bold'
)
grocerypriceEntry.grid(row=1, column=1, ipadx=5, ipady=2)

grocerytaxLabel = Label(
    F6, text='Grocery Tax', font=('times new roman', 14, 'bold'),
    bg='black', fg='white'
).grid(row=1, column=2, padx=20, pady=1, sticky='w')
grocerytaxEntry = Entry(
    F6, bd=8, relief=GROOVE, textvariable=StringVar(),
    font='arial 10 bold'
)
grocerytaxEntry.grid(row=1, column=3, ipadx=5, ipady=2)

colddrinkpriceLabel = Label(
    F6, text='Total Cold Drink Price', font=('times new roman', 14, 'bold'),
    bg='black', fg='white'
).grid(row=2, column=0, padx=20, pady=1, sticky='w')
colddrinkpriceEntry = Entry(
    F6, bd=8, relief=GROOVE, textvariable=StringVar(),
    font='arial 10 bold'
)
colddrinkpriceEntry.grid(row=2, column=1, ipadx=5, ipady=2)

colddrinktaxLabel = Label(
    F6, text='Cold Drink Tax', font=('times new roman', 14, 'bold'),
    bg='black', fg='white'
).grid(row=2, column=2, padx=20, pady=1, sticky='w')
colddrinktaxEntry = Entry(
    F6, bd=8, relief=GROOVE, textvariable=StringVar(),
    font='arial 10 bold'
)
colddrinktaxEntry.grid(row=2, column=3, ipadx=5, ipady=2)

totalbillLabel = Label(
    F6, text='Total Bill', font=('times new roman', 14, 'bold'),
    bg='black', fg='white'
).grid(row=3, column=0, padx=20, pady=1, sticky='w')
totalbillEntry = Entry(
    F6, bd=8, relief=GROOVE, textvariable=StringVar(),
    font='arial 10 bold'
)
totalbillEntry.grid(row=3, column=1, ipadx=5, ipady=2)

btnFrame = Frame(F6, bd=7, relief=GROOVE)
btnFrame.place(x=770, width=580, height=105)

totalBtn = Button(
    btnFrame, text='Total', bg='black', fg='white',
    bd=5, relief=GROOVE, padx=2, pady=15, width=5,
    font='arial 12 bold', command=total
)
totalBtn.grid(row=0, column=0, padx=2, pady=5)

generateBtn = Button(
    btnFrame, text='Bill', bg='black', fg='white',
    bd=5, relief=GROOVE, padx=2, pady=15, width=5,
    font='arial 12 bold', command=bill_area
)
generateBtn.grid(row=0, column=1, padx=2, pady=5)

clearBtn = Button(
    btnFrame, text='Clear', bg='black', fg='white',
    bd=5, relief=GROOVE, padx=2, pady=15, width=5,
    font='arial 12 bold', command=clear
)
clearBtn.grid(row=0, column=2, padx=2, pady=5)

exitBtn = Button(
    btnFrame, text='Exit', bg='black', fg='white',
    bd=5, relief=GROOVE, padx=2, pady=15, width=5,
    font='arial 12 bold', command=exit
)
exitBtn.grid(row=0, column=3, padx=2, pady=5)

addBtn = Button(
    btnFrame,text='Add', bg='black', fg='white',
    bd=5,relief=GROOVE, padx=2, pady=15, width=5,
    font='arial 12 bold',command=add_product
)
addBtn.grid(row=0, column=4, padx=2, pady=5)

deleteBtn = Button(
    btnFrame, text='Delete', bg='black', fg='white',
    bd=5, relief=GROOVE, padx=2, pady=15, width=5,
    font='arial 12 bold', command=delete_product
)
deleteBtn.grid(row=0, column=5, padx=2, pady=5)

lowBtn = Button(
    btnFrame, text='Low Stock', bg='black', fg='white',
    bd=5, relief=GROOVE, padx=2, pady=15, width=10,
    font='arial 12 bold', command=low_stock_report
)
lowBtn.grid(row=0, column=6, padx=2, pady=5)

open_login_window()
root.mainloop()