from tkinter import *
root = Tk()
root.geometry("400x250")
root.configure(background = 'black')
root.title("Currency Converter")
OPTIONS = {
'Australian Dollar':49.10,
'Brazilian Real':17.30,
'British Pound':90.92,
'Chinese Yuan':10.29,
'Euro':77.85,
'HongKong Dollar':8.83,
'Indonesian Rupiah':0.004864,
'Japanese Yen':0.628,
'Pakistani Rupee':0.49,
'SriLankan Rupee':0.39,
'Swiss France':69.62,
'Us Dollar':69.32
}
heading = Label(root, text="WELCOME TO CURRENCY CONVERTER", font=('arial 13 bold'), fg="steelblue",bg="black").pack(pady=10)
entr_amt = Label(root, text="Enter Amount in indian rupees", font=('arial 13 bold'),fg="red",bg="black").place(x=70, y=50)
my_num= IntVar()
ent_box = Entry(root, width=26, textvariable=my_num).place(x=120, y=90)
variable1 = StringVar(root)
option = OptionMenu(root,variable1,*OPTIONS)
option.place(x=130 , y=125,width=130, height=30)
Amount1_field = Entry(root)
Amount1_field.place(x=130,y=210)
def converter():
	price = my_num.get()
	answer = variable1.get()
	DICT = OPTIONS.get(answer,None)
	converted = float(price)/float(DICT)
	Amount1_field.insert(0, str(converted))
btn1 = Button(root, text="Convert", width=8, height=1, bg="lightgreen", command=converter).place(x=160, y=170)
root.mainloop()
