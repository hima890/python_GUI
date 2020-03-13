# here we import the libs
from tkinter import *
import backEndScript


# the logic part of the programe shoude come first so it can work
# as you can see blow the function nd there name witch also def. there job 
def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])


def view_command():
    list1.delete(0, END)
    for row in backEndScript.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backEndScript.search(title_text.get(), auther_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backEndScript.insert(title_text.get(), auther_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), auther_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    backEndScript.delete(selected_tuple[0])


def update_command():
    backEndScript.update(selected_tuple[0],title_text.get(), auther_text.get(), year_text.get(), isbn_text.get())
    print(title_text.get(), auther_text.get(), year_text.get(), isbn_text.get())

# here is the ui and ux part 
# first we get the window setup
windowe = Tk()
windowe.title('Book Store')
windowe.maxsize(500, 270)
windowe.minsize(500, 270)



# layout
# then the label and bottun and entry widget
# label part
l1 = Label(windowe, text='title')
l1.grid(row=0, column=0)

l2 = Label(windowe, text='auther')
l2.grid(row=0, column=2)

l3 = Label(windowe, text='year')
l3.grid(row=1, column=0)

l4 = Label(windowe, text='isbn')
l4.grid(row=1, column=2)

# entry part
title_text = StringVar()
e1 = Entry(windowe, text=title_text)
e1.grid(row=0, column=1)

auther_text = StringVar()
e2 = Entry(windowe, text=auther_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(windowe, text=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(windowe, text=isbn_text)
e4.grid(row=1, column=3)

# the list box widget for showing data
list1 = Listbox(windowe, height=10, width=35)
list1.grid(row=3, column=0, rowspan=8, columnspan=2)

# bading and styling with empty column and row
a = Label(windowe, height=1)
a.grid(row=2, column=0)
b = Label(windowe, height=1, text=' ')
b.grid(row=2, column=4 )

# the list box widget setup with the scrollbar
sb1 = Scrollbar(windowe)
sb1.grid(row=3, column=2, rowspan=6, columnspan=1) 
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# i dont now what this shit for but it makes the code run
list1.bind('<<ListboxSelect>>', get_selected_row)

# the bottun layout
b1 = Button(windowe, text='view all', width=12, command=view_command)
b1.grid(row=3, column=3)

b2 = Button(windowe, text='search entry', width=12, command=search_command)
b2.grid(row=4, column=3)

b3 = Button(windowe, text='add entry', width=12, command=add_command)
b3.grid(row=5, column=3)

b4 = Button(windowe, text='update', width=12, command=update_command)
b4.grid(row=6, column=3)

b5 = Button(windowe, text='delete', width=12, command = delete_command)
b5.grid(row=7, column=3)

b6 = Button(windowe, text='close', width=12, command=windowe.destroy)
b6.grid(row=8, column=3)

#and the main loop for the GUI
windowe.mainloop()