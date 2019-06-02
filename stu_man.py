import tkinter as tk
from tkinter import ttk
import stu_sql as sq
mainWindow = tk.Tk()
mainWindow.title("STUDENT MANAGEMENT SYSTEM")

label_1 = tk.Label(mainWindow, text="COLLEGE MANAGEMENT PORTAL", font=("Sylfaen", 20))
label_1.pack()

button_1 = tk.Button(mainWindow,text="ADD_STUDENT",command=lambda:add(),padx=(20),pady=(10), width=20)
button_1.pack()

button2 = tk.Button(mainWindow,text="UPDATE_STUDENT", command=lambda: update(), padx=(20),pady=(10), width=20)
button2.pack()

button3 = tk.Button(mainWindow,text="DELETE_STUDENT", command=lambda: delete(),padx=(20),pady=(10), width=20)
button3.pack()

button4 = tk.Button(mainWindow,text="VIEW_STUDENT", command=lambda: view(),padx=(20),pady=(10), width=20)
button4.pack()

button5 = tk.Button(mainWindow,text="SEARCH_STUDENT", command=lambda: search(),padx=(20),pady=(10), width=20)
button5.pack()

def add():
    addWindow = tk.Tk()
    addWindow.title("ADD STUDENT DETAILS")

    name_label = tk.Label(addWindow, text="ENTER  THE NAME: ",)
    name_label.pack()
    name_entry = tk.Entry(addWindow)
    name_entry.pack()
    branch_label = tk.Label(addWindow, text="ENTER STREAM/BRANCH: " ,)
    branch_label.pack()
    branch_entry = tk.Entry(addWindow)
    branch_entry.pack()
    section_label = tk.Label(addWindow, text="ENTER THE SECTION OF STUDENT:")
    section_label.pack()
    section_entry = tk.Entry(addWindow)
    section_entry.pack()
    roll_label = tk.Label(addWindow, text="ENTER ROLL_NO:",)
    roll_label.pack()
    roll_entry = tk.Entry(addWindow)
    roll_entry.pack()
    grade_label = tk.Label(addWindow, text="ENTER THE GRADE: ",)
    grade_label.pack()
    grade_entry = tk.Entry(addWindow)
    grade_entry.pack()

    button6 = tk.Button(addWindow,text="OK", command=lambda: sq.insert_data(name_entry.get(),branch_entry.get(),section_entry.get(),
                                            roll_entry.get(), grade_entry.get()), padx=(20), pady=(10))
    button6.pack()

    addWindow.mainloop()



def update():
    updateWindow = tk.Tk()
    updateWindow.title("UPDATE STUDENT DETAILS")
    roll_label = tk.Label(updateWindow,text="Enter the roll number")
    roll_label.pack()
    roll_entry = tk.Entry(updateWindow)
    roll_entry.pack()
    button1 = tk.Button(updateWindow,text="SHOW DETAILS",command=lambda: show_detail(str(roll_entry.get())))
    button1.pack()

def view():

     viewWindow = tk.Tk()

     viewWindow.title("VIEW DETAILS OF STUDENTS")

     appLabel = tk.Label(viewWindow, text="STUDENT MANAGEMENT SYSTEM DATA",)
     appLabel.config(font=("Sylfaen", 30))
     appLabel.pack()

     tree = ttk.Treeview(viewWindow)
     tree["columns"] = ("one", "two", "three", "four", "five")

     tree.heading("one", text="BRANCH NAME")
     tree.heading("two", text="SECTION")
     tree.heading("three", text="ROLL NUMBER")
     tree.heading("four", text="GRADE")
     tree.heading("five", text=" ")

     cursor = sq.view_data()
     i = 0

     for row in cursor:
        tree.insert('', i, text= str(row[0]),
                     values=(row[1], row[2],
                             row[3], row[4]))
        i = i + 1

     tree.pack()
     viewWindow.mainloop()

