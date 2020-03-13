from tkinter import *

windowe = Tk()

l1 = Label(windowe, text='title')
l1.grid(row=0, column=0)

l2 = Label(windowe, text='auther')
l2.grid(row=0, column=2)

l3 = Label(windowe, text='year')
l3.grid(row=1, column=0)

l4 = Label(windowe, text='isbn')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(windowe, text=title_text)
e1.grid(row=0, column=1)

auther_text = StringVar()
e2 = Entry(windowe, text=title_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(windowe, text=title_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(windowe, text=title_text)
e4.grid(row=1, column=3)


list1 = Listbox(windowe, height=10, width=35)
list1.grid(row=3, column=0, rowspan=8, columnspan=2)

a = Label(windowe, height=1)
a.grid(row=2, column=0)
b = Label(windowe, height=1, text=' ')
b.grid(row=2, column=4 )


sb1 = Scrollbar(windowe)
sb1.grid(row=3, column=2, rowspan=6, columnspan=1) 

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(windowe, text='view all', width=12)
b1.grid(row=3, column=3)

b2 = Button(windowe, text='search entry', width=12)
b2.grid(row=4, column=3)

b3 = Button(windowe, text='add entry', width=12)
b3.grid(row=5, column=3)

b4 = Button(windowe, text='update', width=12)
b4.grid(row=6, column=3)

b5 = Button(windowe, text='delete', width=12)
b5.grid(row=7, column=3)

b6 = Button(windowe, text='close', width=12)
b6.grid(row=8, column=3)


windowe.mainloop()