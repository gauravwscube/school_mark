# School Mark Sheet
from tkinter import *
from tkinter.messagebox import askokcancel 

def get_data():
    name = st_name_1.get()
    
    hindi = hindi_name_1.get()
    english = english_name_1.get()
    sst = sst_name_1.get()
    science = science_name_1.get()
    maths = maths_name_1.get()

    total = hindi+english+sst+science+maths

    per = (total/500)*100

    div = ""

    if per>=60:
        div = "1 st Div"
    elif per<60 and per>=50:
        div = "2 nd Div"
    elif per<50 and per>=35:
        div = "3 rd Div"
    else:
        div = "Fail"

    messagebox(name,total,per,div)


def messagebox(*data):
    print_1 = f""" 
    Name : {data[0]}
    Total : {data[1]}
    Percentage : {data[2]}
    Division : {data[3]}
    """
    askokcancel(title="Wscube E School",message=print_1)

win = Tk() # start
#-------------------------------
win.title("Wscube E School")
win.config(bg = "yellow")
# win.iconbitmap("unnamed.ico")
win.geometry("550x650")
win.resizable(False,False)

#-------------------------------- 
# title name 
school_name = Label(win,text="Wscube E School",
    font=("Times New Roman",40,"bold"),bg = "yellow")
school_name.place(x=100,y=20,height=60,width=400)

#-------------------------------- 
# Name Entry
st_name = Label(win,text="Student Name",
    font=("Times New Roman",20,"bold"))
st_name.place(x=10,y=100,height=40,width=200)

st_name_1=StringVar()
st_name_Entry = Entry(win,font=("Times New Roman",20,"bold")
    ,textvariable=st_name_1)
st_name_Entry.place(x=230,y=100,height=40,width=300)

#--------------------------------
# Subject name 
subject_name = Label(win,text="Subject Number",
    font=("Times New Roman",30,"bold"),bg="yellow")
subject_name.place(x=100,y=160,height=60,width=400)

#--------------------------------
# variable
hindi_name_1=DoubleVar()
english_name_1=DoubleVar()
sst_name_1=DoubleVar()
science_name_1=DoubleVar()
maths_name_1=DoubleVar()

#---------------------------------
# subject No.

hindi_name = Label(win,text="Hindi",
    font=("Times New Roman",20,"bold"))
hindi_name.place(x=10,y=240,height=40,width=200)

hindi_name_Entry = Entry(win,
    font=("Times New Roman",20,"bold"),textvariable=hindi_name_1)
hindi_name_Entry.place(x=230,y=240,height=40,width=300)
#----------------------
english_name = Label(win,text="English",
    font=("Times New Roman",20,"bold"))
english_name.place(x=10,y=300,height=40,width=200)

english_name_Entry = Entry(win,
    font=("Times New Roman",20,"bold"),textvariable=english_name_1)
english_name_Entry.place(x=230,y=300,height=40,width=300)
#------------------------
science_name = Label(win,text="Science",
    font=("Times New Roman",20,"bold"))
science_name.place(x=10,y=360,height=40,width=200)

science_name_Entry = Entry(win,
    font=("Times New Roman",20,"bold"),textvariable=science_name_1)
science_name_Entry.place(x=230,y=360,height=40,width=300)
#--------------------------
maths_name = Label(win,text="Maths",
    font=("Times New Roman",20,"bold"))
maths_name.place(x=10,y=420,height=40,width=200)

maths_name_Entry = Entry(win,
    font=("Times New Roman",20,"bold"),textvariable=maths_name_1)
maths_name_Entry.place(x=230,y=420,height=40,width=300)
#------------------------------
sst_name = Label(win,text="SST",
    font=("Times New Roman",20,"bold"))
sst_name.place(x=10,y=480,height=40,width=200)

sst_name_Entry = Entry(win,
    font=("Times New Roman",20,"bold"),textvariable=sst_name_1)
sst_name_Entry.place(x=230,y=480,height=40,width=300)
#--------------------------------
# Button

button = Button(win,text="Done",
    font=("Times New Roman",20,"bold"),command=get_data)
button.place(x=200,y=540,height=60,width=200)




win.mainloop() # stop



