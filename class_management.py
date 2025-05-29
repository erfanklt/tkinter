from tkinter import *

# Define two sets for classes
class1_students = set()
class2_students = set()

# Create main window
window = Tk()
window.geometry("400x500")
window.config(bg="lightgray")

# Labels
label1 = Label(window, text="Class 1:")
label1.place(x=50, y=20)

label2 = Label(window, text="Class 2:")
label2.place(x=50, y=60)

# Entry fields
entry1 = Entry(window)
entry1.place(x=100, y=20)

entry2 = Entry(window)
entry2.place(x=100, y=60)

# Result display label
result_label = Label(window, text="", bg="white", width=40, height=20)
result_label.place(x=50, y=150)

def add_to_class1():
    name = entry1.get()
    if name != "":
        class1_students.add(name)
        show_all_students()

def add_to_class2():
    name = entry2.get()
    if name != "":
        class2_students.add(name)
        show_all_students()

def show_all_students():
    text = "Students in Class 1:\n"
    for student in class1_students:
        text = text + student + "\n"
    text = text + "\nStudents in Class 2:\n"
    for student in class2_students:
        text = text + student + "\n"
    result_label.config(text=text)

def show_common():
    text = "Common Students:\n"
    found = False
    for student in class1_students:
        if student in class2_students:
            text = text + student + "\n"
            found = True
    if not found:
        text = "No common students found"
    result_label.config(text=text)

# Add buttons
add_button1 = Button(window, text="Add to Class 1", command=add_to_class1)
add_button1.place(x=250, y=20)

add_button2 = Button(window, text="Add to Class 2", command=add_to_class2)
add_button2.place(x=250, y=60)

# Show common students button
common_button = Button(window, text="Show Common Students", command=show_common)
common_button.place(x=150, y=100)

window.mainloop() 