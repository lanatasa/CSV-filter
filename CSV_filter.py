from tkinter import *
from tkinter.ttk import Combobox, Notebook
from tkinter import filedialog as fd
import csv

file_name = ""

def filter_data():
    letter_value = letters_combobox_var.get()  
    date_value = date_entry.get()
    records_counter = 0
    data_listbox.delete(0, END)
    with open('babies_names.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line['FirstForename'][0] == letter_value:
                if line['yr'] == date_value:
                    data_listbox.insert('end', f'Date of birth : {line["yr"]}. Child name: {line["FirstForename"]}')
                    records_counter += 1
  
    records_value_init = 'Records found: '
    records_label.config(text=f'{records_value_init} {records_counter}')


def filter_custom_file_data():
    field_value = fields_combobox_var.get()
    row_counter = 0
    data_listbox2.delete(0, END)
    number_of_rows = int(row_entry.get())
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            row_counter += 1
            if row_counter != number_of_rows + 1:
                data_listbox2.insert('end', f'{field_value}: {line[field_value]}')
            else:
                records_label2.config(text='Records found: ')
                break
    records_value_init = 'Records found: '
    records_label2.config(text=f'{records_value_init} {number_of_rows}')


def select_file():
    filetypes = (
        ('Csv files', '*.csv'),
        ('All files', '*.*')
    )
    keys = ''

    global file_name
    file_name = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            keys = list(line.keys())
            break

        fields_combobox['values'] = keys


root = Tk()
root.resizable(0, 0)

root.title("CSV filter")
root.geometry("500x650")

notebook = Notebook(root)
first_frame = Frame(notebook)  # original frame
second_frame = Frame(notebook)  # custom frame

notebook.add(first_frame, text="Original Frame")
notebook.add(second_frame, text="Custom Frame")
notebook.pack(expand=1, fill="both")

# -------------- FRAME ONE ---------------------

# ---------  widget variables  ----------------

letters_combobox_var = StringVar()

# ---------    widgets   -------------------

filter_label_frame = LabelFrame(first_frame, text="Filter Options", width=440, height=150)
letter_label = Label(filter_label_frame, text="Pick a letter:")
letters_combobox = Combobox(filter_label_frame, textvariable=letters_combobox_var)
letters_combobox['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
letters_combobox.state(["readonly"])
letters_combobox.set("Select letter")

date_label = Label(filter_label_frame, text="Enter a date (1974 - 2020):")
date_entry = Entry(filter_label_frame)

filter_button = Button(filter_label_frame, text="FILTER", width=55, bg="lightgreen", command=filter_data)

data_listbox = Listbox(first_frame, width=73, height=25)
scroll_bar = Scrollbar(first_frame, orient=VERTICAL, command=data_listbox.yview)
data_listbox["yscrollcommand"] = scroll_bar.set
records_label = Label(first_frame, text="Records found: ")

# ---------- widgets placement -------------

filter_label_frame.place(x=30, y=30)
letter_label.place(x=20, y=20)
letters_combobox.place(x=110, y=20)
date_label.place(x=20, y=50)
date_entry.place(x=165, y=50)
filter_button.place(x=20, y=100)
data_listbox.place(x=30, y=190)
scroll_bar.pack(side="right", fill="y")
records_label.place(x=30, y=600)


# -------------- FRAME SECOND ---------------------

# --------- widget variables ----------------

fields_combobox_var = StringVar()

# ---------  widgets -------------------
select_file_button = Button(second_frame, text='Select file', command=select_file)
filter_label_frame2 = LabelFrame(second_frame, text='Filter Options', width=440, height=100)
fields_combobox = Combobox(filter_label_frame2, textvariable=fields_combobox_var)
fields_label = Label(filter_label_frame2, text='Select field: ')
filter_button2 = Button(filter_label_frame2, text='FILTER', width=55, bg='lightgreen', command=filter_custom_file_data)
data_listbox2 = Listbox(second_frame, height=26, width=73)
records_label2 = Label(second_frame, text='Records found: ')
row_entry = Entry(filter_label_frame2)
scroll_bar2 = Scrollbar(second_frame, orient=VERTICAL, command=data_listbox2.yview)
data_listbox2["yscrollcommand"] = scroll_bar2.set
row_label = Label(filter_label_frame2, text='Rows: ')

fields_combobox.set('Select field')

# ---------- widgets placement -------------

select_file_button.place(x=30, y=10)
filter_label_frame2.place(x=30, y=50)
fields_label.place(x=20, y=20)
fields_combobox.place(x=110, y=20)
filter_button2.place(x=20, y=50)
data_listbox2.place(x=30, y=160)
records_label2.place(x=30, y=590)
row_entry.place(x=300, y=20)
scroll_bar2.pack(side="right", fill="y")
row_label.place(x=260, y=20)

fields_combobox.state(['readonly'])

root.mainloop()
