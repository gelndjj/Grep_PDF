from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import customtkinter, os, PyPDF2, re, shutil, time

root = Tk()
root.geometry('900x400')
root.title('PDF Global Regular Expression Print')
root.resizable(False, False)

#FRAMES
left_fr = customtkinter.CTkFrame(root,corner_radius=0,fg_color='#dbdadb',width=200)
left_fr.pack(side=LEFT,fill=Y)

cent_fr = customtkinter.CTkFrame(root, corner_radius=8, fg_color='#dbdadb', width=180, height=159)
cent_fr.place(x=223, y=232)

right_doc = customtkinter.CTkFrame(root, corner_radius=8, fg_color='#dbdadb', width=465, height=159)
right_doc.place(x=421, y=232)

#LABEL FRAMES
frame_title = LabelFrame(left_fr, text='Global Regular Expression\n Print',fg='#5c5b5b', bg='#dbdadb',relief=GROOVE)
frame_title.place(relx=0.07,rely=0.01)

frame_search = LabelFrame(left_fr, text='Search for',fg='#5c5b5b', bg='#dbdadb')
frame_search.place(relx=0.07,rely=0.40)

frame_find = LabelFrame(cent_fr,text='test',fg='#5c5b5b', bg='#dbdadb', width=50)
frame_find.place(relx=0.5,rely=0.5)

#LABELS
title = Label(frame_title, bg='#dbdadb',fg='white',text='PDF GREP',font=('Brush Script MT',26,'italic'))
title.pack()

txt_left2 = Label(frame_search, bg='#dbdadb',fg='#5c5b5b',text='Type in text you look for :   ')
txt_left2.pack()

txt_right_doc = customtkinter.CTkLabel(right_doc, bg_color='#dbdadb',text_color='#5c5b5b',text='Search by using Regular Expressions - Instructions')
txt_right_doc.place(relx=0.05, rely=0.01)

#OPEN A FOLDER
def open_folder():
    
    path = filedialog.askdirectory()
    result_txt.delete(0,END)
    total = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pdf') or file.endswith('.PDF'):
                total +=1
                full_path = os.path.join(root,file)
                result_txt.insert(END, f'{full_path}')
    create_file = open(os.path.expanduser('~/pdf_gather.txt'),'w')
    for item in result_txt.get(0,END):
        create_file.write(f'{item}\n')
    size()

#SEARCH INSIDE PDF
def search_pdfs_full_open():
    pattern = txt_input.get()
    re_pattern = f'{pattern}'

    file_pdf_path = open(os.path.expanduser('~/pdf_gather.txt'),'r')
    result_txt1.delete(0,END)
    for line in file_pdf_path.readlines():
        lEn = len(line)
        full_line = line[:lEn - 1]
        with open(full_line, 'rb') as f:
            pdf_file = PyPDF2.PdfReader(f)
            for p in range(pdf_file.numPages):
                page_found = p
                page = pdf_file.getPage(p)
                page_content = page.extract_text()
                result = re.findall(re_pattern, page_content)
                result_occurence = result.count(re_pattern)     

                if result :
                    result_txt1.insert(END,f'\'{result[0]}\' found {result_occurence} time(s) in page {page_found} inside the document: {full_line}\n')

def clear(event):
        
    result_txt.delete(0,END)
    result_txt1.delete(0,END)
    txt_input.delete(0,END)
    info.destroy()
    result.destroy()

def size():
    global info
    global result

    total = 0
    size_folder = 0
    MB = 1024*1024

    for item in result_txt.get(0,END):
        total += 1
        size_folder += os.path.getsize(item)
    result = customtkinter.CTkLabel(cent_fr, text = f'Total = {total} pdf file(s)\n'
                                                     'Size =  {:2f} MB'.format(size_folder/MB))
    result.place(relx=0.15, rely=0.1)
    info = customtkinter.CTkLabel(cent_fr, text='Press Shift + down\nto clear results')
    info.place(relx=0.15, rely=0.4)

switch_on = True
def show_ins():
    global switch_on

    if switch_on:
        expression_ins.insert(END,'\d = A digit\n\w = Alphanumeric\n\s = White space\n\D = A non digit\n\W = Non-alphanumeric\n\S = Non-whitespace\n[a-zA-Z] = Alphabet characters\n\n\'+\' = Occurs one or more times\n{3} = Occurs 3 times\n{2,5} = Occurs 2 to 5 times\n{2,} = Occurs 2 or more\n\'\*\' = Occurs zero or more times\n\'?\' = Once or more\n\nFor instance, the following pattern \'\d\d\d\d-\d\d-\d\d\' can\nfind 1970-01-01 among others.')
        switch_on = False

    else:
        expression_ins.delete('1.0',END)
        switch_on = True

def quit():
    try:
        os.remove(os.path.expanduser('~/pdf_gather.txt'))
        time.sleep(0.5)
        root.destroy()
    except:
        root.destroy()

#INPUT ENTRY 
txt_input = customtkinter.CTkEntry(frame_search,width=120, border_width=1)
txt_input.pack(padx=2,pady=15)

#BUTTONS
btn_open_path = customtkinter.CTkButton(frame_title,text='Open a folder', width=140, height=32,border_width=2, corner_radius=20, command=open_folder)
btn_open_path.pack(padx=2,pady=15)
btn_search = customtkinter.CTkButton(frame_search, text='Go ahead',width=140,height=32,border_width=2, corner_radius=20, command=search_pdfs_full_open)
btn_search.pack(padx=2,pady=15)
btn_exit = customtkinter.CTkButton(root, text='Quit', width=60,fg_color='#989da1',border_width=2, hover_color='black' ,command=quit)
btn_exit.place(relx=0.02, rely=0.895)

btn_show_ins = customtkinter.CTkSwitch(right_doc,text='', command=show_ins)
btn_show_ins.place(relx=0.75, rely=0.04)

#TEXTBOX
result_txt = Listbox(root,height=11, width=25, bd=3)
result_txt.place(x=225,y=20)

result_txt1 = Listbox(root,height=11, width=43,bd=3)
result_txt1.place(x=490,y=20)

expression_ins = customtkinter.CTkTextbox(right_doc,height=110, width=400,fg_color='white', corner_radius=4, border_width=2)
expression_ins.place(x=20, y=33)

root.bind('<Shift-Down>', clear)

root.mainloop()