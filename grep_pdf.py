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

right_fr = customtkinter.CTkFrame(root,corner_radius=0, fg_color='#ebebeb')
right_fr.pack(fill=BOTH)

cent_fr = customtkinter.CTkFrame(root, corner_radius=8, fg_color='#dbdadb', width=180, height=160)
cent_fr.place(x=225, y=230)

right_doc = customtkinter.CTkFrame(root, corner_radius=8, fg_color='#dbdadb', width=465, height=115)
right_doc.place(x=421, y=232)

#LABEL FRAMES
frame_title = LabelFrame(left_fr, text='Global Regular Expression\n Print',fg='#5c5b5b', bg='#dbdadb',relief=GROOVE)
frame_title.place(relx=0.07,rely=0.01)

frame_search = LabelFrame(left_fr, text='Search for',fg='#5c5b5b', bg='#dbdadb')
frame_search.place(relx=0.07,rely=0.40)

frame_find = LabelFrame(cent_fr, text='Options',fg='#5c5b5b', bg='#dbdadb')
frame_find.place(relx=0.07,rely=0.01)

#LABELS
title = Label(frame_title, bg='#dbdadb',fg='white',text='PDF GREP',font=('Brush Script MT',26,'italic'))
title.pack()

txt_left2 = Label(frame_search, bg='#dbdadb',fg='#5c5b5b',text='Type in text you look for :   ')
txt_left2.pack()

txt_left3 = customtkinter.CTkLabel(frame_find, bg_color='#dbdadb',text_color='#5c5b5b',text='Find                        ')
txt_left3.pack()

txt_right_doc = customtkinter.CTkLabel(right_doc, bg_color='#dbdadb',text_color='#5c5b5b',text='Search by using Regular Expressions - Instructions')
txt_right_doc.place(relx=0.05, rely=0.01)

#OPEN A FOLDER
def open_folder():
    var_btn_size.set('0')
    path = filedialog.askdirectory()
    result_txt.delete('1.0',END)
    total = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pdf') or file.endswith('.PDF'):
                total +=1
                full_path = os.path.join(root,file)
                result_txt.insert(END, f'{full_path}\n')
    pdf_count = customtkinter.CTkLabel(left_fr, text=f'PDF files found: {total}')
    pdf_count.place(x=43, y=330)
    left_fr.after(3000, lambda: pdf_count.destroy())

    create_file = open(os.path.expanduser('~/pdf_gather.txt'),'w')
    create_file.write(result_txt.get('1.0',END))
    create_file.truncate(create_file.tell()-1)
    create_file.close()


#SEARCH INSIDE PDF
def search_pdfs_full_open(event):
    pattern = txt_input.get()
    re_pattern = f'{pattern}'

    file_pdf_path = open(os.path.expanduser('~/pdf_gather.txt'),'r')
    result_txt1.delete('1.0',END)
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

def count_pdf():
        total = 0
        file_pdf_path = open(os.path.expanduser('~/pdf_gather.txt'),'r')
        for line in file_pdf_path.readlines():
            total += 1
        pdf_count_res = customtkinter.CTkLabel(left_fr, text=f'PDF files found: {total}')
        pdf_count_res.place(x=43, y=210)
        left_fr.after(3000, lambda: pdf_count_res.destroy())

def clear(event):
        
    result_txt.delete('1.0',END)
    result_txt1.delete('1.0',END)
    result_txt_2.delete('1.0',END)
    txt_input.delete(0,END)
    find_txt.delete(0,END)

def size():

    result_txt_2.delete('1.0',END)
    file_pdf_path = open(os.path.expanduser('~/pdf_gather.txt'),'r')
    total = 0
    size_folder = 0
    MB = 1024*1024
    
    if var_btn_size.get() == 1:
        for line in file_pdf_path.readlines():
            total += 1
            size_folder += os.path.getsize(line[:-1])
    result_txt_2.insert(END,f'{total} file(s) found for a total of ''{:2f} MB'.format(size_folder/MB))

    if var_btn_size.get() == 0:
        result_txt_2.delete('1.0',END)

def find(event):
    total = 0
    word = find_txt.get()
    result_txt.tag_config('tag',foreground='#3a8ed0',background = '#dbdbda',underline=1)
    word_start = result_txt.search(word,'1.0',END)
    word_end = '+%dc' % len(word)
    while word_start:
        full_word = word_start + word_end
        result_txt.tag_add('tag',word_start, full_word)
        word_start = result_txt.search(word, full_word,END)
        total += 1
    txt_left4 = Label(root, bg='#ebebeb',fg='blue',text=f'\' {word} \' found {total} time(s)', font=('Arial',12,'italic'))
    txt_left4.place(relx=0.25,rely=0.04)
    root.after(4000, lambda: txt_left4.destroy())

switch_on = True
def show_ins():
    global switch_on

    if switch_on:
        expression_ins.insert(END,'\d = A digit\n\w = Alphanumeric\n\s = White space\n\D = A non digit\n\W = Non-alphanumeric\n\S = Non-whitespace\n[a-zA-Z] = Alphabet characters\n\n\'+\' = Occurs one or more times\n{3} = Occurs 3 times\n{2,5} = Occurs 2 to 5 times\n{2,} = Occurs 2 or more\n\'\*\' = Occurs zero or more times\n\'?\' = Once or more\n\nFor instance \'\d\d\d\d-\d\d-\d\d\' can find 1970-01-01\namong others.')
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

find_txt =customtkinter.CTkEntry(frame_find, width=120,fg_color='white', corner_radius=8)
find_txt.pack(padx=2, pady=2)

#CHECK BUTTONS
var_btn_size = IntVar()
btn_show = customtkinter.CTkCheckBox(frame_find, text='Get number/size', variable=var_btn_size, onvalue=1, offvalue=0, command=size)
btn_show.pack(padx=12,pady=22)

#BUTTONS
btn_open_path = customtkinter.CTkButton(frame_title,text='Open a folder', width=140, height=32,border_width=2, corner_radius=20, command=open_folder)
btn_open_path.pack(padx=2,pady=15)
btn_search = customtkinter.CTkButton(frame_search, text='Go ahead',width=140,height=32,border_width=2, corner_radius=20, command=search_pdfs_full_open)
btn_search.pack(padx=2,pady=15)
btn_exit = customtkinter.CTkButton(root, text='Quit', width=60,fg_color='#989da1',border_width=2, command=quit)
btn_exit.place(relx=0.920, rely=0.895)

btn_show_ins = customtkinter.CTkSwitch(right_doc,text='', command=show_ins)
btn_show_ins.place(relx=0.75, rely=0.04)

#TEXTBOX
result_txt = customtkinter.CTkTextbox(root,height=180, width=250,fg_color='white', corner_radius=8)
result_txt.place(x=225,y=40)

result_txt1 = customtkinter.CTkTextbox(root,height=180, width=390,fg_color='white', corner_radius=8)
result_txt1.place(x=495,y=40)

result_txt_2 = customtkinter.CTkTextbox(root,height=5, width=400,fg_color='white', corner_radius=8,border_width=1)
result_txt_2.place(x=420,y=355)

expression_ins = customtkinter.CTkTextbox(right_doc,height=70, width=400,fg_color='white', corner_radius=4, border_width=2)
expression_ins.place(x=20, y=33)


find_txt.bind('<Return>',find)
txt_input.bind('<Return>',search_pdfs_full_open)
root.bind('<Shift-Down>', clear)
root.mainloop()