def delete():
    deleteWindow = tk.Tk()
    deleteWindow.title("DELETE THE STUDENT DETAILS")

    roll_label = tk.Label(deleteWindow, text="Enter the roll number")
    roll_label.pack()
    roll_entry = tk.Entry(deleteWindow)
    roll_entry.pack()
    button1 = tk.Button(deleteWindow, text="DELETE DATA", command=lambda: sq.delete_data(str(roll_entry.get())))
    button1.pack()
    deleteWindow.mainloop()

def search():
    searchWindow = tk.Tk()
    searchWindow.title("SEARCH THE STUDENT DETAILS")

    roll_label = tk.Label(searchWindow, text="Enter the roll number")
    roll_label.pack()
    roll_entry = tk.Entry(searchWindow)
    roll_entry.pack()
    button1 = tk.Button(searchWindow, text="SEARCH DATA", command=lambda: show_search(str(roll_entry.get())))
    button1.pack()
    searchWindow.mainloop()

def show_detail(roll_entry):
    cursor = sq.fetch_data(roll_entry)
    addWindow = tk.Tk()
    addWindow.title("ADD STUDENT DETAILS")

    name_label = tk.Label(addWindow, text="ENTER  THE NAME: ", )
    name_label.pack()
    name_entry = tk.Entry(addWindow)
    name_entry.insert(0, cursor[0])
    name_entry.pack()
    branch_label = tk.Label(addWindow, text="ENTER STREAM/BRANCH: ", )
    branch_label.pack()
    branch_entry = tk.Entry(addWindow)
    branch_entry.insert(0, cursor[1])
    branch_entry.pack()
    section_label = tk.Label(addWindow, text="ENTER THE SECTION OF STUDENT:")
    section_label.pack()
    section_entry = tk.Entry(addWindow)
    section_entry.insert(0, cursor[2])
    section_entry.pack()
    roll_label = tk.Label(addWindow, text="ENTER ROLL_NO:", )
    roll_label.pack()
    roll_entry = tk.Entry(addWindow)
    roll_entry.insert(0, cursor[3])
    roll_entry.pack()
    grade_label = tk.Label(addWindow, text="ENTER THE GRADE: ", )
    grade_label.pack()
    grade_entry = tk.Entry(addWindow)
    grade_entry.insert(0, cursor[4])
    grade_entry.pack()

    button6 = tk.Button(addWindow, text="UPDATE",
                        command=lambda: sq.update_data(name_entry.get(), branch_entry.get(), section_entry.get(),
                                                str(roll_entry.get()), str(grade_entry.get())), padx=(20), pady=(10))
    button6.pack()

    addWindow.mainloop()


def show_search(roll_entry):
    cursor = sq.fetch_data(roll_entry)
    addWindow = tk.Tk()
    addWindow.title("ADD STUDENT DETAILS")

    name_label = tk.Label(addWindow, text="ENTER  THE NAME: " )
    name_label.pack()
    namelabel = tk.Label(addWindow, text=cursor[0] )
    namelabel.pack()
    branch_label = tk.Label(addWindow, text="ENTER STREAM/BRANCH: " )
    branch_label.pack()
    branchlabel = tk.Label(addWindow, text= cursor[1])
    branchlabel.pack()
    section_label = tk.Label(addWindow, text="ENTER THE SECTION OF STUDENT:")
    section_label.pack()
    sectionlabel = tk.Label(addWindow, text=cursor[2])
    sectionlabel.pack()
    roll_label = tk.Label(addWindow, text="ENTER ROLL_NO:")
    roll_label.pack()
    rolllabel = tk.Label(addWindow, text=cursor[3])
    rolllabel.pack()
    grade_label = tk.Label(addWindow, text="ENTER THE GRADE: ")
    grade_label.pack()
    gradelabel = tk.Label(addWindow, text=cursor[4])
    gradelabel.pack()

    addWindow.mainloop()







mainWindow.mainloop()









